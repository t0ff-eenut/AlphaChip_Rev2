import AlphaChip_Memory
from ISP import AlphaChip_ISP_Mode

def Recheck_Process(b_real_time):
    if AlphaChip_Memory.g_b_Debugging:
        print()
        print("ISP : MODE : Recheck_Process")
        print("ISP : MODE : Recheck_Process : BYPASS : ", AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION'])
        if AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION']:
            print("ISP : MODE : Recheck_Process : BYPASS : count : ", AlphaChip_Memory.g_N_RECHECK_SETTING['_BYPASS_COUNT'])
        print()
    i_Occupancy_count = 0   # 재실 횟수
    if AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION']:
        i_Continual_count = 0   # 연속적 재실 횟수
    b_occupancy = False     # 재실 유무
    b_bypass = False        # 재실 ByPass
    
    for n in range(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']):                                                                             # AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT'] 만큼 반복
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : MODE : Recheck_Process : count : ", n)
            AlphaChip_ISP_Mode.display_status()
        if b_real_time:
            AlphaChip_ISP_Mode.ISP_New_Frame(True)                                                                                                                       # 새로운 Frame
            g_i_resualt = AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']     
            print("ISP : MODE : Recheck_Process : g_i_resualt : ", g_i_resualt)
            if AlphaChip_Memory.g_i_Occupancy_buffer_memory_point == 0:
                i_buffer_point = AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT'] - 1
            else :
                i_buffer_point = AlphaChip_Memory.g_i_Occupancy_buffer_memory_point - 1
        else:
            i_buffer_point = n
            
        if AlphaChip_Memory.g_b_A_Occupancy_buffer[i_buffer_point] == True:
            i_Occupancy_count += 1                                                                                                                              # 움직임 Count
            if AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION']:
                i_Continual_count += 1
        else :
            if AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION']:
                i_Continual_count = 0
            else :
                continue
                
        ## OPT : 연속적으로 3번 재실 조건에 맞다면
        if AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION']:
            ## 연속적으로 3번 재실 조건에 맞다면 ByPass
            if i_Continual_count >=  AlphaChip_Memory.g_N_RECHECK_SETTING['_BYPASS_COUNT']:
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : Recheck_Process : BYPASSing")
                b_bypass = True
                b_occupancy = True
                break
        
    # ByPass가 아니라면
    if not b_bypass:
        ## 재실 퍼센트 계산
        if AlphaChip_Memory.g_b_Debugging:
            print("ISP : MODE : Recheck_Process : 재실 Frame 갯수 : ", i_Occupancy_count)
            print("ISP : MODE : Recheck_Process : 재실 인정 횟수 : ", AlphaChip_Memory.g_N_RECHECK_SETTING['_OCCUPANCY_ACKNOWIEDGMENT_COUNT'])
        if i_Occupancy_count >= AlphaChip_Memory.g_N_RECHECK_SETTING['_OCCUPANCY_ACKNOWIEDGMENT_COUNT']:                                ###### 재실이라면 #######
            b_occupancy = True
        else:
            b_occupancy = False
    print("ISP : MODE : Recheck_Process : 재실 : ", b_occupancy)
    return b_occupancy

