import AlphaChip_Memory, AlphaChip_Rev2.Tkinter_Display_Start as Tkinter_Display_Start
# from CIS import AlphaChip_CIS
from ISP import AlphaChip_ISP, AlphaChip_ISP_Display, AlphaChip_ISP_Signal_Clear, AlphaChip_ISP_Recheck, AlphaChip_ISP_LED, AlphaChip_ISP_Pseudo
from CPU import AlphaChip_Firmware
import time, threading

# PiRA 1
#########################################################################################################################################################
#
#                                                                                                                  ###############
#                                                                                                                  # Active Mode #
#   #################    ################    ##############                                                        ###############  
#   # Power On Mode # => # Standby Mode # => # Watch Mode # =====================================================>                  
#   #################    ################    ##############                                                 
#                                                                                                                  
#                                                                                                                 
#
#########################################################################################################################################################

# PiRA 2
#########################################################################################################################################################
#
#                                                                                                                  ###############
#                                                                                                                  # Active Mode #
#   #################    ################    ##############                                                        ###############     ################
#   # Power On Mode # => # Standby Mode # => # Watch Mode # =====================================================>         |        => # Recheck Mode #
#   #################    ################    ##############                                                        ###############     ################
#                                                                                                                  # Detect Mode #
#                                                                                                                  ###############
#
#########################################################################################################################################################

# SSL-G 1
#########################################################################################################################################################
#
#                                                                                                                  ###############
#                                                                                                                  # Active Mode #
#   #################    ################    ##############    ####################    ########################    ###############      ################
#   # Power On Mode # => # Standby Mode # => # Watch Mode # => # LOW_Recheck_Mode # => # LED_ON(High Recheck) # =>                   => # Recheck Mode #
#   #################    ################    ##############    ####################    ########################    ###############      ################
#                                                                                                                  # Detect Mode #
#                                                                                                                  ###############
#
#########################################################################################################################################################

# SSL-G 2
#########################################################################################################################################################
#
#                                                                                                                  ###############
#                                                                                                                  # Active Mode #
#   #################    ################    ##############    ####################    ########################    ###############      ################
#   # Power On Mode # => # Standby Mode # => # Watch Mode # => # LOW_Recheck_Mode # => # LED_ON(High Recheck) # =>                   => # Recheck Mode #
#   #################    ################    ##############    ####################    ########################    ###############      ################
#                                                                                                                  # Detect Mode #
#                                                                                                                  ###############
#
#########################################################################################################################################################
Ext_GPIO_LED_ON_Mode_Signal = False
g_i_time = AlphaChip_Memory.g_N_mode['IDLE_MODE']

if AlphaChip_Memory.g_b_Debugging:
    AlphaChip_ISP_Display.display_status()
            
############################################################################################################ 확인 필요 ##########################
def Ext_Active_ON():
    AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_ACTIVE_MODE'] = True
def Ext_Active_OFF():
    AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_ACTIVE_MODE'] = False
def Ext_Button():
    AlphaChip_Memory.g_Ext_Botton_Push = True
############################################################################################################ 확인 필요 ##########################       

# 새로운 이미지 받기
def ISP_New_Frame(b_resualt):
    global g_i_Illuminance, g_i_x_Illuminance, g_i_Illuminance_delta_signal, g_i_Illuminance_delta, g_i_resualt
    while True:
        # if not b_resualt :
        #     b_first_print = True
        #     while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:               # 만약 CIS Setting이 변경 되었다면
        #         if AlphaChip_Memory.g_b_Debugging and b_first_print:
        #             print("ISP : MODE : NEW FRAME : WAIT CHANGE CIS SETTING")
        #             b_first_print = False
        #         continue    
        #     b_first_print = True
        #     AlphaChip_Memory.g_b_FRAME_READY = False                                        # ISP 새로운 Frame Signal 초기화
        #     while not AlphaChip_Memory.g_b_FRAME_READY or AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']: 
        #         if AlphaChip_Memory.g_b_Debugging and b_first_print:
        #             print("ISP : MODE : NEW FRAME : WAIT FRAME_READY")
        #             b_first_print = False
        #         continue
        #     # Frame이 생성되고 통신중이 아니라면
        #     g_i_x_Illuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x']    # 과거 조도 측정 값 저장
        #     g_i_Illuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']    # 현재 조도 측정 값 저장
        #     g_i_Illuminance_delta_signal = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta_signal']
        #     g_i_Illuminance_delta = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta']
        #     g_i_resualt = AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']  
        #     display_status()
        #     break
        # else:
        #     b_first_print = True
        #     while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:               # 만약 CIS Setting이 변경 되었다면
        #         if AlphaChip_Memory.g_b_Debugging and b_first_print:
        #             print("ISP : MODE : NEW FRAME : WAIT CHANGE CIS SETTING")
        #             b_first_print = False
        #         continue    
        #     b_first_print = True
        #     AlphaChip_Memory.g_b_FRAME_READY = False     # 새로운 Frame 완료
        #     while not AlphaChip_Memory.g_b_FRAME_READY or AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
        #         if AlphaChip_Memory.g_b_Debugging and b_first_print:
        #             print("ISP : MODE : NEW FRAME : WAIT FRAME_READY")
        #             b_first_print = False
        #         continue
        #     g_i_x_Illuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x']    # 과거 조도 측정 값 저장
        #     g_i_Illuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']    # 현재 조도 측정 값 저장
        #     g_i_Illuminance_delta_signal = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta_signal']
        #     g_i_Illuminance_delta = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta']
        #     g_i_resualt = AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']  
        #     display_status()
        #     if AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[0] == False and AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[1] == False:
        #         break

        b_first_print = True
        while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:               # 만약 CIS Setting이 변경 되었다면
            if AlphaChip_Memory.g_b_Debugging and b_first_print:
                print("ISP : MODE : NEW FRAME : WAIT CHANGE CIS SETTING")
                b_first_print = False
            continue    
        b_first_print = True
        AlphaChip_Memory.g_b_FRAME_READY = False     # 새로운 Frame 완료
        while not AlphaChip_Memory.g_b_FRAME_READY or AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
            if AlphaChip_Memory.g_b_Debugging and b_first_print:
                print("ISP : MODE : NEW FRAME : WAIT FRAME_READY")
                b_first_print = False
            continue
        g_i_x_Illuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x']    # 과거 조도 측정 값 저장
        g_i_Illuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']    # 현재 조도 측정 값 저장
        g_i_Illuminance_delta_signal = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta_signal']
        g_i_Illuminance_delta = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta']
        g_i_resualt = AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']  
        AlphaChip_ISP_Display.display_status()
        if (not b_resualt
            or (AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[0] == False and AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[1] == False)):
            break
            
