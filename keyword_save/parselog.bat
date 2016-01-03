@echo off

echo "######### grep  "Fatal" -winr . #####################"
grep  "Fatal" -winr . 
echo @   
echo @  
echo "######### grep  "deadlock" -wnr . #####################"
grep  "deadlock" -winr . 
echo @   
echo @   
echo "######### [kernel] grep  "SMSM_RESET" -wnr .  ##########"
grep  "SMSM_RESET" -wnr .
echo @   
echo @ 



echo "######### [LOGCAT] grep  "Timed out waiting for " -nr .  ##########"
grep  "Timed out waiting for " -nr .
echo @   
echo @ 


echo "######### [kernel] grep  " Triggered from" -wnr . ---- for power off or on  reason  ##########"
grep  " Triggered from" -nr .
echo @   
echo @   


echo "######### [LOGCAT] grep  "over battery temperature" -nr .  ##########"
grep  "over battery temperature" -nr .
echo @   
echo @    [CMDQ][ERR]


rem echo "######### [LOGCAT] grep  "[CMDQ][ERR]" -nr .   ---- for cmdq error  ##########"
rem grep  "[CMDQ][ERR]" -nr .
rem echo @   
rem echo @

rem pil_vote_load_worker: Failed to load modem

echo "######### [kernel] grep  "panic" -wnr .  ##########"
grep  "panic" -wnr .
echo @   
echo @   
echo "######### [kernel] grep  "target.reset.count" -nr .  ##########"
grep  "target.reset.count" -nr .
echo @   
echo @   
echo "######### [kernel] grep  "unhandled page fault" -wnr .  ##########"
grep  "unhandled page fault" -wnr .
echo @   
echo @   
echo "######### [kernel] grep  "pgd = " -wnr .  ##########"
grep  "pgd = " -wnr .
echo @   
echo @   
echo "######### [kernel] grep  "PC is at JNI ERROR" -wnr .  ##########"
grep  "PC is at " -wnr .
echo @   
echo @   



echo "######### [kernel] grep  "rpm_err_fatal" -wnr .  ##########"
grep  "rpm_err_fatal" -wnr .
echo @   
echo @   

echo "######### [kernel] grep  "JNI ERROR" -wnr .  ##########"
grep  "JNI ERROR" -wnr .


echo @ 
echo @    

echo "######### grep  "Out of memory" -wnr . #############"
grep  "Out of memory" -nr . 
echo @   
echo @   


echo "######### grep  " Blocked" -wnr . #############"
grep  " Blocked" -nr . 
echo @   
echo @   battery does not charge full


echo "######### grep  "battery does not charge full" -wnr . #############"
grep  "battery does not charge full" -nr . 
echo @   
echo @   


echo "|||||||||||||||  MTK start---  |||||||||||||||||||"
rem [305:mtk_wmtd][WMT-CTRL][I]wmt_ctrl_evt_err_trg_assert:wmt-ctrl:drv_type(0),reason(32)
rem [305:mtk_wmtd][STP] mtk_wcn_stp_set_wmt_evt_err_trg_assert:[I] set evt err tigger assert flag to 1
echo "######### MTK =====  Grep  "wmt_ctrl_evt_err_trg_assert" -inr .  ##########"

echo "----------------------------------"
grep  "wmt_ctrl_evt_err_trg_assert" -inr .

echo "######### MTK =====  Grep  "mtk_wcn_stp_set_wmt_evt_err_trg_assert" -inr .  ##########"

echo "----------------------------------"
grep  "mtk_wcn_stp_set_wmt_evt_err_trg_assert" -inr .

echo "----------grep  over retry limit power reset ------------------------"
grep  "over retry limit power reset" -inr .

echo "----------grep  Timed out waiting for vsync 一般是显示卡住问题 ，典型log:  W hwcomposer: [JOB] (0) Timed out waiting for vsync... ------------------------"
grep  "Timed out waiting for vsync" -nr .
rdma underflow 

echo "----------grep  Timed out waiting for Dispatcher_0 一般是显示卡住问题 ，典型log:  Timed out waiting for Dispatcher_0------------------------"
grep  "Timed out waiting for Dispatcher_0" -nr .


echo "----------grep  disp ovl status error -----------------------"
grep  "disp ovl status error" -nr .

echo "----------grep  RDMA0 underflow :: for rdma underflow  -----------------------"
grep  "RDMA0 underflow" -nr .

