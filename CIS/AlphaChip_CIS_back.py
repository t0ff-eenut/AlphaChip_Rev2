from picamera2 import Picamera2
import cv2, time, os
import AlphaChip_Memory
from ISP import AlphaChip_ISP
#### GAIN 22 max
g_i_sensor_mode = 2
i_zero_count = 0
def PiCamera_INIT():
    global g_PICAM_RAW
    g_PICAM_RAW = Picamera2()
    if AlphaChip_Memory.g_RAW_CAM :
        preview_config = g_PICAM_RAW.create_preview_configuration(raw=g_PICAM_RAW.sensor_modes[g_i_sensor_mode])
        g_PICAM_RAW.configure(preview_config)
    else : 
        preview_config = g_PICAM_RAW.create_preview_configuration()
    g_PICAM_RAW.controls.AnalogueGain = AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN']          # RAW Gain Set
    g_PICAM_RAW.controls.ExposureTime = AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME']  # RAW INTTime Set
    g_PICAM_RAW.start()

i_image_count = 0
i_read_image_number = 0
i_x_Mode = -1
b_Change_Image = False
b_Frame_Ready = False
s_image_addr = ''
A_image_list = []
def CIS_ADC():
    global g_F_Process_image, i_zero_count, i_image_count, i_x_Mode, b_Frame_Ready, s_image_addr, A_image_list, b_Change_Image, i_read_image_number
    # if AlphaChip_Memory.g_RAW_CAM :
    #     F_RAW_image = g_PICAM_RAW.capture_array("raw")
    #     i_RAW_image_y, i_RAW_image_x = F_RAW_image.shape        #1520 3072 # 3040 6112
    #     # print(raw.shape)
    #     # print(raw_x, raw_y)
    #     i_sensor_x, i_sensor_y = g_PICAM_RAW.sensor_modes[g_i_sensor_mode]['size']
    #     # print(Original_x, Original_y)
    #     for j in range(i_RAW_image_x-1, int(i_sensor_x*1.5)-1 ,-1):
    #         F_RAW_image = AlphaChip_Memory.np.delete(F_RAW_image, j, 1) 
    #     A = F_RAW_image.reshape(int(F_RAW_image.size/3),3)
    #     A  = AlphaChip_Memory.np.delete(A, 2, 1)
    #     A = A.reshape(i_sensor_y,i_sensor_x) # 1520, 2028
    # else :
    #     Original = g_PICAM_RAW.capture_array()
    #     A = cv2.cvtColor(Original, cv2.COLOR_BGR2GRAY)  
        
    # original_y, original_x = A.shape

    # if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['64x64']:
    #     i_target_size_x = i_target_size_y = 64
    # elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['16x16']:
    #     i_target_size_x = i_target_size_y = 16
            
    
    # F_temp = AlphaChip_Memory.np.zeros((i_target_size_y,i_target_size_x), AlphaChip_Memory.np.uint8)    # 빈 공간 생성
    # x_raising = int(original_x / i_target_size_x)                                                       # x_증가 폭
    # x_start = int(x_raising / 2)                                                                        # x_시작 점
    # y_raising = int(original_y / i_target_size_y)                                                       # y_증가 폭
    # y_start = int(y_raising / 2)                                                                        # y_시작 점
    # for point in range(0, i_target_size_y * i_target_size_x, 1):                                        # 모든 픽셀에 대해서            
    #     F_temp[int(point / i_target_size_x), int(point % i_target_size_x)] = A[y_start + (y_raising * int(point / i_target_size_x)), x_start + (x_raising * int(point % i_target_size_x))]
    # g_F_Process_image = F_temp
    
    
    
    
    
    
    
    if i_x_Mode != AlphaChip_ISP.g_i_Mode:
        i_x_Mode = AlphaChip_ISP.g_i_Mode
        b_illuminance = False
        i_read_image_number = 0
        i_image_count = 0
        b_Change_Image = True
        
    # if ((AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['WATCH_MODE'] and i_image_count > 10)
    #     or (AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE'] and ((i_image_count > 10 and i_image_count <= 13) or i_image_count > 13))
    #     or (AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LED_ON'] and i_image_count > 3)
    #     or (AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['DETECT_MODE'] and (i_image_count > 170 or i_image_count > 7))
    #     or (AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['ACTIVE_MODE'] and i_image_count > 100)
    #     or (AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['RECHECK_MODE'] and i_image_count > 20)):
    #     b_Change_Image = True
    
    if b_Change_Image == True:
        b_Change_Image = False
        A_image_list = []
        s_image_addr = 'Test_image/Maker_240508/'
        
        # Test_image/Maker_240508/Background/Process/HIGH_12F/240508_170332_L60
        
    #     if AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['IDLE_MODE']:
    #         s_image_type = 'Background'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['POWER_ON_MODE']:
    #         s_image_type = 'Background'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['STAND_BY_MODE']:
    #         s_image_type = 'Background'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['WATCH_MODE']:
    #         if i_image_count <= 10:
    #             s_image_type = 'Background'
    #         else:
    #             s_image_type = 'InterMove'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE']:
    #         if i_image_count <= 10 :
    #             s_image_type = 'Background'
    #         elif i_image_count > 10 and i_image_count <= 13:
    #             s_image_type = 'InterMove'
    #         else:
    #             s_image_type = 'Occupancy'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LED_ON']:
    #         if i_image_count <= 3:
    #             s_image_type = 'InterMove'
    #         else:
    #             s_image_type = 'Occupancy'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['DETECT_MODE']:
    #         if i_image_count <= 30:
    #             s_image_type = 'Background'
    #         elif i_image_count > 170:
    #             s_image_type = 'Background'
    #         else:
    #             s_image_type = 'Occupancy'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['ACTIVE_MODE']:
    #         if i_image_count <= 100:
    #             s_image_type = 'Occupancy'
    #         else:
    #             s_image_type = 'Background'
    #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['RECHECK_MODE']:
    #         if i_image_count <= 20:
    #             s_image_type = 'Occupancy'
    #         else:
    #             s_image_type = 'Background'
    #     s_image_addr = s_image_addr + s_image_type + '/Process/'
        
        
    #     s_cis_mode_type = ''
    #     if (AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['LOW']
    #         or (AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['DETECT_MODE'] and i_image_count > 170)):
    #         s_cis_mode_type = 'LOW'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['HIGH']:
    #         s_cis_mode_type = 'HIGH'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['RAW']:
    #         s_cis_mode_type = 'RAW'
    #     s_image_addr = s_image_addr + s_cis_mode_type + '_'
        
        
    #     s_FPS_type = ''
    #     if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['12FRAME']:
    #         s_FPS_type = '12'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['6FRAME']:
    #         s_FPS_type = '6'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['4FRAME']:
    #         s_FPS_type = '4'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['3FRAME']:
    #         s_FPS_type = '3'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['2FRAME']:
    #         s_FPS_type = '2'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['1FRAME']:
    #         s_FPS_type = '1'
    #     s_image_addr = s_image_addr + s_FPS_type + 'F'


    #     i_lux_min = 255
    #     i_lux_max = 0
    #     for dir_member in os.listdir(s_image_addr):                 #폴더 안에 파일 확인
    #         if os.path.isdir(s_image_addr+'/'+dir_member):          #폴더가 맞으면 재귀함수
    #             s_dir_member_split = dir_member.split('_')
    #             s_dir_lux = s_dir_member_split[2][1:2]
    #             if not s_cis_mode_type == 'RAW':
    #                 if int(s_dir_lux[0]) > i_lux_max:
    #                     i_lux_max = int(s_dir_lux[0])
    #                     s_image_addr = s_image_addr + '/' + dir_member
    #             else:
    #                 if int(s_dir_lux[0]) < i_lux_min:
    #                     i_lux_min = int(s_dir_lux[0])
    #                     s_image_addr = s_image_addr + '/' + dir_member

    #     if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['64x64']:
    #         s_scale_type = '64'
    #     elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['16x16']:
    #         s_scale_type = '16'



    
    #     for dir_member in os.listdir(s_image_addr):                 #폴더 안에 파일 확인
    #         if (s_image_addr+'/'+dir_member).endswith('.pgm'):      #찾는 파일이 맞을경우
    #             s_split_file_name = dir_member.split('_')
    #             if s_split_file_name[0] == s_scale_type:
    #                 A_image_list.append(s_split_file_name)
                  
                  
                    
    # s_image_addr_2 = s_image_addr + '/'
    # for i in range(len(A_image_list)):
    #     if int(A_image_list[i][3]) == i_image_count:
    #         s_file_addr = ''
    #         for x in range(len(A_image_list[i])):
    #             if x == len(A_image_list[i]) - 1:
    #                 s_file_addr = s_file_addr + A_image_list[i][x]
    #             else:
    #                 s_file_addr = s_file_addr + A_image_list[i][x] + '_'
    #         s_image_addr_2 = s_image_addr_2 + s_file_addr
    #         print("s_image_addr : ", s_image_addr_2)
    #         g_F_Process_image = cv2.imread(s_image_addr_2, cv2.IMREAD_UNCHANGED)
    #         b_Frame_Ready = True
    #         break

    # i_image_count += 1
    # if i_image_count > len(A_image_list):
    #     i_image_count = 0
    
        i_Target = AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']
        if i_Target == AlphaChip_Memory.g_N_TARGET['PIRA_1']:
            if AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['IDLE_MODE']:
                s_image_type = 'Background'
                b_illuminance = True
            elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['POWER_ON_MODE']:
                s_image_type = 'Background'
                b_illuminance = True
            elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['STAND_BY_MODE']:
                s_image_type = 'Background' # HIGH
                b_illuminance = True
                if i_image_count > 20:
                    s_image_type = 'Background' # LOW
                    b_illuminance = False
            elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['WATCH_MODE']:
                s_image_type = 'Background' # LOW
                b_illuminance = False
                if i_image_count > 20:
                    s_image_type = 'Background' # HIGH
                    b_illuminance = True
            elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['ACTIVE_MODE']:
                s_image_type = 'Background' # HIGH
                b_illuminance = True
                if i_image_count > 20:
                    s_image_type = 'InterMove'  # HIGH
                    b_illuminance = True
                elif i_image_count > 25:
                    s_image_type = 'Occupancy'  # HIGH
                    b_illuminance = True
                elif i_image_count > 125:
                    s_image_type = 'InterMove'  # HIGH
                    b_illuminance = True
                elif i_image_count > 130:
                    s_image_type = 'Background' # HIGH
                    b_illuminance = True
                elif i_image_count > 150:
                    s_image_type = 'Background' # LOW
                    b_illuminance = False
                
                
        # if i_Target == AlphaChip_Memory.g_N_TARGET['PIRA_2']:
        #     if AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['IDLE_MODE']:
        #         s_image_type = 'Background'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['POWER_ON_MODE']:
        #         s_image_type = 'Background'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['STAND_BY_MODE']:
        #         s_image_type = 'Background' # HIGH
        #         s_image_type = 'Background' # LOW
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['WATCH_MODE']:
        #         s_image_type = 'Background' # LOW
        #         s_image_type = 'Background' # HIGH
        #         s_image_type = 'InterMove'  # LOW
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE']:
        #         s_image_type = 'Background' # 
        #         s_image_type = 'InterMove'
        #         s_image_type = 'Occupancy'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LED_ON']:
        #         s_image_type = 'InterMove'
        #         s_image_type = 'Occupancy'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['DETECT_MODE']:
        #         s_image_type = 'Background'
        #         s_image_type = 'Background'
        #         s_image_type = 'Occupancy'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['ACTIVE_MODE']:
        #         s_image_type = 'Background' # HIGH  
        #         s_image_type = 'InterMove'  # HIGH
        #         s_image_type = 'Occupancy'  # HIGH
        #         s_image_type = 'InterMove'  # HIGH
        #         s_image_type = 'Background' # HIGH
        #         s_image_type = 'Background' # LOW
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['RECHECK_MODE']:
        #         s_image_type = 'Occupancy'
        #         s_image_type = 'Background'
                
        # if i_Target == AlphaChip_Memory.g_N_TARGET['SSL_1']:
        #     if AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['IDLE_MODE']:
        #         s_image_type = 'Background'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['POWER_ON_MODE']:
        #         s_image_type = 'Background'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['STAND_BY_MODE']:
        #         s_image_type = 'Background' # HIGH
        #         s_image_type = 'Background' # LOW
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['WATCH_MODE']:
        #         s_image_type = 'Background' # LOW
        #         s_image_type = 'Background' # HIGH
        #         s_image_type = 'InterMove'  # LOW
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE']:
        #         s_image_type = 'Background' # 
        #         s_image_type = 'InterMove'
        #         s_image_type = 'Occupancy'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LED_ON']:
        #         s_image_type = 'InterMove'
        #         s_image_type = 'Occupancy'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['DETECT_MODE']:
        #         s_image_type = 'Background'
        #         s_image_type = 'Background'
        #         s_image_type = 'Occupancy'
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['ACTIVE_MODE']:
        #         s_image_type = 'Background' # HIGH  
        #         s_image_type = 'InterMove'  # HIGH
        #         s_image_type = 'Occupancy'  # HIGH
        #         s_image_type = 'InterMove'  # HIGH
        #         s_image_type = 'Background' # HIGH
        #         s_image_type = 'Background' # LOW
        #     elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['RECHECK_MODE']:
        #         s_image_type = 'Occupancy'
        #         s_image_type = 'Background'
                
        s_image_addr = s_image_addr + s_image_type + '/Process/'
        
        s_cis_mode_type = ''
        if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['LOW']:
            s_cis_mode_type = 'LOW'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['HIGH']:
            s_cis_mode_type = 'HIGH'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['RAW']:
            s_cis_mode_type = 'RAW'
        s_image_addr = s_image_addr + s_cis_mode_type + '_'
        
        s_FPS_type = ''
        if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['12FRAME']:
            s_FPS_type = '12'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['6FRAME']:
            s_FPS_type = '6'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['4FRAME']:
            s_FPS_type = '4'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['3FRAME']:
            s_FPS_type = '3'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['2FRAME']:
            s_FPS_type = '2'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] == AlphaChip_Memory.g_FRAME_SPEED['1FRAME']:
            s_FPS_type = '1'
        s_image_addr = s_image_addr + s_FPS_type + 'F'            
                
        i_lux_min = 255
        i_lux_max = 0
        s_dir_member_min = ''
        s_dir_member_max = ''
        for dir_member in os.listdir(s_image_addr):                 #폴더 안에 파일 확인
            if os.path.isdir(s_image_addr+'/'+dir_member):          #폴더가 맞으면 재귀함수
                s_dir_member_split = dir_member.split('_')
                s_dir_lux = s_dir_member_split[2][1:2]
                if int(s_dir_lux[0]) > i_lux_max:
                    i_lux_max = int(s_dir_lux[0])
                    s_dir_member_max = dir_member
                if int(s_dir_lux[0]) < i_lux_min:
                    i_lux_min = int(s_dir_lux[0])
                    s_dir_member_min = dir_member
    # Test_image/Maker_240508/Background/Process/HIGH_12F/240508_170332_L60
        if b_illuminance:
            s_image_addr = s_image_addr + '/' + s_dir_member_max
        else:
            s_image_addr = s_image_addr + '/' + s_dir_member_min
                
        if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['64x64']:
            s_scale_type = '64'
        elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['16x16']:
            s_scale_type = '16'
        
        for dir_member in os.listdir(s_image_addr):                 #폴더 안에 파일 확인
            if (s_image_addr+'/'+dir_member).endswith('.pgm'):      #찾는 파일이 맞을경우
                s_split_file_name = dir_member.split('_')
                if s_split_file_name[0] == s_scale_type:
                    A_image_list.append(s_split_file_name)
                  
    s_image_addr_2 = s_image_addr + '/'
    for i in range(len(A_image_list)):
        if int(A_image_list[i][3]) == i_read_image_number:
            s_file_addr = ''
            for x in range(len(A_image_list[i])):
                if x == len(A_image_list[i]) - 1:
                    s_file_addr = s_file_addr + A_image_list[i][x]
                else:
                    s_file_addr = s_file_addr + A_image_list[i][x] + '_'
            s_image_addr_2 = s_image_addr_2 + s_file_addr
            print("s_image_addr : ", s_image_addr_2)
            g_F_Process_image = cv2.imread(s_image_addr_2, cv2.IMREAD_UNCHANGED)
            b_Frame_Ready = True
            break

    i_image_count += 1
    i_read_image_number += 1
    if i_read_image_number > len(A_image_list):
        i_read_image_number = 0
            
            
            
    print("sleep : ", AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] / 1000000)
    time.sleep(AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][1] / 1000000)                 
                

