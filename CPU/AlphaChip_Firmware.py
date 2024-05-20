import AlphaChip_Memory
from ISP import AlphaChip_ISP_Mode, AlphaChip_ISP_Signal_Clear
from CPU import AlphaChip_Firmware_PowerON,AlphaChip_Firmware_GainSetting, AlphaChip_Firmware_TPSetting
# 새로운 이미지 받기
def CPU_New_Frame(resualt):
    global g_i_x_liiuminance, g_i_liiuminance, g_i_resualt
    while True:
        if not resualt :
            b_first_print = True
            while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:               # 만약 CIS Setting이 변경 되었다면
                if AlphaChip_Memory.g_b_Debugging and b_first_print:
                    print("CPU : Firmware : CPU_New_Frame : WAIT CHANGE CIS SETTING")
                    b_first_print = False
                continue    
            b_first_print = True
            AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NEW_FRAME'] = True               # 새로운 이미지 Signal 제거
            AlphaChip_ISP_Signal_Clear.clear_signal()                                       # Signal 제거 Clear
            while not AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME'] or AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                if AlphaChip_Memory.g_b_Debugging and b_first_print:
                    print("CPU : Firmware : CPU_New_Frame : WAIT NewFrame")
                    b_first_print = False
                continue
            
            g_i_x_liiuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x']    # 과거 조도 측정 값 저장
            g_i_liiuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']    # 현재 조도 측정 값 저장
            g_i_resualt = AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']  
            if AlphaChip_Memory.g_b_Debugging:
                print("CPU : Firmware : CPU_New_Frame : g_i_x_liiuminance : ", g_i_x_liiuminance)
                print("CPU : Firmware : CPU_New_Frame : g_i_liiuminance : ", g_i_liiuminance)
                print("CPU : Firmware : CPU_New_Frame : g_i_resualt : ", g_i_resualt)
                AlphaChip_ISP_Mode.display_status()
            break
        else:
            b_first_print = True
            while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:               # 만약 CIS Setting이 변경 되었다면
                if AlphaChip_Memory.g_b_Debugging and b_first_print:
                    print("CPU : Firmware : CPU_New_Frame : WAIT CHANGE CIS SETTING")
                    b_first_print = False
                continue    
            b_first_print = True
            AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NEW_FRAME'] = True               # 새로운 이미지 Signal 제거
            AlphaChip_ISP_Signal_Clear.clear_signal()                                       # Signal 제거 Clear
            while not AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME'] or AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                if AlphaChip_Memory.g_b_Debugging and b_first_print:
                    print("CPU : Firmware : CPU_New_Frame : WAIT NewFrame")
                    b_first_print = False
                continue
            
            g_i_x_liiuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x']    # 과거 조도 측정 값 저장
            g_i_liiuminance = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']    # 현재 조도 측정 값 저장
            g_i_resualt = AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']  
            if AlphaChip_Memory.g_b_Debugging:
                AlphaChip_ISP_Mode.display_status()
            if AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[0] == False and AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[1] == False:
                break

def INTTime_set(b_vector):    
    if AlphaChip_Memory.g_b_Debugging:
        print("CPU : Firmware : INTTime Setting")     
    i_gain = 0       
    i_inttime = 0
    i_inttime_UD = 0
    i_inttime_range_min = 0
    i_inttime_range_max = 0
    i_cis_setting = AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING']
    if i_cis_setting == AlphaChip_Memory.g_CIS_MODE['LOW']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CPU : Firmware : INTTime Setting : LOW INTTIME SETTING")
        i_gain = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']
        i_inttime_UD = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL']
        i_inttime_range_min = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MIN']
        i_inttime_range_max = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MAX']
    elif i_cis_setting == AlphaChip_Memory.g_CIS_MODE['HIGH']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CPU : Firmware : INTTime Setting : HIGH INTTIME SETTING")
        i_gain = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']
        i_inttime_UD = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL']
        i_inttime_range_min = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MIN']
        i_inttime_range_max = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MAX']
        
    if (b_vector == False and ((i_inttime - i_inttime_UD) < i_inttime_range_min)) or (b_vector == True and ((i_inttime + i_inttime_UD) > i_inttime_range_max)):
        if AlphaChip_Memory.g_b_Debugging:
            print("CPU : Firmware : INTTime Setting : INTTIME RANGE OVER")
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
            AlphaChip_Firmware_GainSetting.Gain_SET()
    else:        
        if b_vector == False:
            if AlphaChip_Memory.g_b_Debugging:
                print("CPU : Firmware : INTTime Setting : INTTIME DOWN")
            i_inttime -= i_inttime_UD
        elif b_vector == True:
            if AlphaChip_Memory.g_b_Debugging:
                print("CPU : Firmware : INTTime Setting : INTTIME UP")
            i_inttime += i_inttime_UD
            
        if i_cis_setting == AlphaChip_Memory.g_CIS_MODE['LOW']:
            AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME'] = i_inttime
        elif i_cis_setting == AlphaChip_Memory.g_CIS_MODE['HIGH']:
            AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME'] = i_inttime
    AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True 
    
    
# Power_ON
def Boot_CPU():
    if AlphaChip_Memory.g_b_Debugging:
        print()
        print("CPU Boot")
    AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK'] = True
    if AlphaChip_Memory.g_b_Debugging:
        print("CPU_WAKE_UP_CHECK")
    WakeUP = AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] # 모드 확인
    if WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['Power_On_setting']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CPU : PowerON")
        AlphaChip_Firmware_PowerON.PowerON()
    # Gain SET
    # Watch_Mode, Active_Mode_1
    elif WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['_Low_Gain_setting'] or WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['_High_Gain_setting']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CPU : Gain_SET")
        AlphaChip_Firmware_GainSetting.Gain_SET()
        
    elif WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['_TP_Setting']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CPU : TPSetting")
        AlphaChip_Firmware_TPSetting.TPSetting()

    AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE'] = True
    if AlphaChip_Memory.g_b_Debugging:
        print("CPU_DONE")
        print("CPU Boot end")
        
    