def Mode():
    global g_i_time, g_i_x_Illuminance, g_i_Illuminance
    AlphaChip_Memory.g_b_FRAME_READY = False                         # 새로운 Frame 완료 ISP
    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['POWER_ON_MODE']
    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['POWER_ON_MODE']
    AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                        # CIS Setting이 변경 됨
    # AlphaChip_ISP_Active_Signal.GPIO.add_event_detect(AlphaChip_ISP_Active_Signal.g_i_Active_Input_PinNumber, AlphaChip_ISP_Active_Signal.GPIO.RISING, callback=Ext_Active_ON, bouncetime=300)      # Active Signal Input Interrupt
    # AlphaChip_ISP_Button.GPIO.add_event_detect(AlphaChip_ISP_Button.g_i_Ext_Button_PinNumber, AlphaChip_ISP_Button.GPIO.RISING, callback=Ext_Button, bouncetime=300)                               # EXT Button Input Interrup
    while True:
        ################ 반복 ####################################### 반복 ####################################### 반복 ####################################### 반복 ####################################### 반복 ####################################### 반복 ####################################### 반복 #######################
        if AlphaChip_Memory.g_b_Debugging:
            b_first_print = True
        while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:                                       # CIS Setting 중 이면
            if AlphaChip_Memory.g_b_Debugging and b_first_print:
                print("ISP : MODE : Wait CHANGE_CIS_SETTING")
                b_first_print = False   
            continue                                                                                                # 대기
        # # Master ######################################################################################################################################################################################
        # # SSL인 경우
        # if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1'] or AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:
        #     ### EXT Button Signal 인지
        #     if AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_ACTIVE_MODE'] == True:                                                             # Active Mode Signal이 들어온 경우
        #         AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['ACTIVE_MODE_1']                                  # ACTIVE_MODE_1로 전환
        #         # AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_ACTIVE_MODE'] = False
                
        #     ### EXT Active Mode Signal 인지
        #     elif AlphaChip_Memory.g_Ext_Botton_Push == True:                                                                                # 외부 버튼 Signal이 들어온 경우
        #         AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['ACTIVE_MODE_1']                                  # ACTIVE_MODE_1로 전환
        #         AlphaChip_Memory.g_Ext_Botton_Push = False                                                                                      # Active Mode Signal OFF
                
        ## POWER_ON_MODE ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        if AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['POWER_ON_MODE']:  
            if AlphaChip_Memory.g_b_Debugging:
                print()
                print("ISP : MODE : POWER_ON_MODE")   
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                           # CIS Setting이 변경 됨
            AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['Power_On_setting']                     # CPU 부팅 이유 표기
            WakeUp_System = threading.Thread(name="WakeUp_System", target=AlphaChip_Firmware.Boot_CPU, daemon=True)
            i_CPU_ON_x_time = g_i_time = time.time() ### Mode 진입 시간
            while True:
                ISP_New_Frame(False)
                g_i_time = time.time()
                if AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE']:
                    AlphaChip_ISP_Signal_Clear.clear_signal()
                    AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['non']                  # CPU가 종료됨을 뜻함
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : POWER_ON_MODE : CPU DONE CLEAR")
                    ### Stand by Mode 로 전환
                    while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                        continue
                    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']
                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']              # STAND BY MODE로 전환
                    if WakeUp_System.is_alive():
                        WakeUp_System._stop()
                    break
                elif not AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']:
                    if g_i_time - i_CPU_ON_x_time > (AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000) and WakeUp_System.is_alive():
                        if AlphaChip_Memory.g_b_Debugging:
                            print("ISP : MODE : POWER_ON_MODE : CPU ON TIME OVER : ", g_i_time - i_CPU_ON_x_time)
                        WakeUp_System._stop()
                        while WakeUp_System.is_alive():
                            continue
                        WakeUp_System.start()
                        if AlphaChip_Memory.g_b_Debugging:
                            print("ISP : MODE : WATCH_MODE : CPU Restart")
                        i_CPU_ON_x_time = time.time()
                    elif not WakeUp_System.is_alive():
                        WakeUp_System.start()
                        i_CPU_ON_x_time = time.time()

                
        ## STAND_BY_MODE ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        ## 여기서의 CIS Setting 값이 바뀌면 안됨 (조도의 기준값 RAW)
        elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['STAND_BY_MODE']:
            if AlphaChip_Memory.g_b_Debugging:
                print()
                print("ISP : MODE : STAND_BY_MODE")   
            ##### 모드 초기 세팅 #####
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                           # CIS Setting이 변경 됨
            
            # AlphaChip_Memory.g_INT_STS_REGISTER['LED_STS'] = 0                                                                          # LED 상태 non
            AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] = False                                                                  # Pseudo 상태 non
            while True:
                ISP_New_Frame(False)                                                                                                                  # 새로운 프레임
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : STAND_BY_MODE : illuminance : ", g_i_Illuminance)   
                    print("ISP : MODE : STAND_BY_MODE : Dark : ", AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_Illuminance_DARK_TH'])   
                if g_i_Illuminance < AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_Illuminance_DARK_TH']:                                  # 밤이면(AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['_Illuminance_DARK_TH'] 보다 높은 조도 계산값이라면)
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : STAND_BY_MODE : 밤")   
                    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_DAY_CHACK'] = False                                                              # 밤이라고 저장
                    while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                        continue
                    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['WATCH_MODE']
                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['WATCH_MODE']                                 # WATCH MODE로 전환
                    break
                else :     
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : STAND_BY_MODE : 낮")    
                    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_DAY_CHACK'] = True
                    time.sleep(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_ILLUMINANCE_CHECK_TIME'])           # 10초동안 대기
        
        ## WATCH_MODE ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        ## LOW CIS의 조절, 조도의 급격한 변화, 저조도 움직임을 파악
        elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['WATCH_MODE']:
            if AlphaChip_Memory.g_b_Debugging:
                print()
                print("ISP : MODE : WATCH_MODE")   
            ##### 모드 초기 세팅 ######
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                        # CIS Setting이 변경 됨            
            i_CPU_ON_x_time = i_Mode_in_x_time = g_i_time = time.time()                                                              # WATCH_MODE 진입 시간 측정            
            i_Occupancy_count = 0   # 재실 Count# 현재 시간
            while True:
                ISP_New_Frame(True)
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : WATCH_MODE : g_i_x_Illuminance : ", g_i_x_Illuminance)
                    print("ISP : MODE : WATCH_MODE : g_i_Illuminance : ", g_i_Illuminance)
                    print("ISP : MODE : WATCH_MODE : g_i_Illuminance_delta_signal : ", int(g_i_Illuminance_delta_signal))
                    print("ISP : MODE : WATCH_MODE : g_i_Illuminance_delta : ", g_i_Illuminance_delta)
                    if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1'] or AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:
                        print("ISP : MODE : WATCH_MODE : resualt : ", g_i_resualt)
                g_i_time = time.time() 

                ### 1. 외부 전등에 의해 급격하게 밝아졌는지 ########################################################################################                
                if g_i_Illuminance_delta_signal == False:
                    if g_i_resualt > AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MAX']:
                        if AlphaChip_Memory.g_TP1_REGISTER['_LOW_LIGHT_Delta_TH'] < g_i_Illuminance_delta:
                            if AlphaChip_Memory.g_b_Debugging:
                                print("ISP : MODE : WATCH_MODE : 점등 감지")
                            # AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_X_ILLUMINANCE'] = g_i_x_Illuminance
                            while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                                continue
                            ##### PiRA 1
                            if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['PIRA_1']:                                                                                 # PIRA_1 일 때
                                AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']
                                AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']                                                                                  # ACTIVE_MODE_1 전환
                            # ##### PiRA 2
                            # elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['PIRA_2']:                                                                               # PIRA_2 일 때
                            #     AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['DETECT_MODE']
                            #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['DETECT_MODE']                                                                                  # ACTIVE_MODE_2 전환
                            # ##### SSL-G 1  
                            # elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1']:                                                                                # SSL_1 일 때
                            #     AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['DETECT_MODE'] 
                            #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['DETECT_MODE']                                                                                   # ACTIVE_MODE_2 전환
                            # ##### SSL-G 2
                            # elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:                                                                                # SSL_2 일 때
                            #     AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['DETECT_MODE'] 
                            #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['DETECT_MODE']                                                                                  # ACTIVE_MODE_2 전환
                            else:
                                AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['DETECT_MODE']
                                AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['DETECT_MODE']
                            break
                #### SSL_G 에서만 동작
                if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1'] or AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:
                    #### 2. 저조도에서 움직임이 발생하였는지 ###############################################################################################################################################################################################################################
                    if (((AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['16x16']) and (g_i_resualt >= AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MIN'] and g_i_resualt < AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MAX']))
                        or ((AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['64x64']) and (g_i_resualt >= AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MIN'] and g_i_resualt < AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MAX']))):     # 픽셀이 변화하였는지(움직임 인지 구간)
                        if AlphaChip_Memory.g_b_Debugging:
                            print("ISP : MODE : WATCH_MODE : 저조도 움직임 Delta 감지")
                        while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                            continue   
                        AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE'] 
                        AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE']                                                                                                                                                       # LOW_RECHECK_MODE 전환
                        break
                    
                #### Watch Mode 유지 시간
                if int(g_i_time - i_Mode_in_x_time) > AlphaChip_Memory.g_N_TIMER_SET_REGISTER['_WATCH_MODE_TIME']:                                                                         # WATCH MODE가 AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['_WATCH_MODE_TIME']분 이상 지속 시
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : WATCH_MODE : WATCH_MODE_TIME : ", int(g_i_time - i_Mode_in_x_time))
                    while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                        continue
                    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE'] 
                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                                                                                  # STAND_BY_MODE 전환
                    break        

                if g_i_Illuminance < AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN'] or g_i_Illuminance > AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MAX']: # 조도 Range에 없으면   
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : WATCH_MODE : illuminance RANGE OUT")
                    # AlphaChip_ISP_Activation_Setting.Activation_Setting()

        ## LOW_RECHECK_MODE #################################################################################################################################################################################################################################################################################################################################################################################################################################
        ## 저조도에서의 움직임을 8Frame동안 다시 확인 - 저조도 노이즈로 인한 동작인지 판단
        elif AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] == AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE']:
            if AlphaChip_Memory.g_b_Debugging:
                print()
                print("ISP : MODE : LOW_RECHECK_MODE")   
            ##### 모드 초기 세팅 ######
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                              # CIS Setting이 변경 됨
            
            ### SSL-G 1
            if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1']:
                # AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']번의 Frame동안 차영상 연산 실시 - 결과 값을 Buffer 에다가 저장 - 연속 3번 재실이면 ByPass - 아니라면 8번 연산 후 AlphaChip_Memory.g_N_RECHECK_SETTING['_OCCUPANCY_ACKNOWIEDGMENT_COUNT'] 이상이면 재실임을 반환
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : LOW_RECHECK_MODE : Recheck Start")   
                b_occupancy = AlphaChip_ISP_Recheck.Recheck_Process(True)
                while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                    continue   
                if b_occupancy == True:                                                                                                     # 재실이라면
                    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['LED_ON'] 
                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['LED_ON']             # LED_ON 전환
                                     
                else :                                                                                                                      # 재실이 아니라면
                    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE'] 
                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                              # STAND_BY_MODE 전환

            # ### SSL-G 2
            # elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:
            #     continue

        ## LED_ON #######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        elif AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] == AlphaChip_Memory.g_N_mode['LED_ON']:
            if AlphaChip_Memory.g_b_Debugging:
                print()
                print("ISP : MODE : LED_ON")   
            ##### 모드 초기 세팅 ######
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                    # CIS Setting이 변경 됨
            ### SSL-G 1
            if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1']:
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : LED_ON : LED 점진적 ON")   
                AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] = True # LED 상태 ON(점진적)             
                for led_level in range(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'], 6, 1):                                                        # 현재 LED LEVEL 부터 끝까지 점진적 점등
                    AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])      # 현재 LED LEVEL로 LED PWM 출력
                    AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level                                                                           # 현재 LED LEVEL을 저장
                    time.sleep(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['_DIM_WAIT_TIME']/1000)                                                        # 대기
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : LED_ON : Recheck_Process Start")  
                b_occupancy = AlphaChip_ISP_Recheck.Recheck_Process(True) 
                while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                    continue
                if b_occupancy == True:                                                                                                                 # 재실이라면
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : LED_ON : 재실")  
                        print("ISP : MODE : LED_ON : _LOW_RECHECK_ERROR_COUNT 0로 설정")  
                    AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT'] = 0                                                                    # Error Count를 초기화
                    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['ACTIVE_MODE'] 
                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']                              # STAND_BY_MODE 전환
                else :                                                                                                                                  # 재실이 아니라면
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : LED_ON : 재실이 아님")  
                        print("ISP : MODE : LED_ON : LED 즉시 소등")  
                    AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = 0
                    AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] )                              # LED 소등(즉각적)
                    AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] = False  # LED 상태 OFF
                    AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT'] += 1                                                                   # 저조도 ERROR 카운트 증가
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : MODE : LED_ON : _LOW_RECHECK_ERROR_COUNT : ", AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT'])  
                    if AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT'] > AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_MAX']:   # 만약 ERROR 카운트가 연속적으로 AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_LOW_RECHECK_ERROR_MAX']번 발생 하였다면
                        if AlphaChip_Memory.g_b_Debugging:
                            print("ISP : MODE : LED_ON : LOW_TP1_MIN 증가")                                                                                                               # TP1 MIN 증가
                            print("ISP : MODE : LED_ON : LOW_TP1_MIN 증가 기능 만들어야함")                                                                                                               # TP1 MIN 증가  
                    AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE'] 
                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                              # STAND_BY_MODE 전환
                    
            # ### SSL-G 2
            # elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:
            #     continue
            else:
                print("Target = Mode 해당 아님")

        ## ACTIVE_MODE ##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        elif AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] == AlphaChip_Memory.g_N_mode['ACTIVE_MODE']:
            if AlphaChip_Memory.g_b_Debugging:
                print()
                print("ISP : MODE : ACTIVE_MODE")   
            ##### 모드 초기 세팅 ######
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                           # CIS Setting이 변경 됨
                
            i_Occupancy_count = 0
            i_Mode_in_x_time = g_i_time = i_Pseudo_Signal_x_time = i_LED_on_x_time = time.time()                                        # Mode 진입 시간 및 Pseudo Signal 마지막 출력 시간 설정
            
            AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] = True              # LED 상태 ON
            for led_level in range(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'], 6, 1):
                AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                time.sleep(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['_DIM_WAIT_TIME']/1000)
                if AlphaChip_Memory.g_b_Debugging:
                    Tkinter_Display_Start.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
                    print("ISP : MODE : ACTIVE_MODE : 출력 초기화")
                    
            while True:
                if AlphaChip_ISP.g_i_Mode != AlphaChip_Memory.g_N_mode['ACTIVE_MODE']:
                    break
                ISP_New_Frame(True)
                g_i_time = time.time()                                                                          # 현재 시간 파악
                ### PiRA 1
                if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['PIRA_1']:
                    if AlphaChip_Memory.g_b_Debugging:
                        Tkinter_Display_Start.Pseudo_State_text_handle.configure(text = 'OFF', bg = 'gray')
                        print("ISP : MODE : ACTIVE_MODE : g_i_x_Illuminance : ", g_i_x_Illuminance)
                        print("ISP : MODE : ACTIVE_MODE : g_i_Illuminance : ", g_i_Illuminance)
                        print("ISP : MODE : ACTIVE_MODE : Result_data : ", g_i_resualt)
                    if g_i_Illuminance_delta_signal == True:
                        if g_i_resualt > AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']:
                            if AlphaChip_Memory.g_TP1_REGISTER['_HIGH_LIGHT_Delta_TH'] < g_i_Illuminance_delta:
                                if AlphaChip_Memory.g_b_Debugging:
                                    print("ISP : MODE : ACTIVE_MODE : 소등")
                                b_Occupancy = AlphaChip_ISP_Recheck.Recheck_Process(False)
                                if b_Occupancy:  # 재실 중 PIR 센서등이 소등했다고 판단하여 Pseudo Signal의 Setting을 수정한다.
                                    while True:
                                        if AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH'] >= 500 and AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'] == 2:  # Pseudo Signal 출력 주기가 최대값인 경우
                                            break                                                                                                                               # Setting 종료
                                        elif AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'] == 2:                                                                  # Pseudo Signal 연속 2회 출력일 경우
                                            AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH'] += 50                                                                        # 출력 폭을 50ms 증가 후
                                            AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'] = 1                                                                         # 출력 횟수 1회로 감소
                                        else :                                                                                                                              # 이외
                                            AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'] += 1                                                                        # 출력 횟수 1회 증가
                                        
                                        if AlphaChip_Memory.g_b_Debugging:
                                            Tkinter_Display_Start.insert_Pseudo_Signal_Count_text.delete(0,10)
                                            Tkinter_Display_Start.insert_Pseudo_Signal_Count_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT']))
                                            Tkinter_Display_Start.insert_Pseudo_Signal_Width_text.delete(0,10)
                                            Tkinter_Display_Start.insert_Pseudo_Signal_Width_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH']))
                                            Tkinter_Display_Start.insert_Pseudo_Signal_Cycle_text.delete(0,10)
                                            Tkinter_Display_Start.insert_Pseudo_Signal_Cycle_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH']))
                                        
                                        # 수정된 Pseudo Signal 출력
                                        for i in range(0, AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'], 1):                                                      # 저장된 Pseudo Signal 출력 횟수 만큼 반복
                                            AlphaChip_Memory.g_INT_STS_REGISTER['_Pseudo_STS'] = True                                                                           # Pseudo Signal 출력 표시
                                            if AlphaChip_Memory.g_b_Debugging:
                                                Tkinter_Display_Start.Pseudo_State_text_handle.configure(text = 'ON', bg = 'yellow')
                                            AlphaChip_ISP_Pseudo.GPIO.output(AlphaChip_ISP_Pseudo.g_i_Pseudo_0_OUT_PinNumber, True)                         
                                            AlphaChip_ISP_Pseudo.time.sleep(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH'] / 1000)                                      # Pseudo Signal 출력 폭
                                            AlphaChip_ISP_Pseudo.GPIO.output(AlphaChip_ISP_Pseudo.g_i_Pseudo_0_OUT_PinNumber, False)
                                            AlphaChip_Memory.g_INT_STS_REGISTER['_Pseudo_STS'] = False
                                            if AlphaChip_Memory.g_b_Debugging:
                                                Tkinter_Display_Start.Pseudo_State_text_handle.configure(text = 'Non', bg = 'gray')
                                        i_Pseudo_Signal_x_time = time.time()                                                                                                # 마지막 Pseudo Signal 출력 시간 저장
                                        ISP_New_Frame(True)                                                                                                                          # 새로운 Frame 확인하여 점등 하였는지 확인
                                        if g_i_Illuminance_delta_signal == False:
                                            if g_i_resualt > AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']:
                                                if AlphaChip_Memory.g_TP1_REGISTER['_HIGH_LIGHT_Delta_TH'] < g_i_Illuminance_delta:
                                                    break
                                else:                                                                                                                               # 재실이 아니라면
                                    AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                                      # STAND BY MODE로 전환
                                    break
                              
                    elif (g_i_resualt >= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN']) and (g_i_resualt < AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']): # 픽셀이 변화하였는지(움직임 인지 구간)
                        if g_i_time - i_Pseudo_Signal_x_time >= ((2000 - AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH']) / 100):                # 마지막 Pseudo Signal 출력 신호가 2000 - AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH'] s만큼 흘렀다면(Pseudo Signal 출력 주기)
                            for i in range(0, AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'], 1):                                                  # AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'] 횟수 만큼 Pseudo Signal 출력                      
                                AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] = True                                                                       # Pseudo Signal ON
                                if AlphaChip_Memory.g_b_Debugging:
                                    Tkinter_Display_Start.Pseudo_State_text_handle.configure(text = 'ON', bg = 'yellow')
                                AlphaChip_ISP_Pseudo.GPIO.output(AlphaChip_ISP_Pseudo.g_i_Pseudo_0_OUT_PinNumber,  AlphaChip_Memory.g_INT_STS_REGISTER['_Pseudo_STS'])
                                AlphaChip_ISP_Pseudo.time.sleep(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH'] / 1000)                                  # Pseudo Signal 폭
                                AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] = False                                                                      # Pseudo Signal OFF
                                if AlphaChip_Memory.g_b_Debugging:
                                    Tkinter_Display_Start.Pseudo_State_text_handle.configure(text = 'OFF', bg = 'gray')   
                                AlphaChip_ISP_Pseudo.GPIO.output(AlphaChip_ISP_Pseudo.g_i_Pseudo_0_OUT_PinNumber, AlphaChip_Memory.g_INT_STS_REGISTER['_Pseudo_STS'])
                            i_Pseudo_Signal_x_time = time.time() ####### 마지막 Pseudo Signal 출력 시간 저장           
       
                ### PiRA 2 / SSL_G_1
                else:
                    # if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['PIRA_2'] and g_i_resualt > AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_64_TP2_MAX']:                           # PiRA 2 만 외부 전등에 의해 LED 동작함
                    #     if AlphaChip_Memory.g_b_Debugging:
                    #         print("ISP : MODE : ACTIVE_MODE_1 : g_i_x_liiuminance : ", g_i_x_liiuminance)
                    #         print("ISP : MODE : ACTIVE_MODE_1 : g_i_liiuminance : ", g_i_liiuminance)
                    #     if g_i_x_liiuminance > g_i_liiuminance:                                                                                                                                                         # 밝기가 어두워 졌는지 확인
                    #         if AlphaChip_Memory.g_b_Debugging:
                    #             print("ISP : MODE : ACTIVE_MODE_1 : Alpha Chip LED 소등")
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['LED_STS'] = 1 # LED 상태 ON
                    #         for led_level in range(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'], 6, 1):                                                    
                    #             AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #             time.sleep(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME']/1000)
                    #             AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    #             if AlphaChip_Memory.g_b_Debugging:
                    #                 display.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
                    #     elif g_i_x_liiuminance < g_i_liiuminance:                                                                                                                                                       # 밝기가 밝아 졌는지 확인
                    #         if AlphaChip_Memory.g_b_Debugging:
                    #             print("ISP : MODE : ACTIVE_MODE_1 : Alpha Chip LED 점등")
                    #         for led_level in range(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'], -1, -1):
                    #             AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #             time.sleep(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME']/1000)
                    #             AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    #             if AlphaChip_Memory.g_b_Debugging:
                    #                 display.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['LED_STS'] = 2 # LED 상태 OFF
                    
                    if g_i_resualt >= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN'] and g_i_resualt <= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']:                                                   # 픽셀이 변화하였는지(움직임 인지 구간)
                        i_LED_on_x_time = time.time()                                                                                                                                                                   # 마지막 움직임 시간을 현재 시간으로 설정
                        if AlphaChip_Memory.g_b_Debugging:
                            print("ISP : MODE : ACTIVE_MODE : Result_data : ", g_i_resualt)
                            print("ISP : MODE : ACTIVE_MODE : 움직임")

                    elif g_i_time - i_LED_on_x_time > AlphaChip_Memory.g_N_TIMER_SET_REGISTER['_LED_ON_TIME'] :                                                                                               # 마지막 움직임까지 AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_LED_ON_TIME']초 이상 흘렀다면
                        while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                            continue   
                        AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['RECHECK_MODE'] 
                        AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['RECHECK_MODE']                              # STAND_BY_MODE 전환                                                                                          # RECHECK_MODE로 전환
                        if AlphaChip_Memory.g_b_Debugging:
                            print("ISP : MODE : ACTIVE_MODE : Recheck 전환")
                        break

                    if g_i_time - i_Mode_in_x_time > AlphaChip_Memory.g_N_TIMER_SET_REGISTER['_MODE_TIME'] :                                                                                        # Mode 진입한지 AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['_ACTIVE_2_MODE_TIME']분 지났다면
                        if AlphaChip_Memory.g_b_Debugging:
                            print("ISP : MODE : ACTIVE_MODE : Mode 시간 초과")
                            print("ISP : MODE : ACTIVE_MODE : LED 깜빡임")
                        i_Dimming_count = 0
                        b_Dimming_UP = False
                        i_Dimming_time = i_Dimming_x_time = time.time()
                        led_level = AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']
                        while True: # LED 깜빡임 5회 진행(5분 동안)
                            i_Dimming_time = time.time()
                            if i_Dimming_time - i_Dimming_x_time >= 1:
                                if b_Dimming_UP:
                                    led_level = 0
                                elif not b_Dimming_UP:
                                    led_level = 5
                                AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                                AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                                i_Dimming_x_time = time.time()
                                b_Dimming_UP = not b_Dimming_UP
                                i_Dimming_count += 1
                                if AlphaChip_Memory.g_b_Debugging:
                                    Tkinter_Display_Start.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
                                    print("ISP : MODE : ACTIVE_MODE_1 : i_Dimming_count : ", i_Dimming_count)
                            
                            ISP_New_Frame(True)
                            if AlphaChip_Memory.g_b_Debugging:
                                print("ISP : MODE : ACTIVE_MODE_1 : Mode 시간 초과 : Result_data : ", g_i_resualt)
                            if g_i_resualt >= AlphaChip_Memory.g_N_RECHECK_SETTING['g_i_big_move_TP2'] or AlphaChip_Memory.g_Ext_Botton_Push == True:
                                if AlphaChip_Memory.g_b_Debugging:
                                    if g_i_resualt >= AlphaChip_Memory.g_N_RECHECK_SETTING['g_i_big_move_TP2']:
                                        print("ISP : MODE : ACTIVE_MODE_1 : Mode 시간 초과 : 큰 움직임")
                                    elif AlphaChip_Memory.g_Ext_Botton_Push == True :                                             # 외부 버튼이 눌리면   
                                        print("ISP : MODE : ACTIVE_MODE_1 : Active Mode 시간 초과 : Button 누름")      
                                led_level = 5
                                AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                                AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                                i_Mode_in_x_time = time.time()
                                break
     
                            elif i_Dimming_count >= AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['_FLIKER_COUNT']:                                                                  # 외부 버튼이 눌리지 않았다면 (사람이 없었음)
                                if AlphaChip_Memory.g_b_Debugging:
                                    print("ISP : MODE : ACTIVE_MODE_1 : Active Mode 시간 초과 : Button 안누름")
                                    print("ISP : MODE : ACTIVE_MODE_1 : Active Mode 시간 초과 : Button 안누름 : TP 조절")
                                
                                if AlphaChip_Memory.g_b_Debugging:
                                    print("ISP : Activation_Setting : TP2 Setting CPU ON")
                                AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['_TP_Setting']
                                WakeUp_System = threading.Thread(name="TP_Setting", target=AlphaChip_Firmware.Boot_CPU, daemon=True)
                                i_CPU_ON_x_time = g_i_time = time.time() ### Mode 진입 시간
                                while True:
                                    g_i_time = time.time()
                                    if AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE']:
                                        AlphaChip_ISP_Signal_Clear.clear_signal()
                                        AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['non']                  # CPU가 종료됨을 뜻함
                                        if AlphaChip_Memory.g_b_Debugging:
                                            print("ISP : Activation_Setting : TP2 Setting : CPU DONE CLEAR")
                                        break
                                    elif not AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']:
                                        if g_i_time - i_CPU_ON_x_time > (AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000) and WakeUp_System.is_alive():
                                            if AlphaChip_Memory.g_b_Debugging:
                                                print("ISP : Activation_Setting : TP2 Setting : CPU ON TIME OVER : ", g_i_time - i_CPU_ON_x_time)
                                            WakeUp_System._stop()
                                            while WakeUp_System.is_alive():
                                                continue
                                            WakeUp_System.start()
                                            if AlphaChip_Memory.g_b_Debugging:
                                                print("ISP : Activation_Setting : TP2 Setting : CPU Restart")
                                            i_CPU_ON_x_time = time.time()
                                            time.sleep(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000)
                                        elif not WakeUp_System.is_alive():
                                            WakeUp_System.start()
                                            i_CPU_ON_x_time = time.time()
                                            time.sleep(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000)
 
                                led_level = 0
                                AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                                AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                                while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                                    continue   
                                AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE'] 
                                AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                              # STAND_BY_MODE 전환
                                break

                
        ## DETECT_MODE ###################################################################################################
        elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['DETECT_MODE']:
            if AlphaChip_Memory.g_b_Debugging:
                print()
                print("ISP : MODE : DETECT_MODE")   
            ##### 모드 초기 세팅 ######
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                           # CIS Setting이 변경 됨
            
            ISP_New_Frame(False)
            i_Mode_in_x_time = g_i_time = i_on_occupancey_x_time = time.time()                                                                                   # Mode 진입 시간 및 Pseudo Signal 마지막 출력 시간 설정
            i_Occupancy_count = 0   # 재실 Count
            i_start_illuminance = g_i_Illuminance
            #############################
            while True:
                ISP_New_Frame(True)
                if AlphaChip_Memory.g_b_Debugging:
                    print()
                    print("ISP : MODE : DETECT_MODE : g_i_time : ", g_i_time)
                    print("ISP : MODE : DETECT_MODE : i_Mode_in_x_time : ", i_Mode_in_x_time)
                    print("ISP : MODE : DETECT_MODE : i_start_illuminance : ", i_start_illuminance)
                    print("ISP : MODE : DETECT_MODE : g_i_x_Illuminance : ", g_i_x_Illuminance)
                    print("ISP : MODE : DETECT_MODE : g_i_Illuminance : ", g_i_Illuminance)
                    print("ISP : MODE : DETECT_MODE : g_i_Illuminance_delta_signal : ", int(g_i_Illuminance_delta_signal))
                    print("ISP : MODE : DETECT_MODE : g_i_Illuminance_delta : ", g_i_Illuminance_delta)
                            
                    print("AlphaChip_Memory.g_b_A_Illuminance_buffer : ", AlphaChip_Memory.g_b_A_Illuminance_buffer)
                    print("AlphaChip_Memory.g_i_Illuminance_Buffer_delta : ", AlphaChip_Memory.g_i_Illuminance_Buffer_delta)
                    print("AlphaChip_Memory.g_i_Illuminance_Buffer_avg : ", AlphaChip_Memory.g_i_Illuminance_Buffer_avg)
                    print("ISP : MODE : DETECT_MODE : g_i_resualt : ", g_i_resualt)
                    print()
                    # print("ISP : MODE : DETECT_MODE : AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_X_ILLUMINANCE'] : ", AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_X_ILLUMINANCE'])
                g_i_time = time.time()     
                # ### PiRA 2 / SSL_G_1
                if g_i_Illuminance_delta_signal == True:
                    if g_i_resualt > AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']:
                        if AlphaChip_Memory.g_TP1_REGISTER['_HIGH_LIGHT_Delta_TH'] < g_i_Illuminance_delta:
                            if AlphaChip_Memory.g_b_Debugging:
                                print("ISP : MODE : DETECT_MODE : 소등 감지")
                            b_Occupancy = AlphaChip_ISP_Recheck.Recheck_Process(False)
                            while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                                continue
                            if b_Occupancy:
                                AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']
                                AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']                                                      # ACTIVE_MODE 로 전환 
                            else:                                                                                                                                               # 재실 횟수가 적다면
                                # AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT'] += 1                                                                             # 저조도 Error Count 증가
                                AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']
                                AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                                                      # STAND_BY_MODE 전환 
                            break
                        
                # if (g_i_resualt >= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN']) and (g_i_resualt < AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']):  # 픽셀이 변화하였는지(움직임 인지 구간)
                #         i_on_occupancey_x_time = time.time()                                                                                                                      # 마지막 움직임의 시간을 현재 시간으로 설정
                
                elif g_i_time - i_Mode_in_x_time > AlphaChip_Memory.g_N_TIMER_SET_REGISTER['_MODE_TIME']:                                                             # 마지막 움직임 시간이 AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['_ACTIVE_2_MODE_TIME'] 이상이라면
                    b_Occupancy = AlphaChip_ISP_Recheck.Recheck_Process(False)
                    while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                        continue
                    if b_Occupancy:
                        AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']
                        AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']                                                      # ACTIVE_MODE 로 전환 
                    else:                                                                                                                                               # 재실 횟수가 적다면
                        # AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT'] += 1                                                                             # 저조도 Error Count 증가
                        AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']
                        AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                                                      # STAND_BY_MODE 전환 
                    break
                    
                    
                    
                    
                    
                    
                    # if AlphaChip_Memory.g_b_Debugging:
                    #     print("ISP : MODE : DETECT_MODE : Mode 시간 초과")

                    #     print("i_start_illuminance : ", i_start_illuminance)
                    #     print("g_i_Illuminance : ", g_i_Illuminance)
                    #     print("AlphaChip_Memory.g_i_Illuminance_Buffer_avg : ", AlphaChip_Memory.g_i_Illuminance_Buffer_avg)
                    #     print("AlphaChip_Memory.g_i_Illuminance_Buffer_delta : ", AlphaChip_Memory.g_i_Illuminance_Buffer_delta)
                    # if i_start_illuminance - AlphaChip_Memory.g_TP1_REGISTER['_HIGH_LIGHT_Delta_TH'] > AlphaChip_Memory.g_i_Illuminance_Buffer_avg:
                    #     if AlphaChip_Memory.g_i_Illuminance_Buffer_delta < 3:
                    #         # 소등한 상황 (소등을 인지 못함)
                    #         while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                    #             continue
                    #         AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE'] 
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']
                    #         led_level = 0
                    #         AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    #         break
                    
                    # if AlphaChip_Memory.g_b_Debugging:
                    #     print("ISP : MODE : DETECT_MODE : Mode 시간 초과 : LED 깜빡임")
                    # i_Dimming_count = 0
                    # b_Dimming_UP = False
                    # i_Dimming_time = i_Dimming_x_time = time.time()
                    # led_level = AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']
                    # while True: # LED 깜빡임 5회 진행(5초 동안)
                    #     i_Dimming_time = time.time()
                    #     if i_Dimming_time - i_Dimming_x_time >= AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['_FLIKER_SPEED']:
                    #         if b_Dimming_UP:
                    #             led_level = 0
                    #         elif not b_Dimming_UP:
                    #             led_level = 5
                    #         AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #         # time.sleep(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME']/1000)                                                        # 대기
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    #         i_Dimming_x_time = time.time()
                    #         b_Dimming_UP = not b_Dimming_UP
                    #         i_Dimming_count += 1
                    #         if AlphaChip_Memory.g_b_Debugging:
                    #             display.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
                    #             print("ISP : MODE : DETECT_MODE : Mode 시간 초과 : 깜빡임 횟수 : ", i_Dimming_count)
                        
                    #     ISP_New_Frame(True)
                        
                    #     if AlphaChip_Memory.g_b_Debugging:
                    #         print("ISP : MODE : DETECT_MODE : Mode 시간 초과 : Result_data : ", g_i_resualt)
                    #     if g_i_resualt >= AlphaChip_Memory.g_N_RECHECK_SETTING['g_i_big_move_TP2'] :
                    #         if AlphaChip_Memory.g_b_Debugging:
                    #             print("ISP : MODE : DETECT_MODE : Mode 시간 초과 : 큰 움직임")
                    #         led_level = 5
                    #         AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #         # time.sleep(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME']/1000)                                                        # 대기
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    #         i_Mode_in_x_time = time.time()
                    #         break
                        
                    #     elif AlphaChip_Memory.g_Ext_Botton_Push == True :                                             # 외부 버튼이 눌리면   
                    #         if AlphaChip_Memory.g_b_Debugging:
                    #             print("ISP : MODE : DETECT_MODE : Mode 시간 초과 : Button 누름")
                    #         led_level = 5
                    #         AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #         # time.sleep(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME']/1000)                                                        # 대기
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    #         i_Mode_in_x_time = time.time()
                    #         break
                        
                    #     elif i_Dimming_count >= AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['_FLIKER_COUNT']:                                                                  # 외부 버튼이 눌리지 않았다면 (사람이 없었음)
                    #         if AlphaChip_Memory.g_b_Debugging:
                    #             print("ISP : MODE : DETECT_MODE : Mode 시간 초과 : Button 안누름")
                    #             # print("ISP : MODE : DETECT_MODE : Mode 시간 초과 : Button 안누름 : TP 조절")
                    #         led_level = 100
                    #         AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                            
                    #         if AlphaChip_Memory.g_b_Debugging:
                    #             print("ISP : Activation_Setting : TP2 Setting CPU ON")
                    #         # AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['_TP_Setting']
                    #         # WakeUp_System = threading.Thread(name="TP_Setting", target=AlphaChip_Firmware.Boot_CPU, daemon=True)
                    #         # i_CPU_ON_x_time = g_i_time = time.time() ### Mode 진입 시간
                    #         # while True:
                    #         #     g_i_time = time.time()
                    #         #     if AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE']:
                    #         #         AlphaChip_ISP_Signal_Clear.clear_signal()
                    #         #         AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['non']                  # CPU가 종료됨을 뜻함
                    #         #         if AlphaChip_Memory.g_b_Debugging:
                    #         #             print("ISP : Activation_Setting : TP2 Setting : CPU DONE CLEAR")
                    #         #         break
                    #         #     elif not AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']:
                    #         #         if g_i_time - i_CPU_ON_x_time > (AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000) and WakeUp_System.is_alive():
                    #         #             if AlphaChip_Memory.g_b_Debugging:
                    #         #                 print("ISP : Activation_Setting : TP2 Setting : CPU ON TIME OVER : ", g_i_time - i_CPU_ON_x_time)
                    #         #             WakeUp_System._stop()
                    #         #             while WakeUp_System.is_alive():
                    #         #                 continue
                    #         #             WakeUp_System.start()
                    #         #             if AlphaChip_Memory.g_b_Debugging:
                    #         #                 print("ISP : Activation_Setting : TP2 Setting : CPU Restart")
                    #         #             i_CPU_ON_x_time = time.time()
                    #         #             time.sleep(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000)
                    #         #         elif not WakeUp_System.is_alive():
                    #         #             WakeUp_System.start()
                    #         #             i_CPU_ON_x_time = time.time()
                    #         #             time.sleep(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000)

                    #         while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                    #             continue
                    #         AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE'] 
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']
                    #         led_level = 0
                    #         AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                    #         AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    #         break
                        

        ## RECHECK_MODE ###################################################################################################
        elif AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] == AlphaChip_Memory.g_N_mode['RECHECK_MODE']:
            ##### 모드 초기 세팅 ######
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                          # CIS Setting이 변경 됨
            ### PiRA 2 / SSL_G_1
            #if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['PIRA_2'] or AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1']:
            if AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] == True:                                                                                     # LED가 ON 이라면
                led_level = AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] - 1                                                                           # LED 1단계 Dimming
                AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level        
                if AlphaChip_Memory.g_b_Debugging:
                    Tkinter_Display_Start.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))    
            else:                                                                                                                                       # LED 가 OFF 라면
                AlphaChip_Memory.g_INT_STS_REGISTER['LED_STS'] = True                                                                                          # LED ON 설정
                led_level = 4                                                                                                                               # LED Level 4 로 설정
                AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                if AlphaChip_Memory.g_b_Debugging:
                    Tkinter_Display_Start.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))           
            
            b_occupancy = AlphaChip_ISP_Recheck.Recheck_Process(True)                                                                                       # Recheck 실행
            if b_occupancy == True:                                                                                                                     # 재실이라면
                ### 밝은 환경에서 움직임을 파악하지 못해서 Recheck Mode로 진입한것이기 때문에 TP를 감소시켜야 하는 상황
                AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_COUNT'] += 1                                                                           # High Error 증가
                if AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_COUNT'] > AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_MAX']:                   # ERROR 카운트가 연속적으로 AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_RECHECK_ERROR_MAX']번 발생 하였다면
                    if AlphaChip_Memory.g_b_Debugging:
                        print("HIGH_64_TP2_MIN 감소")
                        print("HIGH_64_TP2_MIN 감소 기능 만들어야함")

                while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                    continue
                AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']
                AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['ACTIVE_MODE']                                              # ACTIVE_MODE_1 전환
            else :                                                                                                                                      # 재실이 아니라면
                AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['_RECHECK_ERROR_COUNT'] = 0                                                                   # Error Count를 초기화
                for led_level in range(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'], -1, -1):                                                          # LED 소등(점진적)
                    AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_'+str(led_level)])
                    AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL'] = led_level
                    time.sleep(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['_DIM_WAIT_TIME']/1000)
                    if AlphaChip_Memory.g_b_Debugging:
                        Tkinter_Display_Start.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))    
                AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] = False # LED OFF

                while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                    continue
                AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']
                AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']                                              # STAND BY MODE로 전환                           
                
            ### SSL-G 2
            #elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:
                #continue
            