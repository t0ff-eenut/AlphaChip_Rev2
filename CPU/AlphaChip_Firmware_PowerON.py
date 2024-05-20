import AlphaChip_Memory, display
from ISP import AlphaChip_ISP_Signal_Clear
from CPU import AlphaChip_Firmware, AlphaChip_Firmware_GainSetting, AlphaChip_Firmware_TPSetting

def PowerON():
    g_i_Target = AlphaChip_Memory.g_N_TARGET['PIRA_1']
    #g_i_Target = AlphaChip_Memory.g_N_TARGET['PIRA_2']
    #g_i_Target = AlphaChip_Memory.g_N_TARGET['SSL_1']

    g_i_LOW_GAIN = 4        # Gain 1-22
    g_i_LOW_INTTIME = 75000 # 최대 100ms (700us - 99371us)
    g_i_LOW_INTTIME_UD = 25000
    
    g_i_HIGH_GAIN = 4       # Gain 1-22
    g_i_HIGH_INTTIME = 75000 # 최대 100ms (700us - 99371us)
    g_i_HIGH_INTTIME_UD = 25000
    
    g_i_RAW_GAIN = 4        # Gain 1-22
    g_i_RAW_INTTIME = 100000 # 최대 100ms (700us - 99371us)

    # g_i_LOW_TP1 = 4
    # g_i_LOW_8_TP2_MIN = 5
    # g_i_LOW_8_TP2_MAX = 30
    # g_i_LOW_16_TP2_MIN = 12
    # g_i_LOW_16_TP2_MAX = 140
    # g_i_LOW_64_TP2_MIN = 130
    # g_i_LOW_64_TP2_MAX = 2000
    # g_i_HIGH_TP1 = 3
    # g_i_HIGH_64_TP2_MIN = 130
    # g_i_HIGH_64_TP2_MAX = 1900
    
    # g_i_LOW_GAIN = 3        # Gain 1-22
    # g_i_LOW_INTTIME = 75000 # 최대 100ms (700us - 99371us)
    # g_i_LOW_INTTIME_UD = 25000
    
    # g_i_HIGH_GAIN = 22       # Gain 1-22
    # g_i_HIGH_INTTIME = 75000 # 최대 100ms (700us - 99371us)
    # g_i_HIGH_INTTIME_UD = 25000
    
    # g_i_RAW_GAIN = 4        # Gain 1-22
    # g_i_RAW_INTTIME = 20000 # 최대 100ms (700us - 99371us)

 
    g_i_LOW_16_TP2_MIN = 60
    g_i_LOW_64_TP2_MIN = 145
    g_i_HIGH_64_TP2_MIN = 145
    # g_i_LOW_16_TP2_MIN = 30
    # g_i_LOW_64_TP2_MIN = 600
    # g_i_HIGH_64_TP2_MIN = 250
    g_i_LOW_TP1 = 3

    g_i_LOW_16_TP2_MAX = int((16*16)/2) - 20

    g_i_LOW_64_TP2_MAX = int((64*64)/2) - 500
    g_i_HIGH_TP1 = 4

    g_i_HIGH_64_TP2_MAX = int((64*64)/2) - 100
    g_i_TP2_SET_MARGIN_16 = 10
    g_i_TP2_SET_MARGIN_64 = 15
    
    g_i_LED_DIMMING_LEVEL_0 = AlphaChip_Memory.g_LED_DIMMING_LEVEL['_LED_LEVEL_0']
    g_i_LED_DIMMING_LEVEL_1 = AlphaChip_Memory.g_LED_DIMMING_LEVEL['_LED_LEVEL_2']
    g_i_LED_DIMMING_LEVEL_2 = AlphaChip_Memory.g_LED_DIMMING_LEVEL['_LED_LEVEL_4']
    g_i_LED_DIMMING_LEVEL_3 = AlphaChip_Memory.g_LED_DIMMING_LEVEL['_LED_LEVEL_6']
    g_i_LED_DIMMING_LEVEL_4 = AlphaChip_Memory.g_LED_DIMMING_LEVEL['_LED_LEVEL_8']
    g_i_LED_DIMMING_LEVEL_5 = AlphaChip_Memory.g_LED_DIMMING_LEVEL['_LED_LEVEL_10']
    g_i_Dimming_wait_time = 50  # ms
    g_i_LED_on_time = 15        # s

    g_i_illuminance_range_max = 100
    g_i_illuminance_range_min = 80
    
    g_i_illuminance_dark_TH = 120   # 밤으로 인식할 조도 값
    g_i_LOW_Ext_Light_TH = 4
    g_i_HIGH_Ext_Light_TH = 2
    g_i_mode_time = 60
  
    ##############################################################

    AlphaChip_Memory.g_CPU_SET_REGISTER['CLK_OUT_DISABLE'] = False                                                      # 외부 CLK 출력 X
    AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] = AlphaChip_Memory.g_CPU_WAKE_UP_CHECK_TIME['8ms']    # CPU 부팅 체크 시간 설정
    AlphaChip_Memory.g_CPU_SET_REGISTER['GPIO_LED_IN_ENABLE'] = True                                                    # GPIO를 이용하여 LED 출력
    AlphaChip_Memory.g_CPU_SET_REGISTER['GPIO_LED_IN_ON_SEL'] = False                                                   # GPIO의 입력 신호에 따라 동작 방식 설정 -> False : HIGH 신호에 LED 출력, True : LOW 신호에 LED 출력
    
    AlphaChip_Memory.g_TP1_REGISTER['_LOW_TP1'] = g_i_LOW_TP1
    AlphaChip_Memory.g_TP1_REGISTER['_HIGH_TP1'] = g_i_HIGH_TP1
    AlphaChip_Memory.g_TP1_REGISTER['_LOW_LIGHT_Delta_TH'] = g_i_LOW_Ext_Light_TH
    AlphaChip_Memory.g_TP1_REGISTER['_HIGH_LIGHT_Delta_TH'] = g_i_HIGH_Ext_Light_TH
    
    AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MIN'] = g_i_LOW_16_TP2_MIN
    AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MAX'] = g_i_LOW_16_TP2_MAX
    AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MIN'] = g_i_LOW_64_TP2_MIN
    AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MAX'] = g_i_LOW_64_TP2_MAX
    AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN'] = g_i_HIGH_64_TP2_MIN
    AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX'] = g_i_HIGH_64_TP2_MAX
    # AlphaChip_Memory.g_TH_DATA_REGISTER['_TP2_SET_MARGIN_8'] = g_i_TP2_SET_MARGIN_8
    # AlphaChip_Memory.g_TH_DATA_REGISTER['_TP2_SET_MARGIN_16'] = g_i_TP2_SET_MARGIN_16
    # AlphaChip_Memory.g_TH_DATA_REGISTER['_TP2_SET_MARGIN_64'] = g_i_TP2_SET_MARGIN_64

    
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_AMP_GAIN'] = g_i_LOW_GAIN
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME'] = g_i_LOW_INTTIME
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL'] = g_i_LOW_INTTIME_UD
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_AMP_GAIN'] = g_i_HIGH_GAIN
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME'] = g_i_HIGH_INTTIME
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL'] = g_i_HIGH_INTTIME_UD
    
    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME'] = g_i_RAW_INTTIME
    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN'] = g_i_RAW_GAIN
    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_Illuminance_DARK_TH'] = g_i_illuminance_dark_TH      # 밤으로 인식할 조도 값
    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_ILLUMINANCE_CHECK_TIME'] = 1                           # 밤으로 인식할 조도 값

    AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] = g_i_Target

    AlphaChip_Memory.g_INT_TIME_SET_REGISTER['HIGH_INT_MIN'] = 700
    AlphaChip_Memory.g_INT_TIME_SET_REGISTER['LOW_INT_MIN'] = 700
    AlphaChip_Memory.g_INT_TIME_SET_REGISTER['HIGH_INT_MAX'] = 100000
    AlphaChip_Memory.g_INT_TIME_SET_REGISTER['LOW_INT_MAX'] = 100000
    
    AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH'] = 50
    AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH'] = 1500
    ######## AlphaChip_Memory.g_PIRA_PULSE_REGISTER['SIGNAL_CHECK'] = True
    AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'] = 1
    
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_0'] = g_i_LED_DIMMING_LEVEL_0
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_1'] = g_i_LED_DIMMING_LEVEL_1
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_2'] = g_i_LED_DIMMING_LEVEL_2
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_3'] = g_i_LED_DIMMING_LEVEL_3
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_4'] = g_i_LED_DIMMING_LEVEL_4
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_5'] = g_i_LED_DIMMING_LEVEL_5
    # AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME'] = g_i_Dimming_wait_time            # DIMMING 단계마다 유지 시간 ms
    # AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_LED_ON_TIME'] = g_i_LED_on_time                     # LED ON 지속 시간 s

    AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MAX'] = g_i_illuminance_range_max
    AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN'] = g_i_illuminance_range_min    

    # AlphaChip_Memory.g_N_TIMER_SET_REGISTER['_WATCH_MODE_TIME'] = g_i_active_2_mode_time        #s        
    AlphaChip_Memory.g_N_TIMER_SET_REGISTER['_MODE_TIME'] = g_i_mode_time        #s        
    # AlphaChip_Memory.g_N_TIMER_SET_REGISTER['_LED_ON_TIME'] = 15
    
    
    AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT'] = 8
    AlphaChip_Memory.g_N_RECHECK_SETTING['_OCCUPANCY_ACKNOWIEDGMENT_COUNT'] = 6
    AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION'] = True
    AlphaChip_Memory.g_N_RECHECK_SETTING['_BYPASS_COUNT'] = 3
    AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_MAX'] = 8
    AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_MAX'] = 8


    ############################################################## 디버그 용 ##################################################################################
    if AlphaChip_Memory.g_b_Debugging:
        display.insert_Low_Gain_text.delete(0,10)
        display.insert_Low_Inttime_text.delete(0,10)
        display.insert_Low_Inttime_UD_text.delete(0,10)
        display.insert_High_Gain_text.delete(0,10)
        display.insert_High_Inttime_text.delete(0,10)
        display.insert_High_Inttime_UD_text.delete(0,10)
        display.insert_Raw_Gain_text.delete(0,10)
        display.insert_Raw_Inttime_text.delete(0,10)
        display.insert_Low_TP1_text.delete(0,10)
        # display.insert_Low_8_TP2_MIN_text.delete(0,10)
        # display.insert_Low_8_TP2_MAX_text.delete(0,10)
        display.insert_Low_16_TP2_MIN_text.delete(0,10)
        display.insert_Low_16_TP2_MAX_text.delete(0,10)
        display.insert_Low_64_TP2_MIN_text.delete(0,10)
        display.insert_Low_64_TP2_MAX_text.delete(0,10)
        display.insert_High_TP1_text.delete(0,10)
        # display.insert_High_8_TP2_MIN_text.delete(0,10)
        # display.insert_High_8_TP2_MAX_text.delete(0,10)
        display.insert_High_64_TP2_MIN_text.delete(0,10)
        display.insert_High_64_TP2_MAX_text.delete(0,10)

        display.insert_Low_Gain_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_AMP_GAIN']))
        display.insert_Low_Inttime_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']))
        display.insert_Low_Inttime_UD_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL']))
        display.insert_High_Gain_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_AMP_GAIN']))
        display.insert_High_Inttime_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']))
        display.insert_High_Inttime_UD_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL']))
        display.insert_Raw_Gain_text.insert(0, str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN']))
        display.insert_Raw_Inttime_text.insert(0, str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME']))
        display.insert_Low_TP1_text.insert(0, str(AlphaChip_Memory.g_TP1_REGISTER['_LOW_TP1']))
        # display.insert_Low_8_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MIN']))
        # display.insert_Low_8_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MAX']))
        display.insert_Low_16_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MIN']))
        display.insert_Low_16_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MAX']))
        display.insert_Low_64_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MIN']))
        display.insert_Low_64_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MAX']))
        display.insert_High_TP1_text.insert(0, str(AlphaChip_Memory.g_TP1_REGISTER['_HIGH_TP1']))
        # display.insert_High_8_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_8_TP2_MIN']))
        # display.insert_High_8_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_8_TP2_MAX']))
        display.insert_High_64_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN']))
        display.insert_High_64_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']))
        
        display.insert_Pseudo_Signal_Count_text.delete(0,10)
        display.insert_Pseudo_Signal_Count_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT']))
        display.insert_Pseudo_Signal_Width_text.delete(0,10)
        display.insert_Pseudo_Signal_Width_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH']))
        display.insert_Pseudo_Signal_Cycle_text.delete(0,10)
        display.insert_Pseudo_Signal_Cycle_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH']))

    
    # AlphaChip_Firmware.CPU_New_Frame(False)
    # if AlphaChip_Memory.g_b_Debugging:
    #     print("CPU : PowerON : CIS 최적화")
    # for n in range(1):
    #     if n == 0: # HIGH 64
    #         if AlphaChip_Memory.g_b_Debugging:
    #             print("CPU : PowerON : CIS 최적화 : HIGH 64")
    #         AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] = AlphaChip_Memory.g_N_SCALE['64x64']                        # 해상도 변경
    #         AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] = AlphaChip_Memory.g_N_CIS_MODE['HIGH']                # CIS 모드 변경
    #         AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_FRAME_SPEED'] = AlphaChip_Memory.g_FRAME_SPEED['12FRAME']            # FRAME 속도 변경
    #         AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                               # CIS Setting이 변경 됨
            
    #     # elif n == 1 :  # LOW 64
    #     #     if AlphaChip_Memory.g_b_Debugging:
    #     #         print("CPU : PowerON : CIS 최적화 : LOW 64")
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] = AlphaChip_Memory.g_N_SCALE['64x64']                        # 해상도 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] = AlphaChip_Memory.g_N_CIS_MODE['LOW']                # CIS 모드 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_FRAME_SPEED'] = AlphaChip_Memory.g_FRAME_SPEED['12FRAME']            # FRAME 속도 변경
    #     #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                               # CIS Setting이 변경 됨
            
    #     # elif n == 2: # HIGH 16
    #     #     if AlphaChip_Memory.g_b_Debugging:
    #     #         print("CPU : PowerON : CIS 최적화 : HIGH 16")
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] = AlphaChip_Memory.g_N_SCALE['16x16']                        # 해상도 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] = AlphaChip_Memory.g_N_CIS_MODE['HIGH']                # CIS 모드 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_FRAME_SPEED'] = AlphaChip_Memory.g_FRAME_SPEED['12FRAME']            # FRAME 속도 변경
    #     #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                               # CIS Setting이 변경 됨
            
    #     # elif n == 2 : # LOW 16
    #     #     if AlphaChip_Memory.g_b_Debugging:
    #     #         print("CPU : PowerON : CIS 최적화 : LOW 16")
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] = AlphaChip_Memory.g_N_SCALE['16x16']                        # 해상도 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] = AlphaChip_Memory.g_N_CIS_MODE['LOW']                # CIS 모드 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_FRAME_SPEED'] = AlphaChip_Memory.g_FRAME_SPEED['12FRAME']            # FRAME 속도 변경
    #     #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                               # CIS Setting이 변경 됨
            
    #     # elif n == 4: # HIGH 8
    #     #     if AlphaChip_Memory.g_b_Debugging:
    #     #         print("CPU : PowerON : CIS 최적화 : HIGH 8")
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] = AlphaChip_Memory.g_N_SCALE['8x8']                        # 해상도 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] = AlphaChip_Memory.g_N_CIS_MODE['HIGH']                # CIS 모드 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_FRAME_SPEED'] = AlphaChip_Memory.g_FRAME_SPEED['12FRAME']            # FRAME 속도 변경
    #     #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                               # CIS Setting이 변경 됨
            
    #     # elif n == 5 : # LOW 8
    #     #     if AlphaChip_Memory.g_b_Debugging:
    #     #         print("CPU : PowerON : CIS 최적화 : LOW 8")
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE'] = AlphaChip_Memory.g_N_SCALE['8x8']                        # 해상도 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING'] = AlphaChip_Memory.g_N_CIS_MODE['LOW']                # CIS 모드 변경
    #     #     AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_FRAME_SPEED'] = AlphaChip_Memory.g_FRAME_SPEED['12FRAME']            # FRAME 속도 변경
    #     #     AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                               # CIS Setting이 변경 됨
        
    #     AlphaChip_Firmware.CPU_New_Frame(False)
    #     ############################################################################################################################################################################################################################################################################################################################################################################################################                
    #     if AlphaChip_Firmware.g_i_liiuminance < AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN'] or AlphaChip_Firmware.g_i_liiuminance > AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MAX']: # 조도 Range에 없으면
    #         if AlphaChip_Memory.g_b_Debugging:
    #             print("CPU : POWER_ON : illuminance RANGE OUT")
    #         i_illuminance_target =  AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN'] + int((AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MAX'] - AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN']) / 2)       
    #         i_CIS_Settitng_Vector = 0               # 1 : 상승, 2 : 하강
    #         i_x_gain = 0
    #         i_x_inttime = 0
    #         i_x_illuminance_ov = 0
    #         while True:
    #             if AlphaChip_Firmware.g_i_liiuminance < i_illuminance_target:                                       # 조도가 낮으면
    #                 if AlphaChip_Memory.g_b_Debugging:
    #                     print("CPU : POWER_ON : illuminance RANGE OUT : 조도가 낮음")
    #                 if i_CIS_Settitng_Vector != 2:                                                                  # CIS 조절 방향이 하강이 아니라면
    #                     if AlphaChip_Memory.g_b_Debugging:
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : INTTIME 상승")
    #                     i_cis_setting = AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING']
    #                     if i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['LOW']:
    #                         i_x_gain = AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN']
    #                         i_x_inttime = AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']
    #                     elif i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['HIGH']:
    #                         i_x_gain = AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN']
    #                         i_x_inttime = AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']
                            
    #                     i_x_illuminance_ov = i_illuminance_target - AlphaChip_Firmware.g_i_liiuminance
    #                     if AlphaChip_Memory.g_b_Debugging:
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : 과거 Target 조도와의 차이 : ", i_x_illuminance_ov)
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : INTTIME 조절 시작")
    #                     i_CIS_Settitng_Vector = 1                                                                           # 상승 방향 설정
    #                     if AlphaChip_Firmware.INTTime_set(True) == -1:                                                                                   # 상승 방향으로 INTTIME SETTING
    #                         break                                                                                # 상승 방향으로 INTTIME SETTING
    #                 else:
    #                     i_illuminance_ov = i_illuminance_target - AlphaChip_Firmware.g_i_liiuminance
    #                     if AlphaChip_Memory.g_b_Debugging:
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : 과거 Target 조도와의 차이 : ", i_x_illuminance_ov)
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : 현재 Target 조도와의 차이 : ", i_illuminance_ov)
    #                     if i_x_illuminance_ov < i_illuminance_ov:
    #                         if AlphaChip_Memory.g_b_Debugging:
    #                             print("CPU : POWER_ON : illuminance RANGE OUT : 직전 CIS Setting 값으로 복원")
    #                         if i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['LOW']:
    #                             AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN'] = i_x_gain
    #                             AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME'] = i_x_inttime
    #                         elif i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['HIGH']:
    #                             AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN'] = i_x_gain
    #                             AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME'] = i_x_inttime
    #                         AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                              # CIS Setting이 변경 됨
    #                     break   
                    
    #             elif AlphaChip_Firmware.g_i_liiuminance > i_illuminance_target:       # 조도가 높고 CIS 조절 방향이 상승이 아니라면
    #                 if AlphaChip_Memory.g_b_Debugging:
    #                     print("CPU : POWER_ON : illuminance RANGE OUT : 조도가 높음")
    #                 if i_CIS_Settitng_Vector != 1:                                     # CIS 조절 방향이 하강이 아니라면
    #                     if AlphaChip_Memory.g_b_Debugging:
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : INTTIME 하강")
    #                     i_cis_setting = AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING']
    #                     if i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['LOW']:
    #                         i_x_gain = AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN']
    #                         i_x_inttime = AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']
    #                     elif i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['HIGH']:
    #                         i_x_gain = AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN']
    #                         i_x_inttime = AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']
    #                     i_x_illuminance_ov = AlphaChip_Firmware.g_i_liiuminance - i_illuminance_target
    #                     if AlphaChip_Memory.g_b_Debugging:
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : 과거 Target 조도와의 차이 : ", i_x_illuminance_ov)
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : INTTIME 조절 시작")
    #                     i_CIS_Settitng_Vector = 2                                                                           # 하강 방향 설정
    #                     if AlphaChip_Firmware.INTTime_set(False) == -1:                                                                                   # 상승 방향으로 INTTIME SETTING
    #                         break
    #                 else:
    #                     i_illuminance_ov = AlphaChip_Firmware.g_i_liiuminance - i_illuminance_target
    #                     if AlphaChip_Memory.g_b_Debugging:
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : 과거 Target 조도와의 차이 : ", i_x_illuminance_ov)
    #                         print("CPU : POWER_ON : illuminance RANGE OUT : 현재 Target 조도와의 차이 : ", i_illuminance_ov)
    #                     if i_x_illuminance_ov < i_illuminance_ov:
    #                         if AlphaChip_Memory.g_b_Debugging:
    #                             print("CPU : POWER_ON : illuminance RANGE OUT : 직전 CIS Setting 값으로 복원")
    #                         if i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['LOW']:
    #                             AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN'] = i_x_gain
    #                             AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME'] = i_x_inttime
    #                         elif i_cis_setting == AlphaChip_Memory.g_N_CIS_MODE['HIGH']:
    #                             AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN'] = i_x_gain
    #                             AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME'] = i_x_inttime
    #                         AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True                                                              # CIS Setting이 변경 됨
    #                     break
    #             AlphaChip_Firmware.CPU_New_Frame(False)
                
    #     print("CPU : POWER_ON : CIS 최적화 : 끝")       
    #     print()       
    AlphaChip_Firmware.CPU_New_Frame(True)
        # AlphaChip_Firmware_TPSetting.TPSetting()



            
    ############################################################################################################################################################################################################################################################################################################################################################################################################                                    
        
    










