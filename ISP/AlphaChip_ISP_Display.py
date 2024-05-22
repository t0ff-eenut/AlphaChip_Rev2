import AlphaChip_Memory, Tkinter_Display_Start

from ISP import AlphaChip_ISP

def display_status():
    Tkinter_Display_Start.PiRA_1_text.configure(bg = 'gray')
    Tkinter_Display_Start.PiRA_2_text.configure(bg = 'gray')
    Tkinter_Display_Start.SSL_G_1_text.configure(bg = 'gray')
    Tkinter_Display_Start.SSL_G_2_text.configure(bg = 'gray')
    if AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['PIRA_1']:
        Tkinter_Display_Start.PiRA_1_text.configure(bg = 'green')
    elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['PIRA_2']:
        Tkinter_Display_Start.PiRA_2_text.configure(bg = 'green')
    elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_1']:
        Tkinter_Display_Start.SSL_G_1_text.configure(bg = 'green')
    elif AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET'] == AlphaChip_Memory.g_N_TARGET['SSL_2']:
        Tkinter_Display_Start.SSL_G_2_text.configure(bg = 'green')
        
    Tkinter_Display_Start.x16_text.configure(bg = 'gray')
    Tkinter_Display_Start.x64_text.configure(bg = 'gray')
    if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['64x64']:
        Tkinter_Display_Start.x64_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][0] == AlphaChip_Memory.g_N_SCALE['16x16']:
        Tkinter_Display_Start.x16_text.configure(bg = 'green')
    
    Tkinter_Display_Start.CPU_ON_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']))
    if AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']:
        Tkinter_Display_Start.CPU_ON_text_handle.configure(bg = 'green')
    else :
        Tkinter_Display_Start.CPU_ON_text_handle.configure(bg = 'gray')

    Tkinter_Display_Start.Low_text.configure(bg = 'gray')
    Tkinter_Display_Start.High_text.configure(bg = 'gray')
    Tkinter_Display_Start.Raw_text.configure(bg = 'gray')
    if AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['LOW']:
        Tkinter_Display_Start.Low_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['HIGH']:
        Tkinter_Display_Start.High_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_A_Mode_Setting[AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']][AlphaChip_ISP.g_i_Mode][2] == AlphaChip_Memory.g_CIS_MODE['RAW']:
        Tkinter_Display_Start.Raw_text.configure(bg = 'green')
        
    Tkinter_Display_Start.non_text.configure(bg = 'gray')
    Tkinter_Display_Start.Power_On_setting_text.configure(bg = 'gray')
    Tkinter_Display_Start.Low_Gain_setting_text.configure(bg = 'gray')
    Tkinter_Display_Start.High_Gain_setting_text.configure(bg = 'gray')
    Tkinter_Display_Start.Raw_Gain_setting_text.configure(bg = 'gray')
    
    if AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] == AlphaChip_Memory.g_WAKE_UP_STS['non']:
        Tkinter_Display_Start.non_text.configure(bg = 'green')
    elif AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] == AlphaChip_Memory.g_WAKE_UP_STS['Power_On_setting']:
        Tkinter_Display_Start.Power_On_setting_text.configure(bg = 'green')
    elif AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] == AlphaChip_Memory.g_WAKE_UP_STS['_Low_Gain_setting']:
        Tkinter_Display_Start.Low_Gain_setting_text.configure(bg = 'green')
    elif AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] == AlphaChip_Memory.g_WAKE_UP_STS['_High_Gain_setting']:
        Tkinter_Display_Start.High_Gain_setting_text.configure(bg = 'green')
    elif AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] == AlphaChip_Memory.g_WAKE_UP_STS['_Raw_Gain_setting']:
        Tkinter_Display_Start.Raw_Gain_setting_text.configure(bg = 'green')
        
    Tkinter_Display_Start.Power_On_text.configure(bg = 'gray')
    Tkinter_Display_Start.Stand_By_text.configure(bg = 'gray')
    Tkinter_Display_Start.Watch_text.configure(bg = 'gray')
    Tkinter_Display_Start.Low_Recheck_text.configure(bg = 'gray')
    Tkinter_Display_Start.LED_On_text.configure(bg = 'gray')
    Tkinter_Display_Start.Active_1_text.configure(bg = 'gray')
    Tkinter_Display_Start.Active_2_text.configure(bg = 'gray')
    Tkinter_Display_Start.Recheck_text.configure(bg = 'gray')
    if AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['POWER_ON_MODE']:
        Tkinter_Display_Start.Power_On_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['STAND_BY_MODE']:
        Tkinter_Display_Start.Stand_By_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['WATCH_MODE']:
        Tkinter_Display_Start.Watch_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LOW_RECHECK_MODE']:
        Tkinter_Display_Start.Low_Recheck_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['LED_ON']:
        Tkinter_Display_Start.LED_On_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['ACTIVE_MODE']:
        Tkinter_Display_Start.Active_1_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['DETECT_MODE']:
        Tkinter_Display_Start.Active_2_text.configure(bg = 'green')
    elif AlphaChip_ISP.g_i_Mode == AlphaChip_Memory.g_N_mode['RECHECK_MODE']:
        Tkinter_Display_Start.Recheck_text.configure(bg = 'green')
        
    # display.Lux_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_STS_REGISTER['_LUX']))
    Tkinter_Display_Start.Illuminanace_text_handle.configure(text = str(AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_data']))
    # display.Resualt_text_handle.configure(text = str(AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta_siganl']))
    # display.Illuminanace_text_handle.configure(text = str(AlphaChip_Memory.g_N_ILLUMINANCE_STS_REGISTER['Illuminance_delta']))
    Tkinter_Display_Start.Resualt_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']))
    
    if AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] == False:
        Tkinter_Display_Start.LED_State_text_handle.configure(text = 'Non', bg = 'gray')
    elif AlphaChip_Memory.g_INT_STS_REGISTER['_PSEUDO_LED_STS'] == True:
        Tkinter_Display_Start.LED_State_text_handle.configure(text = 'ON', bg = 'yellow')
    # elif AlphaChip_Memory.g_INT_STS_REGISTER['LED_STS'] == 2:
    #     display.LED_State_text_handle.configure(text = 'OFF', bg = 'gray')
    
    # if AlphaChip_Memory.g_INT_STS_REGISTER['_Pseudo_STS'] == False:
    #     display.Pseudo_State_text_handle.configure(text = 'Non', bg = 'gray')
    # elif AlphaChip_Memory.g_INT_STS_REGISTER['_Pseudo_STS'] == True:
    #     display.Pseudo_State_text_handle.configure(text = 'ON', bg = 'yellow')
        
    Tkinter_Display_Start.LED_Level_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
        
    for n in range(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']):
        Tkinter_Display_Start.Array_Buffer_text_handle[n].configure(text = str(AlphaChip_Memory.g_b_A_Occupancy_buffer[n]))