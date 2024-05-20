from tkinter import *
from tkinter.simpledialog import *
import AlphaChip_Memory
from ISP import AlphaChip_ISP_Mode, AlphaChip_ISP_Signal_Clear

def insert_Setting():
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_AMP_GAIN'] = int(insert_Low_Gain_text.get())
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME'] = int(insert_Low_Inttime_text.get())
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL'] = int(insert_Low_Inttime_UD_text.get())
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_AMP_GAIN'] = int(insert_High_Gain_text.get())
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME'] = int(insert_High_Inttime_text.get())
    AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL'] = int(insert_High_Inttime_UD_text.get())
    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN'] = int(insert_Raw_Gain_text.get())
    AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME'] = int(insert_Raw_Inttime_text.get())
    if Option_Var.get() == 'on':
        AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE_AVG'] = True
    elif Option_Var.get() == 'off':
        AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE_AVG'] = False
    AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = True
    # AlphaChip_ISP_Mode.NewFrame()
    
def insert_TP():
    AlphaChip_Memory.g_TP1_REGISTER['_LOW_TP1'] = int(insert_Low_TP1_text.get())
    # AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MIN'] = int(insert_Low_8_TP2_MIN_text.get())
    # AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MAX'] = int(insert_Low_8_TP2_MAX_text.get())
    AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MIN'] = int(insert_Low_16_TP2_MIN_text.get())
    AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MAX'] = int(insert_Low_16_TP2_MAX_text.get())
    AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MIN'] = int(insert_Low_64_TP2_MIN_text.get())
    AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MAX'] = int(insert_Low_64_TP2_MAX_text.get())
    AlphaChip_Memory.g_TP1_REGISTER['_HIGH_TP1'] = int(insert_High_TP1_text.get())
    AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN'] = int(insert_High_64_TP2_MIN_text.get())
    AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX'] = int(insert_High_64_TP2_MAX_text.get())
    # AlphaChip_ISP_Mode.ISP_New_Frame(True)

def insert_output():
    AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT'] = int(insert_Pseudo_Signal_Count_text.get())
    AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH'] = int(insert_Pseudo_Signal_Width_text.get())
    AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH'] = int(insert_Pseudo_Signal_Cycle_text.get())

    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_1'] = int(insert_LED_DIMMING_LEVLE_1_text.get())
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_2'] = int(insert_LED_DIMMING_LEVLE_2_text.get())
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_3'] = int(insert_LED_DIMMING_LEVLE_3_text.get())
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_4'] = int(insert_LED_DIMMING_LEVLE_4_text.get())
    AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_5'] = int(insert_LED_DIMMING_LEVLE_5_text.get())   
    # AlphaChip_ISP_Mode.ISP_New_Frame(True)
    
