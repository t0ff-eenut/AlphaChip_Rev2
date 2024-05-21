import threading, time
from CIS import AlphaChip_CIS, AlphaChip_CIS_Setting
from ISP import AlphaChip_ISP_Mode
import AlphaChip_Memory

i_x_illuminance_check_time = time.time()

# 해상도, 프레임 속도
g_A_Mode_Setting = [
    # PiRA_1
      [[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]         # IDLE
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # POWER ON
       ,[AlphaChip_Memory.g_N_SCALE['16x16'], AlphaChip_Memory.g_FRAME_SPEED['1FRAME'], AlphaChip_Memory.g_CIS_MODE['RAW']]         # STAND BY
       ,[AlphaChip_Memory.g_N_SCALE['16x16'], AlphaChip_Memory.g_FRAME_SPEED['3FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]         # WATCH
       ,[0,0,0]
       ,[0,0,0]
       ,[0,0,0]
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]       # ACTIVE
       ,[0,0,0]]
    # PiRA_2
      ,[[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # IDLE
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # POWER ON
       ,[AlphaChip_Memory.g_N_SCALE['16x16'], AlphaChip_Memory.g_FRAME_SPEED['1FRAME'], AlphaChip_Memory.g_CIS_MODE['RAW']]         # STAND BY
       ,[AlphaChip_Memory.g_N_SCALE['16x16'], AlphaChip_Memory.g_FRAME_SPEED['3FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]         # WATCH
       ,[0,0,0]
       ,[0,0,0]
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # DETECT
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # ACTIVE
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]]       # RECHECK
    # SSL-G_1
      ,[[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # IDLE
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # POWER ON
       ,[AlphaChip_Memory.g_N_SCALE['16x16'], AlphaChip_Memory.g_FRAME_SPEED['1FRAME'], AlphaChip_Memory.g_CIS_MODE['RAW']]         # STAND BY
       ,[AlphaChip_Memory.g_N_SCALE['16x16'], AlphaChip_Memory.g_FRAME_SPEED['3FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]         # WATICH
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # LOW RECHECK
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # LED ON
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # DETECT
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # ACTIVE
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]]       # RECHECK
    # SSL-G_2
      ,[[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # IDLE
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # POWER ON
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['RAW']]        # STAND BY
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # WATCH
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['LOW']]        # LOW RECHECK
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # LED ON
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # DETECT
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]        # ACTIVE
       ,[AlphaChip_Memory.g_N_SCALE['64x64'], AlphaChip_Memory.g_FRAME_SPEED['12FRAME'], AlphaChip_Memory.g_CIS_MODE['HIGH']]]       # RECHECK
      ]

def Change_CIS_Set():
    i_cis_mode = g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][2]
    if i_cis_mode == AlphaChip_Memory.g_CIS_MODE['LOW']:
        i_gain = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : Change_CIS_Set : Change LOW CIS Setting")

    elif i_cis_mode == AlphaChip_Memory.g_CIS_MODE['HIGH']:
        i_gain = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : Change_CIS_Set : Change HIGH CIS Setting")
            
    elif i_cis_mode == AlphaChip_Memory.g_CIS_MODE['RAW']:
        i_gain = AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN']
        i_inttime = AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME']
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : Change_CIS_Set : Change RAW CIS Setting")
    i_frame_speed = g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][1]

    AlphaChip_CIS_Setting.CIS_Gain_Set(i_cis_mode, i_gain)
    AlphaChip_CIS_Setting.CIS_INT_Set(i_cis_mode, i_inttime)
    if AlphaChip_Memory.g_b_Debugging:
        print("ISP : Change_CIS_Set : Change Frame Speed Setting")
    AlphaChip_CIS_Setting.CIS_Frame_Set(i_frame_speed)
    
    AlphaChip_Memory.g_b_FRAME_READY = False     # 새로운 Frame 완료
    AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO = [True] * 2
    AlphaChip_Memory.g_b_A_Illuminance_buffer = [0] * AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']
    AlphaChip_Memory.g_b_A_Occupancy_buffer = [False] * AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']
    AlphaChip_Memory.g_RESULT_STS_REGISTER['Illuminance_data_x'] = 0
    AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data'] = 0
    
    AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME'] = False  
    AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = False

def illumination():
    global i_x_illuminance_check_time
    i_illuminance_check_time = time.time()
    if g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['64x64']:
        i_target_size_x = i_target_size_y = 64
    elif g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['16x16']:
        i_target_size_x = i_target_size_y = 16
    ##################################################### illumination #####################################################################
    # raw_metadata = AlphaChip_CIS.g_PICAM_RAW.capture_metadata()
    # AlphaChip_Memory.g_RESULT_STS_REGISTER['_LUX'] = raw_metadata['Lux'] # 실제 LUX 값
    i_process_illu = 0
    for i_pointer in range(i_target_size_y*i_target_size_x):
        i_process_illu += AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][int(AlphaChip_Memory.g_b_FRAME_SRAM_SW)][int(i_pointer/i_target_size_y), int(i_pointer%i_target_size_x)]
    i_process_illu /= (i_target_size_y*i_target_size_x) # 측정 조도 값
    AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x'] = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']
    AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data'] = int(i_process_illu) # 측정 조도 값
    if AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data'] < AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x']:
        AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta_signal'] = True
        AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta'] = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x'] - AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']
    else:
        AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta_signal'] = False
        AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta'] = AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data'] - AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data_x']
        
    if i_illuminance_check_time - i_x_illuminance_check_time > AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_ILLUMINANCE_CHECK_TIME']:
        AlphaChip_Memory.g_b_A_Illuminance_buffer[AlphaChip_Memory.g_i_Illuminance_buffer_memory_point] = int(i_process_illu)
        i_x_illuminance_check_time = i_illuminance_check_time
        
        i_illuminance_min = 255
        i_illuminance_max = 0
        i_buffer_data_count = 0
        i_buffer_illuminance_sum = 0
        for i_pointer in range(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']):
            if not AlphaChip_Memory.g_b_A_Illuminance_buffer[i_pointer] == 0:
                if i_illuminance_max < AlphaChip_Memory.g_b_A_Illuminance_buffer[i_pointer]:
                    i_illuminance_max = AlphaChip_Memory.g_b_A_Illuminance_buffer[i_pointer]
                if i_illuminance_min > AlphaChip_Memory.g_b_A_Illuminance_buffer[i_pointer]:
                    i_illuminance_min = AlphaChip_Memory.g_b_A_Illuminance_buffer[i_pointer]
                i_buffer_illuminance_sum += AlphaChip_Memory.g_b_A_Illuminance_buffer[i_pointer]
                i_buffer_data_count += 1
        AlphaChip_Memory.g_i_Illuminance_Buffer_avg = i_buffer_illuminance_sum / i_buffer_data_count
        AlphaChip_Memory.g_i_Illuminance_Buffer_delta = i_illuminance_max - i_illuminance_min
        
        AlphaChip_Memory.g_i_Illuminance_buffer_memory_point += 1
        AlphaChip_Memory.g_i_Illuminance_buffer_memory_point = AlphaChip_Memory.g_i_Illuminance_buffer_memory_point % AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']      
        
        
    
    ##################################################### illumination #####################################################################

def Result_data():
    global F_Delta_Frame_W
    if g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['64x64']:
        i_target_size_x = i_target_size_y = 64
    elif g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['16x16']:
        i_target_size_x = i_target_size_y = 16
    ##################################################### Result_data #####################################################################
    F_Delta_Frame = AlphaChip_Memory.np.zeros((i_target_size_x,i_target_size_y), AlphaChip_Memory.np.uint8)
    F_Delta_Frame_W = AlphaChip_Memory.np.zeros((i_target_size_x,i_target_size_y), AlphaChip_Memory.np.uint8)
    i_resualt_data = 0  # Delta Pixel Count            
    for index in range(i_target_size_y*i_target_size_x):
        if AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][0][int(index/i_target_size_y), int(index%i_target_size_y)] > AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][1][int(index/i_target_size_y), int(index%i_target_size_y)]:
            i_code_delta = AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][0][int(index/i_target_size_y), int(index%i_target_size_y)] - AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][1][int(index/i_target_size_y), int(index%i_target_size_y)]
        else :
            i_code_delta = AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][1][int(index/i_target_size_y), int(index%i_target_size_y)] - AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][0][int(index/i_target_size_y), int(index%i_target_size_y)]
        F_Delta_Frame[int(index/i_target_size_y), int(index%i_target_size_y)] = i_code_delta
        
        if (((g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['LOW']) and (i_code_delta >= AlphaChip_Memory.g_TP1_REGISTER['_LOW_TP1'])) 
        or ((g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['HIGH']) and (i_code_delta >= AlphaChip_Memory.g_TP1_REGISTER['_HIGH_TP1']))):
            i_resualt_data += 1
            F_Delta_Frame_W[int(index/i_target_size_y), int(index%i_target_size_y)] = 255
        else:
            F_Delta_Frame_W[int(index/i_target_size_y), int(index%i_target_size_y)] = 0
    AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data'] = i_resualt_data
    
    # 재실중임을 판단할 때만 사용
    if (((g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['LOW']) and ((i_resualt_data >= AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MIN']) and (i_resualt_data <= AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MAX'])))
        or ((g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['HIGH']) and ((i_resualt_data >= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN']) and (i_resualt_data <= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX'])))):                                                # 현재 CIS Setting
        AlphaChip_Memory.g_b_A_Occupancy_buffer[AlphaChip_Memory.g_i_Occupancy_buffer_memory_point] = True
    elif (((g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['LOW']) and not ((i_resualt_data >= AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MIN']) and (i_resualt_data <= AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MAX'])))
        or ((g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['HIGH']) and not ((i_resualt_data >= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN']) and (i_resualt_data <= AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX'])))):
        AlphaChip_Memory.g_b_A_Occupancy_buffer[AlphaChip_Memory.g_i_Occupancy_buffer_memory_point] = False
    AlphaChip_Memory.g_i_Occupancy_buffer_memory_point += 1
    AlphaChip_Memory.g_i_Occupancy_buffer_memory_point = AlphaChip_Memory.g_i_Occupancy_buffer_memory_point % AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']            
    
    ##################################################### Result_data #####################################################################
    
