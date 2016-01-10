#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-

import os
import Tkinter

def _load_tkdnd(master):
    tkdndlib = os.environ.get('TKDND_LIBRARY')
    if tkdndlib:
        master.tk.eval('global auto_path; lappend auto_path {%s}' % tkdndlib)
    master.tk.eval('package require tkdnd')
    master._tkdnd_loaded = True


class TkDND(object):
    def __init__(self, master):
        if not getattr(master, '_tkdnd_loaded', False):
            _load_tkdnd(master)
        self.master = master
        self.tk = master.tk

    # Available pre-defined values for the 'dndtype' parameter:
    #   text/plain
    #   text/plain;charset=UTF-8
    #   text/uri-list

    def bindtarget(self, window, callback, dndtype, event='<Drop>', priority=50):
        cmd = self._prepare_tkdnd_func(callback)
        return self.tk.call('dnd', 'bindtarget', window, dndtype, event,
                cmd, priority)

    def bindtarget_query(self, window, dndtype=None, event='<Drop>'):
        return self.tk.call('dnd', 'bindtarget', window, dndtype, event)

    def cleartarget(self, window):
        self.tk.call('dnd', 'cleartarget', window)


    def bindsource(self, window, callback, dndtype, priority=50):
        cmd = self._prepare_tkdnd_func(callback)
        self.tk.call('dnd', 'bindsource', window, dndtype, cmd, priority)

    def bindsource_query(self, window, dndtype=None):
        return self.tk.call('dnd', 'bindsource', window, dndtype)

    def clearsource(self, window):
        self.tk.call('dnd', 'clearsource', window)


    def drag(self, window, actions=None, descriptions=None,
            cursorwin=None, callback=None):
        cmd = None
        if cursorwin is not None:
            if callback is not None:
                cmd = self._prepare_tkdnd_func(callback)
        self.tk.call('dnd', 'drag', window, actions, descriptions,
                cursorwin, cmd)


    _subst_format = ('%A', '%a', '%b', '%D', '%d', '%m', '%T',
            '%W', '%X', '%Y', '%x', '%y')
    _subst_format_str = " ".join(_subst_format)

    def _prepare_tkdnd_func(self, callback):
        funcid = self.master.register(callback, self._dndsubstitute)
        cmd = ('%s %s' % (funcid, self._subst_format_str))
        return cmd

    def _dndsubstitute(self, *args):
        if len(args) != len(self._subst_format):
            return args

        def try_int(x):
            x = str(x)
            try:
                return int(x)
            except ValueError:
                return x

        A, a, b, D, d, m, T, W, X, Y, x, y = args

        event = Tkinter.Event()
        event.action = A       # Current action of the drag and drop operation.
        event.action_list = a  # Action list supported by the drag source.
        event.mouse_button = b # Mouse button pressed during the drag and drop.
        event.data = D         # The data that has been dropped.
        event.descr = d        # The list of descriptions.
        event.modifier = m     # The list of modifier keyboard keys pressed.
        event.dndtype = T
        event.widget = self.master.nametowidget(W)
        event.x_root = X       # Mouse pointer x coord, relative to the root win.
        event.y_root = Y
        event.x = x            # Mouse pointer x coord, relative to the widget.
        event.y = y

        event.action_list = str(event.action_list).split()
        for name in ('mouse_button', 'x', 'y', 'x_root', 'y_root'):
            setattr(event, name, try_int(getattr(event, name)))

        return (event, )



##  the second  tkdnd implement .
class DnD:
    def __init__(self, tkroot):
        self._tkroot = tkroot
        tkroot.tk.eval('package require tkdnd')
        # make self an attribute of the parent window for easy access in child classes
        tkroot.dnd = self

    def bindsource(self, widget, type=None, command=None, arguments=None, priority=None):
        '''Register widget as drag source; for details on type, command and arguments, see bindtarget().
        priority can be a value between 1 and 100, where 100 is the highest available priority (default: 50).
        If command is omitted, return the current binding for type; if both type and command are omitted,
        return a list of registered types for widget.'''
        command = self._generate_callback(command, arguments)
        tkcmd = self._generate_tkcommand('bindsource', widget, type, command, priority)
        res = self._tkroot.tk.eval(tkcmd)
        if type == None:
            res = res.split()
        return res

    def bindtarget(self, widget, type=None, sequence=None, command=None, arguments=None, priority=None):
        '''Register widget as drop target; type may be one of text/plain, text/uri-list, text/plain;charset=UTF-8
        (see the man page tkDND for details on other (platform specific) types);
        sequence may be one of '<Drag>', '<DragEnter>', '<DragLeave>', '<Drop>' or '<Ask>' ;
        command is the callback associated with the specified event, argument is an optional tuple of arguments
        that will be passed to the callback; possible arguments include: %A %a %b %C %c %D %d %L %m %T %t %W %X %x %Y %y
        (see the tkDND man page for details); priority may be a value in the range 1 to 100 ; if there are
        bindings for different types, the one with the priority value will be proceeded first (default: 50).
        If command is omitted, return the current binding for type, where sequence defaults to '<Drop>'.
        If both type and command are omitted, return a list of registered types for widget.'''
        command = self._generate_callback(command, arguments)
        tkcmd = self._generate_tkcommand('bindtarget', widget, type, sequence, command, priority)
        res = self._tkroot.tk.eval(tkcmd)
        if type == None:
            res = res.split()
        return res

    def clearsource(self, widget):
        '''Unregister widget as drag source.'''
        self._tkroot.tk.call('dnd', 'clearsource', widget)

    def cleartarget(self, widget):
        '''Unregister widget as drop target.'''
        self._tkroot.tk.call('dnd', 'cleartarget', widget)

    def drag(self, widget, actions=None, descriptions=None, cursorwindow=None, command=None, arguments=None):
        '''Initiate a drag operation with source widget.'''
        command = self._generate_callback(command, arguments)
        if actions:
            if actions[1:]:
                actions = '-actions {%s}' % ' '.join(actions)
            else:
                actions = '-actions %s' % actions[0]
        if descriptions:
            descriptions = ['{%s}'%i for i in descriptions]
            descriptions = '{%s}' % ' '.join(descriptions)
        if cursorwindow:
            cursorwindow = '-cursorwindow %s' % cursorwindow
        tkcmd = self._generate_tkcommand('drag', widget, actions, descriptions, cursorwindow, command)
        self._tkroot.tk.eval(tkcmd)

    def _generate_callback(self, command, arguments):
        '''Register command as tk callback with an optional list of arguments.'''
        cmd = None
        if command:
            cmd = self._tkroot._register(command)
            if arguments:
                cmd = '{%s %s}' % (cmd, ' '.join(arguments))
        return cmd

    def _generate_tkcommand(self, base, widget, *opts):
        '''Create the command string that will be passed to tk.'''
        tkcmd = 'dnd %s %s' % (base, widget)
        for i in opts:
            if i is not None:
                tkcmd += ' %s' % i
        return tkcmd