echo "----------grep  TERROR:disp ovl status error 一般是显示卡住问题 ，典型log:  " 07-22 08:00:34.640 <3>[51934.297716]<0> (2)[32573:kworker/u8:2][DISP][_ovl_fence_release_callback #3059]ERROR:disp ovl status error!! stat=0x9"------------------------"
grep  "ERROR:disp ovl status error" -nr .


rem mali 13040000.MALI: Failed to soft-reset GPU (timed out after 500 ms), now attempting a hard reset
rem mali 13040000.MALI: Failed to hard-reset the GPU (timed out after 500 ms)
rem [MALI]!!!!MFG(GPU) subsys is still BUSY!!!!!, polling_count=-1

echo "---------- grep  "Failed to soft-reset" -nr .------------------------"
grep  "Failed to soft-reset" -nr .
echo "---------- grep  "Failed to soft-reset" -nr .------------------------"
grep  "Failed to hard-reset" -nr .



rem keyword: HWT,HW_REBOOT
echo "-------------MTK  HWT  ---------------------"
grep  "HWT," -iwnr .
echo "------------- MTK  HW_REBOOT  ---------------------"
grep  "HW_REBOOT," -inr .
echo "------------  MTK __dabt_svc  ---------------------"
grep  "__dabt_svc" -inr .



echo "||||||||||||||| --- MTK END  |||||||||||||||||||"
rem  =============== MTK END --------------------


echo "~~~~~~~~~   ## for android crash or ARR ## ~~~~~~~~~~~~~~~~~"

echo "~~~~~~~--------grep  "Input dispatching timed out" -nr .  for finding : anr  --------~~~~~"
grep  "Input dispatching timed out" -nr . 



echo @   
echo @   
rem echo "######### [kernel] grep  "dump" -wnr .  ##########"
rem grep  "dump" -wnr .
echo @   
echo @   
echo "######### [kernel] grep  "deadbaad" -wnr .  ##########"
grep  "deadbaad" -wnr .
echo @   
echo @   
echo "######### [kernel] grep  "kill" -wnr .  ##########"
grep  "kill" -winr .
echo @   
echo @   
echo "######### grep  "AndroidRuntime" -wnr . #############"
grep  "AndroidRuntime" -wnr . 
echo @ 
echo @    
echo "######### grep  "I DEBUG" -nr .  #############"
grep  "I DEBUG" -nr . 
echo @ 
echo @    
echo "######### grep  "disk I/O error" -wnr . #############"
grep  "disk I/O error" -nr . 
echo @ 
echo @    
echo "######### grep  "corrupt" -wnr . #############"
grep  "corrupt" -wnr . 
echo @ 
echo @    
echo "######### grep  "PLL failed to lock" -nr . #############"
grep  "PLL failed to lock" -wnr . 
echo @ 
echo @    
echo "######### grep  "Shutting down activity manager" -nr . #############"
grep  "Shutting down activity manager" -nr .  
echo @
echo @ 
rem echo "######### grep  "ShutdownThread:" -wnr . #############"
rem grep  "ShutdownThread:" -nr .  
rem echo @
rem echo @ 

echo "Search .... java.io.IOException  ... issue class: sd, database ..."
echo "#########  grep  "java.io.IOException" -inr .  ##########"
grep  "java.io.IOException" -inr .
echo @
echo @ 
rem kernel:: mmcblk1: rw=0, want=3860489, limit=3842048
rem kernel:: attempt to access beyond end of device
echo "#########  grep  "beyond end of device" -inr .  ##########"
grep  "beyond end of device" -inr .
echo @
echo @ 




echo "######### MTK =====  Grep  "MSDC_INT_DATCRCERR" -inr .  ##########"
grep  "MSDC_INT_DATCRCERR" -inr .
echo "----------------------------------"
echo "grep  "mmcblk0: error" -inr ."
echo "----------------------------------"
grep  "mmcblk0: error" -inr .
echo "----------------------------------"
echo "grep  "msdc_dump_trans_error" -inr ."
echo "----------------------------------"
grep  "msdc_dump_trans_error" -inr .
echo @
echo @ 




if {%1}=={} goto common

echo @ 
echo @    

rem echo "######### grep  "W dalvikvm" -nr . #############"
grep  "W dalvikvm" -nr . 
echo @   
echo @   
echo "######### grep  "E dalvikvm" -nr . #############"
grep  "E dalvikvm" -nr . 
echo @   
echo @   
rem echo "#########  grep  "lowmemorykiller" -wnr .  ##########"
rem grep  "lowmemorykiller" -wnr .
echo "##-------  grep  "to free" -wnr .  ---------------###"
grep  "to free" -nr .
echo @
echo @ 
echo "#########  grep  "can not find" -inr .  ##########"
grep  "can not find" -inr .
echo @
echo @ 
echo "Search .... java.io.IOException  ... issue class: sd, database ..."

echo "#########  grep  "java.io.IOException" -inr .  ##########"
grep  "java.io.IOException" -inr .
echo @
echo @ 
rem kernel:: mmcblk1: rw=0, want=3860489, limit=3842048
rem kernel:: attempt to access beyond end of device
rem  echo "#########  grep  "beyond end of device" -inr .  ##########"
rem  grep  "beyond end of device" -inr .
rem  echo @
rem  echo @ 



:common
rem pause
