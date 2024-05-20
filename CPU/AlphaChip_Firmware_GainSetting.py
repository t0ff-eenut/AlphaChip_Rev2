import AlphaChip_Memory
from CPU import AlphaChip_Firmware_TPSetting
def Gain_SET():
    b_vector = False # False 하강, True 상승       
    WakeUP = AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] # 모드 확인
    if WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['_Low_Gain_setting']:
        i_gain = AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']
        i_inttime_UD = AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL']
        i_inttime_range_min = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MIN']
        i_inttime_range_max = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MAX']
    elif WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['_High_Gain_setting']:
        i_gain = AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']
        i_inttime_UD = AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL']
        i_inttime_range_min = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MIN']
        i_inttime_range_max = AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MAX']
    
    if (i_inttime + i_inttime_UD) > i_inttime_range_max :
        b_vector = True
    elif (i_inttime - i_inttime_UD) < i_inttime_range_min :
        b_vector = False
    
    if (i_gain - 1) >= 1 and (i_gain + 1) <= 22:
        if b_vector == False:   
            i_gain -= 1
        elif b_vector == True:
            i_gain += 1
        i_inttime = i_inttime_range_min + (i_inttime_range_max - i_inttime_range_min) / 2
        if WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['_Low_Gain_setting']:
            AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN'] = i_gain
            AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME'] = i_inttime
        elif WakeUP == AlphaChip_Memory.g_WAKE_UP_STS['_High_Gain_setting']:
            AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN'] = i_gain
            AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME'] = i_inttime
            

    