def ISP():
    global g_i_Mode
    g_i_Mode = 0
    BackGround_Mode_STS = threading.Thread(name="BackGround_Mode_STS", target=AlphaChip_ISP_Mode.Mode, daemon=True) # MODE 동작 Thread
    ###############################################################반복#####################################################################

    while True:     
        if AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']:  # 만약 CIS Setting이 변경 되었다면
            Change_CIS_Set()
            
        AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT'] = True        # CIS와 ISP의 통신 중
        # CIS_Frame_ADC   
        AlphaChip_CIS.CIS_ADC()
        AlphaChip_Memory.g_INT_STS_REGISTER['FRAME_BUF_STS'] = AlphaChip_Memory.g_INT_STS_REGISTER['FRAME_BUF_STS'] | 1 << int(AlphaChip_Memory.g_b_FRAME_SRAM_SW)       # FRAME_BUF_STS
        AlphaChip_Memory.g_F_A_FRAME_BUFF[g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][g_i_Mode][0]][int(AlphaChip_Memory.g_b_FRAME_SRAM_SW)] = AlphaChip_CIS.g_F_Process_image
        AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[int(AlphaChip_Memory.g_b_FRAME_SRAM_SW)] = False
        AlphaChip_Memory.g_INT_STS_REGISTER['FRAME_BUF_STS'] = AlphaChip_Memory.g_INT_STS_REGISTER['FRAME_BUF_STS'] & ~(1 << int(AlphaChip_Memory.g_b_FRAME_SRAM_SW))    # FRAME_BUF_STS
        illumination()    # 조도 계산 값
        # # Buff 2개 다 Frame 존재 시
        if ((AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[0] == False) & (AlphaChip_Memory.g_F_A_FRAME_BUFF_ZERO[1] == False) 
            & (AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] != AlphaChip_Memory.g_N_mode['STAND_BY_MODE'])):
            Result_data() # 차영상연산 진행
            # 디버그) 차영상 이미지 출력
            if AlphaChip_Memory.g_b_Debugging:
                AlphaChip_CIS.cv2.imshow("F_Delta_Frame_W", F_Delta_Frame_W)    
                AlphaChip_CIS.cv2.waitKey(1) 
        AlphaChip_Memory.g_b_FRAME_READY = True                         # 새로운 Frame 완료 ISP
        AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME'] = True     # 새로운 Frame 완료 CPU
        AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT'] = False    # CIS와 ISP의 통신 종료
        AlphaChip_Memory.g_b_FRAME_SRAM_SW = not AlphaChip_Memory.g_b_FRAME_SRAM_SW # 다음 저장할 Frame Buffer 공간 선택
        
        if AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME'] and not BackGround_Mode_STS.is_alive():
            BackGround_Mode_STS.start()
        
        # 디버그) 이미지 출력
        if AlphaChip_Memory.g_b_Debugging:        
            AlphaChip_CIS.cv2.imshow("image", AlphaChip_CIS.g_F_Process_image)
            AlphaChip_CIS.cv2.waitKey(1)
    ###############################################################반복#####################################################################