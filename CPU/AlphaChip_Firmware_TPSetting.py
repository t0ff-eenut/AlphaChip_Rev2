import AlphaChip_Memory, display
from CPU import AlphaChip_Firmware
def TPSetting():
    if AlphaChip_Memory.g_b_Debugging:
        print()
        print("CPU : TPSetting : TP 최적화")
        
    i_stable_count = 0
    i_resualt_max = 0
    while i_stable_count < AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']:                                                                       # Recheck Buffer 만큼 Resualt 확인
        if AlphaChip_Memory.g_b_Debugging:
            print("CPU : TPSetting : TP 최적화 : 안정화 Count : ", i_stable_count)
            
        b_first_print = True
        while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:                                       # CIS Setting 중 이면
            if AlphaChip_Memory.g_b_Debugging and b_first_print:
                print("CPU : TPSetting : TP 최적화 : WAIT CHANGE CIS SETTING")
            b_first_print = False
            continue                                                                                                # 대기
        
        AlphaChip_Firmware.CPU_New_Frame(True)
        print("AlphaChip_ISP_Mode.g_i_resualt : ", AlphaChip_Firmware.g_i_resualt)
        if i_resualt_max < AlphaChip_Firmware.g_i_resualt:
            i_stable_count = 0
            i_resualt_max = AlphaChip_Firmware.g_i_resualt
        else :
            i_stable_count += 1
            
    if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] == AlphaChip_Memory.g_N_CIS_MODE['LOW']:
        if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] == AlphaChip_Memory.g_N_SCALE['64x64']:
            AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_64_TP2_MIN'] = i_resualt_max + AlphaChip_Memory.g_TH_DATA_REGISTER['_TP2_SET_MARGIN_64']
            display.insert_Low_64_TP2_MIN_text.delete(0,10)
            display.insert_Low_64_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_64_TP2_MIN']))
        elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] == AlphaChip_Memory.g_N_SCALE['16x16']:
            AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_16_TP2_MIN'] = i_resualt_max + AlphaChip_Memory.g_TH_DATA_REGISTER['_TP2_SET_MARGIN_16']
            display.insert_Low_16_TP2_MIN_text.delete(0,10)
            display.insert_Low_16_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_16_TP2_MIN']))
        elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] == AlphaChip_Memory.g_N_SCALE['8x8']:
            AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MIN'] = i_resualt_max + AlphaChip_Memory.g_TH_DATA_REGISTER['_TP2_SET_MARGIN_8']
            display.insert_Low_8_TP2_MIN_text.delete(0,10)
            display.insert_Low_8_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MIN']))
        
    elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] == AlphaChip_Memory.g_N_CIS_MODE['HIGH']:
        AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_64_TP2_MIN'] = i_resualt_max + AlphaChip_Memory.g_TH_DATA_REGISTER['_TP2_SET_MARGIN_64']
        display.insert_High_64_TP2_MIN_text.delete(0,10)
        display.insert_High_64_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_64_TP2_MIN']))
        
        
        
            
    b_first_print = True
    while AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:               # 만약 CIS Setting이 변경 되었다면
        if AlphaChip_Memory.g_b_Debugging and b_first_print:
            print("CPU : Firmware : WAIT CHANGE CIS SETTING")
            b_first_print = False