def Display():
    global PiRA_1_text, PiRA_2_text, SSL_G_1_text, SSL_G_2_text
    global x8_text, x16_text, x64_text
    global CPU_ON_text_handle
    global Low_text, High_text, Raw_text
    global insert_Low_Gain_text, insert_Low_Inttime_text, insert_Low_Inttime_UD_text
    global insert_High_Gain_text, insert_High_Inttime_text, insert_High_Inttime_UD_text
    global insert_Raw_Gain_text, insert_Raw_Inttime_text, Option_Var
    global non_text, Power_On_setting_text, Low_Gain_setting_text, High_Gain_setting_text, Raw_Gain_setting_text
    global Power_On_text, Stand_By_text, Watch_text, Low_Recheck_text, LED_On_text, Active_1_text, Active_2_text, Recheck_text
    global Lux_text_handle, Illuminanace_text_handle, Resualt_text_handle, Array_Buffer_text_handle
    global Pseudo_State_text_handle, LED_State_text_handle, LED_Level_text_handle
    global insert_Low_TP1_text, insert_Low_16_TP2_MIN_text, insert_Low_16_TP2_MAX_text, insert_Low_64_TP2_MIN_text, insert_Low_64_TP2_MAX_text, insert_High_TP1_text, insert_High_64_TP2_MIN_text, insert_High_64_TP2_MAX_text
    global insert_Pseudo_Signal_Count_text, insert_Pseudo_Signal_Width_text, insert_Pseudo_Signal_Cycle_text, insert_LED_DIMMING_LEVLE_1_text, insert_LED_DIMMING_LEVLE_2_text, insert_LED_DIMMING_LEVLE_3_text, insert_LED_DIMMING_LEVLE_4_text, insert_LED_DIMMING_LEVLE_5_text
    
    main_row = 0
    main_col = 0
    Product_row = 0
    Product_col = 0
    CPU_ON_row = 0
    CPU_ON_col = 0
    Scale_row = 0
    Scale_col = 0
    Status_row = 0
    Status_col = 0
    Mode_row = 0
    Mode_col = 0
    Setting_row = 0
    Setting_col = 0
    Resualt_row = 0
    Resualt_col = 0
    OUTPUT_Setting_row = 0
    OUTPUT_Setting_col = 0
    State_row = 0
    State_col = 0
    TP_row = 0
    TP_col = 0
    OUTPUT_row = 0
    OUTPUT_col = 0
    Array_Buffer_text_handle = []
    
    MainWindows = Tk() # 기본 윈도우 생성
    MainWindows.title("Alpha Chip 상태") # 윈도우의 제목 설정
    MainWindows.geometry("+0+550")
    
    Product_group_Frame = Frame(MainWindows)
    Product_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    Product_text = Label(Product_group_Frame, text="Product : ")
    Product_text.grid(row=Product_row,column=Product_col,sticky=N+E+W+S)
    Product_col += 1
    PiRA_1_text = Label(Product_group_Frame, text="PiRA_1")
    PiRA_1_text.grid(row=Product_row,column=Product_col,sticky=N+E+W+S)
    Product_col += 1
    PiRA_2_text = Label(Product_group_Frame, text="PiRA_2")
    PiRA_2_text.grid(row=Product_row,column=Product_col,sticky=N+E+W+S)
    Product_col += 1
    SSL_G_1_text = Label(Product_group_Frame, text="SSL_G_1")
    SSL_G_1_text.grid(row=Product_row,column=Product_col,sticky=N+E+W+S)
    Product_col += 1
    SSL_G_2_text = Label(Product_group_Frame, text="SSL_G_2")
    SSL_G_2_text.grid(row=Product_row,column=Product_col,sticky=N+E+W+S)
    Product_col += 1

    main_col += 1
    Scale_group_Frame = Frame(MainWindows)
    Scale_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    Scale_text = Label(Scale_group_Frame, text="Scale : ")
    Scale_text.grid(row=Scale_row,column=Scale_col,sticky=N+E+W+S)
    Scale_col += 1
    x8_text = Label(Scale_group_Frame, text="8x8")
    x8_text.grid(row=Scale_row,column=Scale_col,sticky=N+E+W+S)
    Scale_col += 1
    x16_text = Label(Scale_group_Frame, text="16x16")
    x16_text.grid(row=Scale_row,column=Scale_col,sticky=N+E+W+S)
    Scale_col += 1
    x64_text = Label(Scale_group_Frame, text="64x64")
    x64_text.grid(row=Scale_row,column=Scale_col,sticky=N+E+W+S)
    
    main_col += 1
    CPU_ON_group_Frame = Frame(MainWindows)
    CPU_ON_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    CPU_ON_text = Label(CPU_ON_group_Frame, text="CPU : ")
    CPU_ON_text.grid(row=CPU_ON_row,column=CPU_ON_col,sticky=N+E+W+S)
    CPU_ON_col += 1
    CPU_ON_text_handle = Label(CPU_ON_group_Frame, text="Non")
    CPU_ON_text_handle.grid(row=CPU_ON_row,column=CPU_ON_col,sticky=N+E+W+S)
    
    main_row += 1
    main_col = 1
    CIS_Status_group_Frame = Frame(MainWindows)
    CIS_Status_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    Status_text = Label(CIS_Status_group_Frame, text="CIS Status : ")
    Status_text.grid(row=Status_row,column=Status_col,sticky=N+E+W+S)
    Status_col += 1
    Low_text = Label(CIS_Status_group_Frame, text="LOW")
    Low_text.grid(row=Status_row,column=Status_col,sticky=N+E+W+S)
    Status_col += 1
    High_text = Label(CIS_Status_group_Frame, text="HIGH")
    High_text.grid(row=Status_row,column=Status_col,sticky=N+E+W+S)
    Status_col += 1
    Raw_text = Label(CIS_Status_group_Frame, text="RAW")
    Raw_text.grid(row=Status_row,column=Status_col,sticky=N+E+W+S)
    
    main_col += 1
    CPU_group_Frame = Frame(MainWindows)
    CPU_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    State_text = Label(CPU_group_Frame, text="CPU State : ")
    State_text.grid(row=State_row,column=State_col,sticky=N+E+W+S)
    State_col += 1
    non_text = Label(CPU_group_Frame, text="non")
    non_text.grid(row=State_row,column=State_col,sticky=N+E+W+S)
    State_col += 1
    Power_On_setting_text = Label(CPU_group_Frame, text="Power_On_setting")
    Power_On_setting_text.grid(row=State_row,column=State_col,sticky=N+E+W+S)
    State_col += 1
    Low_Gain_setting_text = Label(CPU_group_Frame, text="_Low_Gain_setting")
    Low_Gain_setting_text.grid(row=State_row,column=State_col,sticky=N+E+W+S)
    State_col += 1
    High_Gain_setting_text = Label(CPU_group_Frame, text="_High_Gain_setting")
    High_Gain_setting_text.grid(row=State_row,column=State_col,sticky=N+E+W+S)
    State_col += 1
    Raw_Gain_setting_text = Label(CPU_group_Frame, text="_Raw_Gain_setting")
    Raw_Gain_setting_text.grid(row=State_row,column=State_col,sticky=N+E+W+S)
    
    main_row += 1
    main_col = 0
    Mode_group_Frame = Frame(MainWindows)
    Mode_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S, columnspan=3)
    Mode_text = Label(Mode_group_Frame, text="Mode : ")
    Mode_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    Power_On_text = Label(Mode_group_Frame, text="Power ON")
    Power_On_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    Stand_By_text = Label(Mode_group_Frame, text="Stand By")
    Stand_By_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    Watch_text = Label(Mode_group_Frame, text="Watch")
    Watch_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    Low_Recheck_text = Label(Mode_group_Frame, text="Low Recheck")
    Low_Recheck_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    LED_On_text = Label(Mode_group_Frame, text="LED On")
    LED_On_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    Active_1_text = Label(Mode_group_Frame, text="Active 1")
    Active_1_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    Active_2_text = Label(Mode_group_Frame, text="Active 2")
    Active_2_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)
    Mode_col += 1
    Recheck_text = Label(Mode_group_Frame, text="ReCheck")
    Recheck_text.grid(row=Mode_row,column=Mode_col,sticky=N+E+W+S)

    main_row += 1
    main_col = 0
    Setting_group_Frame = Frame(MainWindows)
    Setting_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S, columnspan=4)
    Setting_text = Label(Setting_group_Frame, text="Setting ")
    Setting_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    Low_CIS_Setting_text = Label(Setting_group_Frame, text="Low")
    Low_CIS_Setting_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 2
    High_CIS_Setting_text = Label(Setting_group_Frame, text="High")
    High_CIS_Setting_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 2
    Raw_CIS_Setting_text = Label(Setting_group_Frame, text="Raw")
    Raw_CIS_Setting_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_row += 1
    Setting_col = 1
    Low_Gain_text = Label(Setting_group_Frame, text="Gain : ")
    Low_Gain_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_Low_Gain_text = Entry(Setting_group_Frame)
    insert_Low_Gain_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_Low_Gain_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_AMP_GAIN']))
    Setting_col += 1
    High_Gain_text = Label(Setting_group_Frame, text="Gain : ")
    High_Gain_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_High_Gain_text = Entry(Setting_group_Frame)
    insert_High_Gain_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_High_Gain_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_AMP_GAIN']))
    Setting_col += 1
    Raw_Gain_text = Label(Setting_group_Frame, text="Gain : ")
    Raw_Gain_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_Raw_Gain_text = Entry(Setting_group_Frame)
    insert_Raw_Gain_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_Raw_Gain_text.insert(0, str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN']))
    Setting_row += 1
    Setting_col = 1
    Low_Inttime_text = Label(Setting_group_Frame, text="INTTime : ")
    Low_Inttime_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_Low_Inttime_text = Entry(Setting_group_Frame)
    insert_Low_Inttime_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_Low_Inttime_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']))
    Setting_col += 1
    High_Inttime_text = Label(Setting_group_Frame, text="INTTime : ")
    High_Inttime_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_High_Inttime_text = Entry(Setting_group_Frame)
    insert_High_Inttime_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_High_Inttime_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']))
    Setting_col += 1
    Raw_Inttime_text = Label(Setting_group_Frame, text="INTTime : ")
    Raw_Inttime_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_Raw_Inttime_text = Entry(Setting_group_Frame)
    insert_Raw_Inttime_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_Raw_Inttime_text.insert(0, str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME']))
    Setting_row += 1
    Setting_col = 1
    Low_Inttime_UD_text = Label(Setting_group_Frame, text="INTTime U/D : ")
    Low_Inttime_UD_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_Low_Inttime_UD_text = Entry(Setting_group_Frame)
    insert_Low_Inttime_UD_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_Low_Inttime_UD_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL']))
    Setting_col += 1
    High_Inttime_UD_text = Label(Setting_group_Frame, text="INTTime U/D: ")
    High_Inttime_UD_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    insert_High_Inttime_UD_text = Entry(Setting_group_Frame)
    insert_High_Inttime_UD_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    insert_High_Inttime_UD_text.insert(0, str(AlphaChip_Memory.g_N_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL']))
    Setting_col += 1
    CIS_Option_text = Label(Setting_group_Frame, text="CIS AVG : ")
    CIS_Option_text.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_col += 1
    Option_Var = StringVar()
    CIS_Option_Check_Box = Checkbutton(Setting_group_Frame, text="CIS AVG : ", variable=Option_Var, onvalue='on', offvalue='off')
    CIS_Option_Check_Box.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    CIS_Option_Check_Box.deselect()
    Setting_col += 1
    insert_Setting_button = Button(Setting_group_Frame, text="CIS 설정", command=insert_Setting)
    insert_Setting_button.grid(row=Setting_row,column=Setting_col,sticky=N+E+W+S)
    Setting_row += 1
    Setting_col = 1

    main_row += 1
    main_col = 0
    Resualt_group_Frame = Frame(MainWindows)
    Resualt_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    Resualt_text = Label(Resualt_group_Frame, text="Resualt ")
    Resualt_text.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_col += 1
    Lux_text = Label(Resualt_group_Frame, text="Lux : ")
    Lux_text.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_col += 1
    Lux_text_handle = Label(Resualt_group_Frame, text="Non")
    Lux_text_handle.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_row += 1
    Resualt_col = 1
    Illuminanace_text = Label(Resualt_group_Frame, text="Illuminanace : ")
    Illuminanace_text.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_col += 1
    Illuminanace_text_handle = Label(Resualt_group_Frame, text="Non")
    Illuminanace_text_handle.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_row += 1
    Resualt_col = 1
    Resualt_count_text = Label(Resualt_group_Frame, text="Resualt : ")
    Resualt_count_text.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_col += 1
    Resualt_text_handle = Label(Resualt_group_Frame, text="Non")
    Resualt_text_handle.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_row += 1
    Resualt_col = 1
    Buffer_text = Label(Resualt_group_Frame, text="Buffer : ")
    Buffer_text.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
    Resualt_col += 1
    for n in range(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']):
        Buffer_text_handle_temp = Label(Resualt_group_Frame, text=str(n))
        Buffer_text_handle_temp.grid(row=Resualt_row,column=Resualt_col,sticky=N+E+W+S)
        Array_Buffer_text_handle.append(Buffer_text_handle_temp)
        Resualt_col += 1

    main_col += 1
    OUTPUT_Setting_group_Frame = Frame(MainWindows)
    OUTPUT_Setting_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    Pseudo_State_text = Label(OUTPUT_Setting_group_Frame, text="Pseudo_State : ")
    Pseudo_State_text.grid(row=OUTPUT_Setting_row,column=OUTPUT_Setting_col,sticky=N+E+W+S)
    OUTPUT_Setting_col += 1
    Pseudo_State_text_handle = Label(OUTPUT_Setting_group_Frame, text="Non")
    Pseudo_State_text_handle.grid(row=OUTPUT_Setting_row,column=OUTPUT_Setting_col,sticky=N+E+W+S)
    OUTPUT_Setting_row += 1
    OUTPUT_Setting_col = 0
    LED_State_text = Label(OUTPUT_Setting_group_Frame, text="LED_State : ")
    LED_State_text.grid(row=OUTPUT_Setting_row,column=OUTPUT_Setting_col,sticky=N+E+W+S)
    OUTPUT_Setting_col += 1
    LED_State_text_handle = Label(OUTPUT_Setting_group_Frame, text="Non")
    LED_State_text_handle.grid(row=OUTPUT_Setting_row,column=OUTPUT_Setting_col,sticky=N+E+W+S)
    OUTPUT_Setting_col += 1
    LED_Level_text = Label(OUTPUT_Setting_group_Frame, text="LED_Level : ")
    LED_Level_text.grid(row=OUTPUT_Setting_row,column=OUTPUT_Setting_col,sticky=N+E+W+S)
    OUTPUT_Setting_col += 1
    LED_Level_text_handle = Label(OUTPUT_Setting_group_Frame, text="Level")
    LED_Level_text_handle.grid(row=OUTPUT_Setting_row,column=OUTPUT_Setting_col,sticky=N+E+W+S)
    OUTPUT_Setting_row += 1
    OUTPUT_Setting_col = 0
    
    main_row += 1
    main_col = 0
    TP_group_Frame = Frame(MainWindows)
    TP_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    TP_text = Label(TP_group_Frame, text="TP Setting ")
    TP_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    LOW_TP1_text = Label(TP_group_Frame, text="LOW TP1 : ")
    LOW_TP1_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_Low_TP1_text = Entry(TP_group_Frame)
    insert_Low_TP1_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_Low_TP1_text.insert(0, str(AlphaChip_Memory.g_TP1_REGISTER['_LOW_TP1']))
    TP_row += 1
    TP_col = 1
    # Low_8_TP2_MIN_text = Label(TP_group_Frame, text="LOW 8 TP2 MIN : ")
    # Low_8_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    # TP_col += 1
    # insert_Low_8_TP2_MIN_text = Entry(TP_group_Frame)
    # insert_Low_8_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    # insert_Low_8_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MIN']))
    # TP_row += 1
    # TP_col = 1
    # Low_8_TP2_MAX_text = Label(TP_group_Frame, text="LOW 8 TP2 MAX : ")
    # Low_8_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    # TP_col += 1
    # insert_Low_8_TP2_MAX_text = Entry(TP_group_Frame)
    # insert_Low_8_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    # insert_Low_8_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MAX']))
    # TP_row += 1
    # TP_col = 1
    Low_16_TP2_MIN_text = Label(TP_group_Frame, text="LOW 16 TP2 MIN : ")
    Low_16_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_Low_16_TP2_MIN_text = Entry(TP_group_Frame)
    insert_Low_16_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_Low_16_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MIN']))
    TP_row += 1
    TP_col = 1
    Low_16_TP2_MAX_text = Label(TP_group_Frame, text="LOW 16 TP2 MAX : ")
    Low_16_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_Low_16_TP2_MAX_text = Entry(TP_group_Frame)
    insert_Low_16_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_Low_16_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TP2_16_LOW_REGISTER['_LOW_16_TP2_MAX']))
    TP_row += 1
    TP_col = 1
    Low_64_TP2_MIN_text = Label(TP_group_Frame, text="LOW 64 TP2 MIN : ")
    Low_64_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_Low_64_TP2_MIN_text = Entry(TP_group_Frame)
    insert_Low_64_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_Low_64_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MIN']))
    TP_row += 1
    TP_col = 1
    Low_64_TP2_MAX_text = Label(TP_group_Frame, text="LOW 64 TP2 MAX : ")
    Low_64_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_Low_64_TP2_MAX_text = Entry(TP_group_Frame)
    insert_Low_64_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_Low_64_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TP2_64_LOW_REGISTER['_LOW_64_TP2_MAX']))
    TP_row += 1
    TP_col = 1
    High_TP1_text = Label(TP_group_Frame, text="High TP1 : ")
    High_TP1_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_High_TP1_text = Entry(TP_group_Frame)
    insert_High_TP1_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_High_TP1_text.insert(0, str(AlphaChip_Memory.g_TP1_REGISTER['_HIGH_TP1']))
    TP_row += 1
    TP_col = 1
    High_64_TP2_MIN_text = Label(TP_group_Frame, text="High 64 TP2 MIN : ")
    High_64_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_High_64_TP2_MIN_text = Entry(TP_group_Frame)
    insert_High_64_TP2_MIN_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_High_64_TP2_MIN_text.insert(0, str(AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MIN']))
    TP_row += 1
    TP_col = 1
    High_64_TP2_MAX_text = Label(TP_group_Frame, text="HIgh 64 TP2 MAX : ")
    High_64_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    TP_col += 1
    insert_High_64_TP2_MAX_text = Entry(TP_group_Frame)
    insert_High_64_TP2_MAX_text.grid(row=TP_row,column=TP_col,sticky=N+E+W+S)
    insert_High_64_TP2_MAX_text.insert(0, str(AlphaChip_Memory.g_TP2_64_HIGH_REGISTER['_HIGH_64_TP2_MAX']))
    TP_row += 1
    TP_col = 1
    insert_TP_button = Button(TP_group_Frame, text="TP 설정", command=insert_TP)
    insert_TP_button.grid(row=TP_row,column=TP_col,sticky=N+E+W+S, columnspan=2)
    
    main_col += 1
    OUTPUT_group_Frame = Frame(MainWindows)
    OUTPUT_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    OUTPUT_text = Label(OUTPUT_group_Frame, text="OUTPUT")
    OUTPUT_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    Pseudo_Signal_Count_text = Label(OUTPUT_group_Frame, text="Pseudo Signal Count : ")
    Pseudo_Signal_Count_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_Pseudo_Signal_Count_text = Entry(OUTPUT_group_Frame)
    insert_Pseudo_Signal_Count_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_Pseudo_Signal_Count_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    Pseudo_Signal_Width_text = Label(OUTPUT_group_Frame, text="Pseudo_Signal_Width : ")
    Pseudo_Signal_Width_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_Pseudo_Signal_Width_text = Entry(OUTPUT_group_Frame)
    insert_Pseudo_Signal_Width_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_Pseudo_Signal_Width_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_PSEDO_WIDTH']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    Pseudo_Signal_Cycle_text = Label(OUTPUT_group_Frame, text="Pseudo_Signal_Cycle : ")
    Pseudo_Signal_Cycle_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_Pseudo_Signal_Cycle_text = Entry(OUTPUT_group_Frame)
    insert_Pseudo_Signal_Cycle_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_Pseudo_Signal_Cycle_text.insert(0, str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    LED_DIMMING_LEVLE_1_text = Label(OUTPUT_group_Frame, text="LED_DIMMING_LEVLE_1 : ")
    LED_DIMMING_LEVLE_1_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_LED_DIMMING_LEVLE_1_text = Entry(OUTPUT_group_Frame)
    insert_LED_DIMMING_LEVLE_1_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_LED_DIMMING_LEVLE_1_text.insert(0, str(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_1']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    LED_DIMMING_LEVLE_2_text = Label(OUTPUT_group_Frame, text="LED_DIMMING_LEVLE_2 : ")
    LED_DIMMING_LEVLE_2_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_LED_DIMMING_LEVLE_2_text = Entry(OUTPUT_group_Frame)
    insert_LED_DIMMING_LEVLE_2_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_LED_DIMMING_LEVLE_2_text.insert(0, str(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_2']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    LED_DIMMING_LEVLE_3_text = Label(OUTPUT_group_Frame, text="LED_DIMMING_LEVLE_3 : ")
    LED_DIMMING_LEVLE_3_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_LED_DIMMING_LEVLE_3_text = Entry(OUTPUT_group_Frame)
    insert_LED_DIMMING_LEVLE_3_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_LED_DIMMING_LEVLE_3_text.insert(0, str(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_3']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    LED_DIMMING_LEVLE_4_text = Label(OUTPUT_group_Frame, text="LED_DIMMING_LEVLE_4 : ")
    LED_DIMMING_LEVLE_4_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_LED_DIMMING_LEVLE_4_text = Entry(OUTPUT_group_Frame)
    insert_LED_DIMMING_LEVLE_4_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_LED_DIMMING_LEVLE_4_text.insert(0, str(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_4']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    LED_DIMMING_LEVLE_5_text = Label(OUTPUT_group_Frame, text="LED_DIMMING_LEVLE_5 : ")
    LED_DIMMING_LEVLE_5_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    OUTPUT_col += 1
    insert_LED_DIMMING_LEVLE_5_text = Entry(OUTPUT_group_Frame)
    insert_LED_DIMMING_LEVLE_5_text.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S)
    insert_LED_DIMMING_LEVLE_5_text.insert(0, str(AlphaChip_Memory.g_LED_DIMMING_LEVEL_SET_REGISTER['DIM_LEVEL_5']))
    OUTPUT_row += 1
    OUTPUT_col = 1
    insert_OUTPUT_button = Button(OUTPUT_group_Frame, text="출력 설정", command=insert_output)
    insert_OUTPUT_button.grid(row=OUTPUT_row,column=OUTPUT_col,sticky=N+E+W+S, columnspan=2)
    
    main_row += 1
    main_col = 0
    Quit_btn = Button(MainWindows, text='종료', command=quit)    # quit는 프로그램을 종료시킨다
    Quit_btn.grid(row=main_row,column=main_col, sticky=N+E+W+S, columnspan=3)
    # 종료버튼 눌렀을 때 카메라도 종료

    MainWindows.mainloop() # GUI 앱 실행