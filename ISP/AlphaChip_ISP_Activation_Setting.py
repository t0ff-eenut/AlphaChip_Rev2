import AlphaChip_Memory
from ISP import AlphaChip_ISP_Mode, AlphaChip_ISP_Signal_Clear
from CPU import AlphaChip_Firmware
import time, threading

def INTTime_set(b_vector):
    if AlphaChip_Memory.g_b_Debugging:
        print("ISP : Activation_Setting : INTTime Setting")        
    i_cis_setting = AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING']
    if i_cis_setting == AlphaChip_Memory.g_CIS_MODE['LOW']:
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : Activation_Setting : INTTime Setting : LOW INTTIME SETTING")
        i_gain = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_AMP_GAIN']    
        i_inttime = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']
        i_inttime_UD = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL']
        i_inttime_range_min = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MIN']
        i_inttime_range_max = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MAX']
    elif i_cis_setting == AlphaChip_Memory.g_CIS_MODE['HIGH']:
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : Activation_Setting : INTTime Setting : HIGH INTTIME SETTING")
        i_gain = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']
        i_inttime_UD = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL']
        i_inttime_range_min = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MIN']
        i_inttime_range_max = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MAX']
        
    if (b_vector == False and ((i_inttime - i_inttime_UD) < i_inttime_range_min)) or (b_vector == True and ((i_inttime + i_inttime_UD) > i_inttime_range_max)):
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : Activation_Setting : INTTime Setting : INTTIME RANGE OVER")
        if (b_vector == False and i_gain == 1) or (b_vector == True and i_gain == 22):
            if AlphaChip_Memory.g_b_Debugging:
                print("CPU : Firmware : INTTime Setting : INTTIME RANGE OVER : GAIN RANGE OVER")
            return -1
        else:
            #### CPU ON
            if i_cis_setting == AlphaChip_Memory.g_CIS_MODE['LOW']:
                AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['_Low_Gain_setting']                     # CPU 부팅 이유 표기
            elif i_cis_setting == AlphaChip_Memory.g_CIS_MODE['HIGH']:
                AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['_High_Gain_setting']                     # CPU 부팅 이유 표기

        WakeUp_System_Gain_Setting = threading.Thread(name="Gain_Setting", target=AlphaChip_Firmware.Boot_CPU, daemon=True)
        i_CPU_ON_x_time = g_i_time = time.time() ### Mode 진입 시간
        while True:
            g_i_time = time.time()
            if AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE']:
                AlphaChip_ISP_Signal_Clear.clear_signal()
                AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['non']                  # CPU가 종료됨을 뜻함
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : INTTime Setting : CPU DONE CLEAR")
                if WakeUp_System_Gain_Setting.is_alive():
                    WakeUp_System_Gain_Setting._stop()
                break
            elif not AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']:
                if g_i_time - i_CPU_ON_x_time > (AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000) and WakeUp_System_Gain_Setting.is_alive():
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : Activation_Setting : INTTime Setting : CPU ON TIME OVER : ", g_i_time - i_CPU_ON_x_time)
                    WakeUp_System_Gain_Setting._stop()
                    while WakeUp_System_Gain_Setting.is_alive():
                        continue
                    WakeUp_System_Gain_Setting.start()
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : Activation_Setting : INTTime Setting : CPU Restart")
                    i_CPU_ON_x_time = time.time()
                    time.sleep(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000)
                elif not WakeUp_System_Gain_Setting.is_alive():
                    WakeUp_System_Gain_Setting.start()
                    i_CPU_ON_x_time = time.time()
                    time.sleep(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000)
    else :
        if b_vector == False:
            if AlphaChip_Memory.g_b_Debugging:
                print("ISP : Activation_Setting : INTTime Setting : INTTIME DOWN")
            i_inttime -= i_inttime_UD
        elif b_vector == True:
            if AlphaChip_Memory.g_b_Debugging:
                print("ISP : Activation_Setting : INTTime Setting : INTTIME UP")
            i_inttime += i_inttime_UD
            
        if i_cis_setting == AlphaChip_Memory.g_CIS_MODE['LOW']:
            AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME'] = i_inttime
        elif i_cis_setting == AlphaChip_Memory.g_CIS_MODE['HIGH']:
            AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME'] = i_inttime
    AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True      


def Activation_Setting():
    if AlphaChip_Memory.g_b_Debugging:
        print()
        print("ISP : Activation_Setting") 
    i_illuminance_target =  AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN'] + int((AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MAX'] - AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN']) / 2)         
    i_CIS_Settitng_Vector = 0               # 1 : 상승, 2 : 하강
    i_x_illuminance_ov = 0
    i_illuminance_ov = 0

    while True:
        if AlphaChip_ISP_Mode.g_i_Illuminance < i_illuminance_target:                                                          # 조도가 낮으면
            if AlphaChip_Memory.g_b_Debugging:
                print("ISP : Activation_Setting : 조도가 낮음")
            if i_CIS_Settitng_Vector != 2:                                                                      # CIS 조절 방향이 하강이 아니라면
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : INTTIME 상승")
                i_x_illuminance_ov = i_illuminance_target - AlphaChip_ISP_Mode.g_i_Illuminance
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : 마지막 Target 조도와의 차이 : ", i_x_illuminance_ov)
                i_CIS_Settitng_Vector = 1                                                                           # 상승 방향 설정
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : INTTIME 조절 시작")
                INTTime_set(True)                                                                                   # 상승 방향으로 INTTIME SETTING
            else:
                i_illuminance_ov = i_illuminance_target - AlphaChip_ISP_Mode.g_i_Illuminance
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : 마지막 Target 조도와의 차이 : ", i_x_illuminance_ov)
                    print("ISP : Activation_Setting : 현재 Target 조도와의 차이 : ", i_illuminance_ov)
                if i_x_illuminance_ov < i_illuminance_ov:
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : Activation_Setting : 직전 CIS Setting 값으로 복원")
                    INTTime_set(False)  
                break
            
        elif AlphaChip_ISP_Mode.g_i_Illuminance > i_illuminance_target:       # 조도가 높고 CIS 조절 방향이 상승이 아니라면
            if AlphaChip_Memory.g_b_Debugging:
                print("ISP : Activation_Setting : 조도가 높음")
            if i_CIS_Settitng_Vector != 1:                                     # CIS 조절 방향이 하강이 아니라면
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting :INTTIME 하강")
                i_x_illuminance_ov = AlphaChip_ISP_Mode.g_i_Illuminance - i_illuminance_target
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : 과거 Target 조도와의 차이 : ", i_x_illuminance_ov)
                i_CIS_Settitng_Vector = 2                                                   # 하강 방향 설정
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : INTTIME 조절 시작")
                INTTime_set(False)                                                                                   # 하강 방향으로 INTTIME SETTING
            else:
                i_illuminance_ov = AlphaChip_ISP_Mode.g_i_Illuminance - i_illuminance_target
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : Activation_Setting : 과거 Target 조도와의 차이 : ", i_x_illuminance_ov)
                    print("ISP : Activation_Setting : 현재 Target 조도와의 차이 : ", i_illuminance_ov)
                if i_x_illuminance_ov < i_illuminance_ov:
                    if AlphaChip_Memory.g_b_Debugging:
                        print("ISP : Activation_Setting : 직전 CIS Setting 값으로 복원")
                    INTTime_set(True)                                                           # CIS Setting이 변경 됨
                break
        AlphaChip_ISP_Mode.ISP_New_Frame(False)
        
    AlphaChip_ISP_Mode.ISP_New_Frame(True)    
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