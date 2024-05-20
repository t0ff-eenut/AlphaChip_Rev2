from tkinter import *
from tkinter.simpledialog import *
import AlphaChip_Memory
# g_TP1 = 1
# def insert_TP():
#     global g_TP1
#     g_TP1 = int(insert_TP_text.get())

# g_Save_CSV = False
# def SaveCSV():
#     global g_Save_CSV
#     g_Save_CSV = not g_Save_CSV

def Display():
    global CPU_DONE_text_handle, INT_ENABLE_text_handle, CLEAR_INT_NEW_FRAME_text_handle, CLEAR_INT_AREA_CHECK_ON_text_handle, CLEAR_INT_AREA_CHECK_OFF_text_handle, CLEAR_INT_RECHECK_ERROR_text_handle, CLEAR_INT_LED_SET_text_handle, CPU_ALWAYS_ON_text_handle, CLEAR_INT_WATCH_GAIN_SET_text_handle, CLEAR_INT_NORMAL_GAIN_SET_text_handle, CLEAR_INT_OTP_MODE_text_handle, CLEAR_INT_DEBUGGER_MODE_text_handle, CLEAR_INT_SCAN_MODE_text_handle, CLEAR_INT_BIST_MODE_text_handle, CLK_OUT_DISABLE_text_handle, CPU_WAKE_UP_CHECK_text_handle, CPU_WAKE_UP_CHECK_TIME_text_handle, GPIO_LED_IN_ENABLE_text_handle, GPIO_LED_IN_ON_SEL_text_handle, CLEAR_EXT_STANDBY_MODE_text_handle, CLEAR_EXT_ACTIVE_MODE_text_handle, CLEAR_CHANGE_CIS_SETTING_text_handle
    global FRAME_BUF_STS_text_handle, LED_STS_text_handle, INT_NEW_FRAME_text_handle, INT_AREA_CHECK_ON_text_handle, INT_AREA_CHECK_OFF_text_handle, INT_RECHECK_ERROR_text_handle, WAKE_UP_STS_text_handle, SIG_STATE_WAIT_text_handle, INT_LED_SET_text_handle,INT_WATCH_GAIN_SET_text_handle, INT_NORMAL_GAIN_SET_text_handle,INT_OTP_MODE_text_handle, INT_DEBUGGER_MODE_text_handle, INT_SCAN_MODE_text_handle, INT_BIST_MODE_text_handle, CHIP_MODE_text_handle, EXT_STANDBY_MODE_text_handle, EXT_ACTIVE_MODE_text_handle, CHANGE_CIS_SETTING_text_handle, LED_LEVEL_handle
    global Illuminance_data_text_handle, Result_data_text_handle, LUX_text_handle
    global start_line_num_new_text_handle, line_count_new_text_handle, start_line_num_old_text_handle, line_count_old_text_handle
    global LOW_TP1_text_handle, LOW_8_TP2_MIN_text_handle, LOW_8_TP2_MAX_text_handle, LOW_64_TP2_MIN_text_handle, LOW_64_TP2_MAX_text_handle, HIGH_TP1_text_handle, HIGH_8_TP2_MIN_text_handle, HIGH_8_TP2_MAX_text_handle, HIGH_64_TP2_MIN_text_handle, HIGH_64_TP2_MAX_text_handle
    global HIGH_INTEGRATION_TIME_UD_SEL_text_handle, HIGH_INTEGRATION_TIME_text_handle, HIGH_AMP_GAIN_text_handle
    global LOW_INTEGRATION_TIME_UD_SEL_text_handle, LOW_INTEGRATION_TIME_text_handle, LOW_AMP_GAIN_text_handle
    global RAW_INTEGRATION_TIME_text_handle, RAW_AMP_GAIN_text_handle
    global OFFSET_PIXEL_DATA_text_handle, SUS_AMP_SEL_text_handle, SUS_LED_BIAS_MARGIN_SEL_text_handle, SUS_CIS_BIAS_MARGIN_SEL_text_handle, TARGET_text_handle, SEL_PN_text_handle, IR_CHECK_text_handle, CLK_GATING_EN_text_handle, SCALE_text_handle, SCALE_AVG_text_handle, CIS_SETTING_text_handle
    global HIGH_INT_MAX_text_handle, HIGH_INT_MIN_text_handle, LOW_INT_MAX_text_handle, LOW_INT_MIN_text_handle
    global PSEUDO_R_WIDTH_text_handle, PSEDO_L_WIDTH_text_handle, CYCLE_LENGTH_text_handle, SIGNAL_CHECK_text_handle, OUTPUT_COUNT_text_handle
    global DIM_LEVEL_1_text_handle, DIM_LEVEL_2_text_handle, DIM_LEVEL_3_text_handle, DIM_LEVEL_4_text_handle, DIM_LEVEL_5_text_handle, DIM_CYCLE_COUNT_text_handle, RECHECK_COUNT_text_handle, DIM_WAIT_TIME_text_handle, LED_ON_TIME_text_handle
    global ILLUMINANCE_RANGE_MAX_text_handle, ILLUMINANCE_RANGE_MIN_text_handle
    global Illuminance_DARK_TH_text_handle, CHECK_ILL_TH_text_handle, ACCEPT_DELTA_text_handle
    global RECHECK_COUNT_text_handle, OCCUPANCY_PERCENT_text_handle, RECHECK_BYPASS_OPTION_text_handle, BYPASS_COUNT_text_handle, LOW_RECHECK_ERROR_MAX_text_handle, LOW_RECHECK_ERROR_COUNT_text_handle, RECHECK_ERROR_MAX_text_handle, RECHECK_ERROR_COUNT_text_handle
    
    main_row = 0
    main_col = 0
    registar_group_row = 0
    registar_group_col = 0
    g_CPU_SET_REGISTER_group_row = 0
    g_CPU_SET_REGISTER_group_col = 0
    g_INT_STS_REGISTER_group_row = 0
    g_INT_STS_REGISTER_group_col = 0
    g_RESULT_STS_REGISTER_group_row = 0
    g_RESULT_STS_REGISTER_group_col = 0
    g_RESULT_AREA_REGISTER_group_row = 0
    g_RESULT_AREA_REGISTER_group_col = 0
    g_TH_DATA_REGISTER_group_row = 0
    g_TH_DATA_REGISTER_group_col = 0
    g_N_HIGH_CIS_SET_REGISTER_group_row = 0
    g_N_HIGH_CIS_SET_REGISTER_group_col = 0
    g_N_LOW_CIS_SET_REGISTER_group_row = 0
    g_N_LOW_CIS_SET_REGISTER_group_col = 0
    g_N_RAW_CIS_SET_REGISTER_group_row = 0
    g_N_RAW_CIS_SET_REGISTER_group_col = 0
    g_FR_CYCLE_REGISTER_group_row = 0
    g_FR_CYCLE_REGISTER_group_col = 0
    g_CIS_DATA_SET_REGISTER_group_row = 0
    g_CIS_DATA_SET_REGISTER_group_col = 0
    g_INT_TIME_SET_REGISTER_group_row = 0
    g_INT_TIME_SET_REGISTER_group_col = 0
    g_PIRA_PULSE_REGISTER_group_row = 0
    g_PIRA_PULSE_REGISTER_group_col = 0   
    g_DIMMING_LEVEL_SEL_REGISTER_group_row = 0
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    g_N_ILLUMINANCE_RANGE_REGISTER_group_row = 0
    g_N_ILLUMINANCE_RANGE_REGISTER_group_col = 0
    g_FRAME_SEL_REGISTER_group_row = 0
    g_FRAME_SEL_REGISTER_group_col = 0
    g_LED_OUT_SEL_REGISTER_group_row = 0
    g_LED_OUT_SEL_REGISTER_group_col = 0
    g_LED_HOLD_TIME_REGISTER_group_row = 0
    g_LED_HOLD_TIME_REGISTER_group_col = 0
    g_CHECK_ILL_TH_SET_REGISTER_group_row = 0
    g_CHECK_ILL_TH_SET_REGISTER_group_col = 0
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_row = 0
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_col = 0
    g_CPU_DATA_1_REGISTER_group_row = 0
    g_CPU_DATA_1_REGISTER_group_col = 0
    g_CPU_DATA_2_REGISTER_group_row = 0
    g_CPU_DATA_2_REGISTER_group_col = 0
    g_CPU_DATA_3_REGISTER_group_row = 0
    g_CPU_DATA_3_REGISTER_group_col = 0
    g_CPU_DATA_4_REGISTER_group_row = 0
    g_CPU_DATA_4_REGISTER_group_col = 0
    g_N_RECHECK_SETTING_group_row = 0
    g_N_RECHECK_SETTING_group_col = 0
    
    MainWindows = Tk() # 기본 윈도우 생성
    MainWindows.title("Regestar_Map") # 윈도우의 제목 설정
    # Registar ##################################################
    registar_group_Frame = Frame(MainWindows)
    registar_group_Frame.grid(row=main_row,column=main_col,sticky=N+E+W+S)
    registar_text = Label(registar_group_Frame, text="Registar")
    registar_text.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S)
    ## CPU_SET ##################################################
    registar_group_row += 1
    g_CPU_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_CPU_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=23)
    registar_group_row += 23
    
    CPU_SET_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CPU_SET_REGISTAR")
    CPU_SET_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    
    CPU_DONE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CPU_DONE : ")
    CPU_DONE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CPU_DONE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE']))
    CPU_DONE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    INT_ENABLE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="INT_ENABLE : ")
    INT_ENABLE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    INT_ENABLE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['INT_ENABLE']))
    INT_ENABLE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_NEW_FRAME_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_NEW_FRAME : ")
    CLEAR_INT_NEW_FRAME_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_NEW_FRAME_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NEW_FRAME']))
    CLEAR_INT_NEW_FRAME_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_AREA_CHECK_ON_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_AREA_CHECK_ON : ")
    CLEAR_INT_AREA_CHECK_ON_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_AREA_CHECK_ON_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_AREA_CHECK_ON']))
    CLEAR_INT_AREA_CHECK_ON_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_AREA_CHECK_OFF_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_AREA_CHECK_OFF : ")
    CLEAR_INT_AREA_CHECK_OFF_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_AREA_CHECK_OFF_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_AREA_CHECK_OFF']))
    CLEAR_INT_AREA_CHECK_OFF_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_RECHECK_ERROR_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_RECHECK_ERROR : ")
    CLEAR_INT_RECHECK_ERROR_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_RECHECK_ERROR_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_RECHECK_ERROR']))
    CLEAR_INT_RECHECK_ERROR_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_LED_SET_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_LED_SET : ")
    CLEAR_INT_LED_SET_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_LED_SET_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_LED_SET']))
    CLEAR_INT_LED_SET_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CPU_ALWAYS_ON_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CPU_ALWAYS_ON : ")
    CPU_ALWAYS_ON_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CPU_ALWAYS_ON_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_ALWAYS_ON']))
    CPU_ALWAYS_ON_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_WATCH_GAIN_SET_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_WATCH_GAIN_SET : ")
    CLEAR_INT_WATCH_GAIN_SET_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_WATCH_GAIN_SET_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_WATCH_GAIN_SET']))
    CLEAR_INT_WATCH_GAIN_SET_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_NORMAL_GAIN_SET_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_NORMAL_GAIN_SET : ")
    CLEAR_INT_NORMAL_GAIN_SET_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_NORMAL_GAIN_SET_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NORMAL_GAIN_SET']))
    CLEAR_INT_NORMAL_GAIN_SET_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    
    CLEAR_INT_OTP_MODE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_OTP_MODE : ")
    CLEAR_INT_OTP_MODE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_OTP_MODE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_OTP_MODE']))
    CLEAR_INT_OTP_MODE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_DEBUGGER_MODE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_DEBUGGER_MODE : ")
    CLEAR_INT_DEBUGGER_MODE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_DEBUGGER_MODE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_DEBUGGER_MODE']))
    CLEAR_INT_DEBUGGER_MODE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_SCAN_MODE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_SCAN_MODE : ")
    CLEAR_INT_SCAN_MODE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_SCAN_MODE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_SCAN_MODE']))
    CLEAR_INT_SCAN_MODE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_INT_BIST_MODE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLEAR_INT_BIST_MODE : ")
    CLEAR_INT_BIST_MODE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_INT_BIST_MODE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_BIST_MODE']))
    CLEAR_INT_BIST_MODE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLK_OUT_DISABLE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CLK_OUT_DISABLE : ")
    CLK_OUT_DISABLE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CLK_OUT_DISABLE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLK_OUT_DISABLE']))
    CLK_OUT_DISABLE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CPU_WAKE_UP_CHECK_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CPU_WAKE_UP_CHECK : ")
    CPU_WAKE_UP_CHECK_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CPU_WAKE_UP_CHECK_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']))
    CPU_WAKE_UP_CHECK_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CPU_WAKE_UP_CHECK_TIME_text = Label(g_CPU_SET_REGISTER_group_Frame, text="CPU_WAKE_UP_CHECK_TIME : ")
    CPU_WAKE_UP_CHECK_TIME_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    CPU_WAKE_UP_CHECK_TIME_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME']))
    CPU_WAKE_UP_CHECK_TIME_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    GPIO_LED_IN_ENABLE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="GPIO_LED_IN_ENABLE : ")
    GPIO_LED_IN_ENABLE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    GPIO_LED_IN_ENABLE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['GPIO_LED_IN_ENABLE']))
    GPIO_LED_IN_ENABLE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    GPIO_LED_IN_ON_SEL_text = Label(g_CPU_SET_REGISTER_group_Frame, text="GPIO_LED_IN_ON_SEL : ")
    GPIO_LED_IN_ON_SEL_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_col += 1
    GPIO_LED_IN_ON_SEL_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['GPIO_LED_IN_ON_SEL']))
    GPIO_LED_IN_ON_SEL_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_EXT_STANDBY_MODE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="_CLEAR_EXT_STANDBY_MODE : ")
    CLEAR_EXT_STANDBY_MODE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_EXT_STANDBY_MODE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_EXT_STANDBY_MODE']))
    CLEAR_EXT_STANDBY_MODE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_EXT_ACTIVE_MODE_text = Label(g_CPU_SET_REGISTER_group_Frame, text="_CLEAR_EXT_ACTIVE_MODE : ")
    CLEAR_EXT_ACTIVE_MODE_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_EXT_ACTIVE_MODE_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_EXT_ACTIVE_MODE']))
    CLEAR_EXT_ACTIVE_MODE_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    CLEAR_CHANGE_CIS_SETTING_text = Label(g_CPU_SET_REGISTER_group_Frame, text="_CLEAR_CHANGE_CIS_SETTING : ")
    CLEAR_CHANGE_CIS_SETTING_text.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col)
    g_CPU_SET_REGISTER_group_col += 1
    CLEAR_CHANGE_CIS_SETTING_text_handle = Label(g_CPU_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_CHANGE_CIS_SETTING']))
    CLEAR_CHANGE_CIS_SETTING_text_handle.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_SET_REGISTER_group_row += 1
    g_CPU_SET_REGISTER_group_col = 0
    blank1 = Label(g_CPU_SET_REGISTER_group_Frame, text=" ")
    blank1.grid(row=g_CPU_SET_REGISTER_group_row,column=g_CPU_SET_REGISTER_group_col)
    
    ## CPU_SET ##################################################
    ## INT_STS ##################################################
    registar_group_row += 1
    g_INT_STS_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_INT_STS_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=21)
    # registar_group_row += 20
       
    INT_STS_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_STS_REGISTER")
    INT_STS_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    
    FRAME_BUF_STS_text = Label(g_INT_STS_REGISTER_group_Frame, text="FRAME_BUF_STS : ")
    FRAME_BUF_STS_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    FRAME_BUF_STS_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['FRAME_BUF_STS']))
    FRAME_BUF_STS_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    LED_STS_text = Label(g_INT_STS_REGISTER_group_Frame, text="LED_STS : ")
    LED_STS_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    LED_STS_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['LED_STS']))
    LED_STS_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_NEW_FRAME_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_NEW_FRAME : ")
    INT_NEW_FRAME_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_NEW_FRAME_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME']))
    INT_NEW_FRAME_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_AREA_CHECK_ON_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_AREA_CHECK_ON : ")
    INT_AREA_CHECK_ON_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_AREA_CHECK_ON_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_AREA_CHECK_ON']))
    INT_AREA_CHECK_ON_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_AREA_CHECK_OFF_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_AREA_CHECK_OFF : ")
    INT_AREA_CHECK_OFF_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_AREA_CHECK_OFF_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_AREA_CHECK_OFF']))
    INT_AREA_CHECK_OFF_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_RECHECK_ERROR_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_RECHECK_ERROR_text : ")
    INT_RECHECK_ERROR_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_RECHECK_ERROR_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_RECHECK_ERROR']))
    INT_RECHECK_ERROR_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    WAKE_UP_STS_text = Label(g_INT_STS_REGISTER_group_Frame, text="WAKE_UP_STS : ")
    WAKE_UP_STS_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    WAKE_UP_STS_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS']))
    WAKE_UP_STS_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    SIG_STATE_WAIT_text = Label(g_INT_STS_REGISTER_group_Frame, text="SIG_STATE_WAIT : ")
    SIG_STATE_WAIT_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    SIG_STATE_WAIT_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']))
    SIG_STATE_WAIT_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_LED_SET_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_LED_SET : ")
    INT_LED_SET_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_LED_SET_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_LED_SET']))
    INT_LED_SET_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_WATCH_GAIN_SET_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_WATCH_GAIN_SET : ")
    INT_WATCH_GAIN_SET_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col)
    g_INT_STS_REGISTER_group_col += 1
    INT_WATCH_GAIN_SET_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_WATCH_GAIN_SET']))
    INT_WATCH_GAIN_SET_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    
    INT_NORMAL_GAIN_SET_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_NORMAL_GAIN_SET : ")
    INT_NORMAL_GAIN_SET_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_NORMAL_GAIN_SET_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_NORMAL_GAIN_SET']))
    INT_NORMAL_GAIN_SET_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_OTP_MODE_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_OTP_MODE : ")
    INT_OTP_MODE_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_OTP_MODE_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_OTP_MODE']))
    INT_OTP_MODE_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_DEBUGGER_MODE_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_DEBUGGER_MODE : ")
    INT_DEBUGGER_MODE_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_DEBUGGER_MODE_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_DEBUGGER_MODE']))
    INT_DEBUGGER_MODE_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_SCAN_MODE_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_SCAN_MODE : ")
    INT_SCAN_MODE_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_SCAN_MODE_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_SCAN_MODE']))
    INT_SCAN_MODE_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    INT_BIST_MODE_text = Label(g_INT_STS_REGISTER_group_Frame, text="INT_BIST_MODE : ")
    INT_BIST_MODE_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    INT_BIST_MODE_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_BIST_MODE']))
    INT_BIST_MODE_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    CHIP_MODE_text = Label(g_INT_STS_REGISTER_group_Frame, text="_CHIP_MODE : ")
    CHIP_MODE_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    CHIP_MODE_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE']))
    CHIP_MODE_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    EXT_STANDBY_MODE_text = Label(g_INT_STS_REGISTER_group_Frame, text="_EXT_STANDBY_MODE : ")
    EXT_STANDBY_MODE_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    EXT_STANDBY_MODE_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_STANDBY_MODE']))
    EXT_STANDBY_MODE_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    EXT_ACTIVE_MODE_text = Label(g_INT_STS_REGISTER_group_Frame, text="_EXT_ACTIVE_MODE : ")
    EXT_ACTIVE_MODE_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    EXT_ACTIVE_MODE_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_ACTIVE_MODE']))
    EXT_ACTIVE_MODE_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    CHANGE_CIS_SETTING_text = Label(g_INT_STS_REGISTER_group_Frame, text="_CHANGE_CIS_SETTING : ")
    CHANGE_CIS_SETTING_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_col += 1
    CHANGE_CIS_SETTING_text_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']))
    CHANGE_CIS_SETTING_text_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    LED_LEVEL_text = Label(g_INT_STS_REGISTER_group_Frame, text="_LED_LEVEL : ")
    LED_LEVEL_text.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col)
    g_INT_STS_REGISTER_group_col += 1
    LED_LEVEL_handle = Label(g_INT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
    LED_LEVEL_handle.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_STS_REGISTER_group_row += 1
    g_INT_STS_REGISTER_group_col = 0
    blank2 = Label(g_INT_STS_REGISTER_group_Frame, text=" ")
    blank2.grid(row=g_INT_STS_REGISTER_group_row,column=g_INT_STS_REGISTER_group_col)
    
    ## g_RESULT_STS_REGISTER ##################################################
    registar_group_col += 2
    registar_group_row = 1
    g_RESULT_STS_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_RESULT_STS_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=5)
    registar_group_row += 4
    
    RESULT_STS_text = Label(g_RESULT_STS_REGISTER_group_Frame, text="RESULT_STS_REGISTER")
    RESULT_STS_text.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_STS_REGISTER_group_row += 1
    g_RESULT_STS_REGISTER_group_col = 0
    
    Illuminance_data_text = Label(g_RESULT_STS_REGISTER_group_Frame, text="Illuminance_data : ")
    Illuminance_data_text.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_STS_REGISTER_group_col += 1
    Illuminance_data_text_handle = Label(g_RESULT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_RESULT_STS_REGISTER['Illuminance_data']))
    Illuminance_data_text_handle.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_STS_REGISTER_group_row += 1
    g_RESULT_STS_REGISTER_group_col = 0
    Result_data_text = Label(g_RESULT_STS_REGISTER_group_Frame, text="Result_data : ")
    Result_data_text.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_STS_REGISTER_group_col += 1
    Result_data_text_handle = Label(g_RESULT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']))
    Result_data_text_handle.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_STS_REGISTER_group_row += 1
    g_RESULT_STS_REGISTER_group_col = 0
    LUX_text = Label(g_RESULT_STS_REGISTER_group_Frame, text="_LUX : ")
    LUX_text.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_STS_REGISTER_group_col += 1
    LUX_text_handle = Label(g_RESULT_STS_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_RESULT_STS_REGISTER['_LUX']))
    LUX_text_handle.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_STS_REGISTER_group_row += 1
    g_RESULT_STS_REGISTER_group_col = 0
    blank3 = Label(g_RESULT_STS_REGISTER_group_Frame, text=" ")
    blank3.grid(row=g_RESULT_STS_REGISTER_group_row,column=g_RESULT_STS_REGISTER_group_col)
    
    ## g_AREA_CHECK_SET_REGISTER ##################################################
    registar_group_row += 1
    g_RESULT_AREA_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_RESULT_AREA_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=6)
    registar_group_row += 5
        
    RESULT_AREA_text = Label(g_RESULT_AREA_REGISTER_group_Frame, text="RESULT_AREA_REGISTER")
    RESULT_AREA_text.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_row += 1
    g_RESULT_AREA_REGISTER_group_col = 0
    
    start_line_num_new_text = Label(g_RESULT_AREA_REGISTER_group_Frame, text="start_line_num_new : ")
    start_line_num_new_text.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_col += 1
    start_line_num_new_text_handle = Label(g_RESULT_AREA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['start_line_num_new']))
    start_line_num_new_text_handle.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_row += 1
    g_RESULT_AREA_REGISTER_group_col = 0
    line_count_new_text = Label(g_RESULT_AREA_REGISTER_group_Frame, text="line_count_new : ")
    line_count_new_text.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_col += 1
    line_count_new_text_handle = Label(g_RESULT_AREA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['line_count_new']))
    line_count_new_text_handle.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_row += 1
    g_RESULT_AREA_REGISTER_group_col = 0
    start_line_num_old_text = Label(g_RESULT_AREA_REGISTER_group_Frame, text="start_line_num_old : ")
    start_line_num_old_text.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_col += 1
    start_line_num_old_text_handle = Label(g_RESULT_AREA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['start_line_num_old']))
    start_line_num_old_text_handle.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_row += 1
    g_RESULT_AREA_REGISTER_group_col = 0
    line_count_old_text = Label(g_RESULT_AREA_REGISTER_group_Frame, text="line_count_old : ")
    line_count_old_text.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_col += 1
    line_count_old_text_handle = Label(g_RESULT_AREA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['line_count_old']))
    line_count_old_text_handle.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col,sticky=N+E+W+S)
    g_RESULT_AREA_REGISTER_group_row += 1
    g_RESULT_AREA_REGISTER_group_col = 0
    blank4 = Label(g_RESULT_AREA_REGISTER_group_Frame, text=" ")
    blank4.grid(row=g_RESULT_AREA_REGISTER_group_row,column=g_RESULT_AREA_REGISTER_group_col)
       
    ## g_TH_DATA_REGISTER ##################################################
    registar_group_row += 1
    g_TH_DATA_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_TH_DATA_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=11)
    registar_group_row += 10
        
    TH_DATA_REGISTER_text = Label(g_TH_DATA_REGISTER_group_Frame, text="TH_DATA_REGISTER")
    TH_DATA_REGISTER_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    
    LOW_TP1_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_LOW_TP1 : ")
    LOW_TP1_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    LOW_TP1_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_TP1']))
    LOW_TP1_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    LOW_8_TP2_MIN_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_LOW_8_TP2_MIN : ")
    LOW_8_TP2_MIN_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    LOW_8_TP2_MIN_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MIN']))
    LOW_8_TP2_MIN_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    LOW_8_TP2_MAX_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_LOW_8_TP2_MAX : ")
    LOW_8_TP2_MAX_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    LOW_8_TP2_MAX_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MAX']))
    LOW_8_TP2_MAX_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    LOW_64_TP2_MIN_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_LOW_64_TP2_MIN : ")
    LOW_64_TP2_MIN_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    LOW_64_TP2_MIN_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_64_TP2_MIN']))
    LOW_64_TP2_MIN_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    LOW_64_TP2_MAX_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_LOW_64_TP2_MAX : ")
    LOW_64_TP2_MAX_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    LOW_64_TP2_MAX_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_64_TP2_MAX']))
    LOW_64_TP2_MAX_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    HIGH_TP1_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_HIGH_TP1 : ")
    HIGH_TP1_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    HIGH_TP1_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_TP1']))
    HIGH_TP1_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    HIGH_8_TP2_MIN_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_HIGH_8_TP2_MIN : ")
    HIGH_8_TP2_MIN_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    HIGH_8_TP2_MIN_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_8_TP2_MIN']))
    HIGH_8_TP2_MIN_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    HIGH_8_TP2_MAX_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_HIGH_8_TP2_MAX : ")
    HIGH_8_TP2_MAX_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    HIGH_8_TP2_MAX_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_8_TP2_MAX']))
    HIGH_8_TP2_MAX_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    HIGH_64_TP2_MIN_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_HIGH_64_TP2_MIN : ")
    HIGH_64_TP2_MIN_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    HIGH_64_TP2_MIN_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_64_TP2_MIN']))
    HIGH_64_TP2_MIN_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    HIGH_64_TP2_MAX_text = Label(g_TH_DATA_REGISTER_group_Frame, text="_HIGH_64_TP2_MAX : ")
    HIGH_64_TP2_MAX_text.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_col += 1
    HIGH_64_TP2_MAX_text_handle = Label(g_TH_DATA_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_64_TP2_MAX']))
    HIGH_64_TP2_MAX_text_handle.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col,sticky=N+E+W+S)
    g_TH_DATA_REGISTER_group_row += 1
    g_TH_DATA_REGISTER_group_col = 0
    blank5 = Label(g_RESULT_AREA_REGISTER_group_Frame, text=" ")
    blank5.grid(row=g_TH_DATA_REGISTER_group_row,column=g_TH_DATA_REGISTER_group_col)
    
    ## g_N_HIGH_CIS_SET_REGISTER ##################################################
    registar_group_row += 2
    g_N_HIGH_CIS_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_N_HIGH_CIS_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=4)
    registar_group_row += 3
        
    HIGH_CIS_SET_REGISTER_text = Label(g_N_HIGH_CIS_SET_REGISTER_group_Frame, text="HIGH_CIS_SET_REGISTER")
    HIGH_CIS_SET_REGISTER_text.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_HIGH_CIS_SET_REGISTER_group_row += 1
    g_N_HIGH_CIS_SET_REGISTER_group_col = 0
    
    HIGH_INTEGRATION_TIME_UD_SEL_text = Label(g_N_HIGH_CIS_SET_REGISTER_group_Frame, text="_HIGH_INTEGRATION_TIME_UD_SEL : ")
    HIGH_INTEGRATION_TIME_UD_SEL_text.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_HIGH_CIS_SET_REGISTER_group_col += 1
    HIGH_INTEGRATION_TIME_UD_SEL_text_handle = Label(g_N_HIGH_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL']))
    HIGH_INTEGRATION_TIME_UD_SEL_text_handle.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_HIGH_CIS_SET_REGISTER_group_row += 1
    g_N_HIGH_CIS_SET_REGISTER_group_col = 0
    HIGH_INTEGRATION_TIME_text = Label(g_N_HIGH_CIS_SET_REGISTER_group_Frame, text="_HIGH_INTEGRATION_TIME : ")
    HIGH_INTEGRATION_TIME_text.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_HIGH_CIS_SET_REGISTER_group_col += 1
    HIGH_INTEGRATION_TIME_text_handle = Label(g_N_HIGH_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']))
    HIGH_INTEGRATION_TIME_text_handle.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_HIGH_CIS_SET_REGISTER_group_row += 1
    g_N_HIGH_CIS_SET_REGISTER_group_col = 0
    HIGH_AMP_GAIN_text = Label(g_N_HIGH_CIS_SET_REGISTER_group_Frame, text="_HIGH_AMP_GAIN : ")
    HIGH_AMP_GAIN_text.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_HIGH_CIS_SET_REGISTER_group_col += 1
    HIGH_AMP_GAIN_text_handle = Label(g_N_HIGH_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN']))
    HIGH_AMP_GAIN_text_handle.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_HIGH_CIS_SET_REGISTER_group_row += 1
    g_N_HIGH_CIS_SET_REGISTER_group_col = 0
    blank6 = Label(g_RESULT_AREA_REGISTER_group_Frame, text=" ")
    blank6.grid(row=g_N_HIGH_CIS_SET_REGISTER_group_row,column=g_N_HIGH_CIS_SET_REGISTER_group_col)
    
    ## g_N_LOW_CIS_SET_REGISTER ##################################################
    registar_group_row += 1
    g_N_LOW_CIS_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_N_LOW_CIS_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=4)
    registar_group_row += 3
    
    LOW_CIS_SET_REGISTER_text = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text="LOW_CIS_SET_REGISTER")
    LOW_CIS_SET_REGISTER_text.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_LOW_CIS_SET_REGISTER_group_row += 1
    g_N_LOW_CIS_SET_REGISTER_group_col = 0
    
    LOW_INTEGRATION_TIME_UD_SEL_text = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text="_LOW_INTEGRATION_TIME_UD_SEL : ")
    LOW_INTEGRATION_TIME_UD_SEL_text.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_LOW_CIS_SET_REGISTER_group_col += 1
    LOW_INTEGRATION_TIME_UD_SEL_text_handle = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL']))
    LOW_INTEGRATION_TIME_UD_SEL_text_handle.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_LOW_CIS_SET_REGISTER_group_row += 1
    g_N_LOW_CIS_SET_REGISTER_group_col = 0
    LOW_INTEGRATION_TIME_text = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text="_LOW_INTEGRATION_TIME : ")
    LOW_INTEGRATION_TIME_text.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_LOW_CIS_SET_REGISTER_group_col += 1
    LOW_INTEGRATION_TIME_text_handle = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']))
    LOW_INTEGRATION_TIME_text_handle.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_LOW_CIS_SET_REGISTER_group_row += 1
    g_N_LOW_CIS_SET_REGISTER_group_col = 0
    LOW_AMP_GAIN_text = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text="_LOW_AMP_GAIN : ")
    LOW_AMP_GAIN_text.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_LOW_CIS_SET_REGISTER_group_col += 1
    LOW_AMP_GAIN_text_handle = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN']))
    LOW_AMP_GAIN_text_handle.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_LOW_CIS_SET_REGISTER_group_row += 1
    g_N_LOW_CIS_SET_REGISTER_group_col = 0
    blank7 = Label(g_N_LOW_CIS_SET_REGISTER_group_Frame, text=" ")
    blank7.grid(row=g_N_LOW_CIS_SET_REGISTER_group_row,column=g_N_LOW_CIS_SET_REGISTER_group_col)
    
    ## g_N_RAW_CIS_SET_REGISTER ##################################################
    registar_group_row += 1
    g_N_RAW_CIS_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_N_RAW_CIS_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=3)
    registar_group_row += 2
        
    RAW_CIS_SET_REGISTER_text = Label(g_N_RAW_CIS_SET_REGISTER_group_Frame, text="RAW_CIS_SET_REGISTER")
    RAW_CIS_SET_REGISTER_text.grid(row=g_N_RAW_CIS_SET_REGISTER_group_row,column=g_N_RAW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_RAW_CIS_SET_REGISTER_group_row += 1
    g_N_RAW_CIS_SET_REGISTER_group_col = 0
    
    RAW_INTEGRATION_TIME_text = Label(g_N_RAW_CIS_SET_REGISTER_group_Frame, text="_RAW_INTEGRATION_TIME : ")
    RAW_INTEGRATION_TIME_text.grid(row=g_N_RAW_CIS_SET_REGISTER_group_row,column=g_N_RAW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_RAW_CIS_SET_REGISTER_group_col += 1
    RAW_INTEGRATION_TIME_text_handle = Label(g_N_RAW_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME']))
    RAW_INTEGRATION_TIME_text_handle.grid(row=g_N_RAW_CIS_SET_REGISTER_group_row,column=g_N_RAW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_RAW_CIS_SET_REGISTER_group_row += 1
    g_N_RAW_CIS_SET_REGISTER_group_col = 0
    RAW_AMP_GAIN_text = Label(g_N_RAW_CIS_SET_REGISTER_group_Frame, text="_RAW_AMP_GAIN : ")
    RAW_AMP_GAIN_text.grid(row=g_N_RAW_CIS_SET_REGISTER_group_row,column=g_N_RAW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_RAW_CIS_SET_REGISTER_group_col += 1
    RAW_AMP_GAIN_text_handle = Label(g_N_RAW_CIS_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN']))
    RAW_AMP_GAIN_text_handle.grid(row=g_N_RAW_CIS_SET_REGISTER_group_row,column=g_N_RAW_CIS_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_N_RAW_CIS_SET_REGISTER_group_row += 1
    g_N_RAW_CIS_SET_REGISTER_group_col = 0
    blank8 = Label(g_N_RAW_CIS_SET_REGISTER_group_Frame, text=" ")
    blank8.grid(row=g_N_RAW_CIS_SET_REGISTER_group_row,column=g_N_RAW_CIS_SET_REGISTER_group_col)
    
    ## g_FR_CYCLE_REGISTER ##################################################
    registar_group_row += 1
    g_FR_CYCLE_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_FR_CYCLE_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S)
    
    g_FR_CYCLE_REGISTER_text = Label(g_FR_CYCLE_REGISTER_group_Frame, text="FR_CYCLE_REGISTER")
    g_FR_CYCLE_REGISTER_text.grid(row=g_FR_CYCLE_REGISTER_group_row,column=g_FR_CYCLE_REGISTER_group_col,sticky=N+E+W+S)
    g_FR_CYCLE_REGISTER_group_row += 1
    g_FR_CYCLE_REGISTER_group_col = 0
    
    blank9 = Label(g_FR_CYCLE_REGISTER_group_Frame, text=" ")
    blank9.grid(row=g_FR_CYCLE_REGISTER_group_row,column=g_FR_CYCLE_REGISTER_group_col)
  
    ## g_CIS_DATA_SET_REGISTER ##################################################
    registar_group_col += 2
    registar_group_row = 1
    g_CIS_DATA_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_CIS_DATA_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=11)
    registar_group_row += 10

    CIS_DATA_SET_REGISTER_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="CIS_DATA_SET_REGISTER")
    CIS_DATA_SET_REGISTER_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    
    OFFSET_PIXEL_DATA_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="OFFSET_PIXEL_DATA : ")
    OFFSET_PIXEL_DATA_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    OFFSET_PIXEL_DATA_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['OFFSET_PIXEL_DATA']))
    OFFSET_PIXEL_DATA_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    SUS_AMP_SEL_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="SUS_AMP_SEL : ")
    SUS_AMP_SEL_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    SUS_AMP_SEL_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SUS_AMP_SEL']))
    SUS_AMP_SEL_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    SUS_LED_BIAS_MARGIN_SEL_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="SUS_LED_BIAS_MARGIN_SEL : ")
    SUS_LED_BIAS_MARGIN_SEL_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    SUS_LED_BIAS_MARGIN_SEL_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SUS_LED_BIAS_MARGIN_SEL']))
    SUS_LED_BIAS_MARGIN_SEL_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    SUS_CIS_BIAS_MARGIN_SEL_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="SUS_CIS_BIAS_MARGIN_SEL : ")
    SUS_CIS_BIAS_MARGIN_SEL_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    SUS_CIS_BIAS_MARGIN_SEL_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SUS_CIS_BIAS_MARGIN_SEL']))
    SUS_CIS_BIAS_MARGIN_SEL_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    TARGET_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="TARGET : ")
    TARGET_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    TARGET_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']))
    TARGET_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    SEL_PN_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="SEL_PN : ")
    SEL_PN_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    SEL_PN_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SEL_PN']))
    SEL_PN_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    IR_CHECK_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="IR_CHECK : ")
    IR_CHECK_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    IR_CHECK_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['IR_CHECK']))
    IR_CHECK_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    CLK_GATING_EN_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="CLK_GATING_EN : ")
    CLK_GATING_EN_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    CLK_GATING_EN_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['CLK_GATING_EN']))
    CLK_GATING_EN_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    SCALE_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="_SCALE : ")
    SCALE_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    SCALE_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE']))
    SCALE_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    SCALE_AVG_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="_SCALE_AVG : ")
    SCALE_AVG_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    SCALE_AVG_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE_AVG']))
    SCALE_AVG_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    CIS_SETTING_text = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text="_CIS_SETTING : ")
    CIS_SETTING_text.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_col += 1
    CIS_SETTING_text_handle = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING']))
    CIS_SETTING_text_handle.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CIS_DATA_SET_REGISTER_group_row += 1
    g_CIS_DATA_SET_REGISTER_group_col = 0
    blank10 = Label(g_CIS_DATA_SET_REGISTER_group_Frame, text=" ")
    blank10.grid(row=g_CIS_DATA_SET_REGISTER_group_row,column=g_CIS_DATA_SET_REGISTER_group_col)

    ## g_INT_TIME_SET_REGISTER ##################################################
    registar_group_row += 1
    g_INT_TIME_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_INT_TIME_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=5)
    registar_group_row += 4
        
    INT_TIME_SET_REGISTER_text = Label(g_INT_TIME_SET_REGISTER_group_Frame, text="INT_TIME_SET_REGISTER")
    INT_TIME_SET_REGISTER_text.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_row += 1
    g_INT_TIME_SET_REGISTER_group_col = 0
    
    HIGH_INT_MAX_text = Label(g_INT_TIME_SET_REGISTER_group_Frame, text="_HIGH_INT_MAX : ")
    HIGH_INT_MAX_text.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_col += 1
    HIGH_INT_MAX_text_handle = Label(g_INT_TIME_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MAX']))
    HIGH_INT_MAX_text_handle.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_row += 1
    g_INT_TIME_SET_REGISTER_group_col = 0
    HIGH_INT_MIN_text = Label(g_INT_TIME_SET_REGISTER_group_Frame, text="_HIGH_INT_MIN : ")
    HIGH_INT_MIN_text.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_col += 1
    HIGH_INT_MIN_text_handle = Label(g_INT_TIME_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MIN']))
    HIGH_INT_MIN_text_handle.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_row += 1
    g_INT_TIME_SET_REGISTER_group_col = 0
    LOW_INT_MAX_text = Label(g_INT_TIME_SET_REGISTER_group_Frame, text="_LOW_INT_MAX : ")
    LOW_INT_MAX_text.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_col += 1
    LOW_INT_MAX_text_handle = Label(g_INT_TIME_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MAX']))
    LOW_INT_MAX_text_handle.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_row += 1
    g_INT_TIME_SET_REGISTER_group_col = 0
    LOW_INT_MIN_text = Label(g_INT_TIME_SET_REGISTER_group_Frame, text="_LOW_INT_MIN : ")
    LOW_INT_MIN_text.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_col += 1
    LOW_INT_MIN_text_handle = Label(g_INT_TIME_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MIN']))
    LOW_INT_MIN_text_handle.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_INT_TIME_SET_REGISTER_group_row += 1
    g_INT_TIME_SET_REGISTER_group_col = 0
    blank11 = Label(g_INT_TIME_SET_REGISTER_group_Frame, text=" ")
    blank11.grid(row=g_INT_TIME_SET_REGISTER_group_row,column=g_INT_TIME_SET_REGISTER_group_col)

    ## g_PLSE_IRA_PUREGISTER ##################################################
    registar_group_row += 1
    g_PIRA_PULSE_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_PIRA_PULSE_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=5)
    registar_group_row += 4
        
    PIRA_PULSE_REGISTER_text = Label(g_PIRA_PULSE_REGISTER_group_Frame, text="PIRA_PULSE_REGISTER")
    PIRA_PULSE_REGISTER_text.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_row += 1
    g_PIRA_PULSE_REGISTER_group_col = 0
    
    PSEUDO_R_WIDTH_text = Label(g_PIRA_PULSE_REGISTER_group_Frame, text="PSEUDO_R_WIDTH : ")
    PSEUDO_R_WIDTH_text.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_col += 1
    PSEUDO_R_WIDTH_text_handle = Label(g_PIRA_PULSE_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['PSEUDO_R_WIDTH']))
    PSEUDO_R_WIDTH_text_handle.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_row += 1
    g_PIRA_PULSE_REGISTER_group_col = 0
    PSEDO_L_WIDTH_text = Label(g_PIRA_PULSE_REGISTER_group_Frame, text="PSEDO_L_WIDTH : ")
    PSEDO_L_WIDTH_text.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_col += 1
    PSEDO_L_WIDTH_text_handle = Label(g_PIRA_PULSE_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['PSEDO_L_WIDTH']))
    PSEDO_L_WIDTH_text_handle.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_row += 1
    g_PIRA_PULSE_REGISTER_group_col = 0
    CYCLE_LENGTH_text = Label(g_PIRA_PULSE_REGISTER_group_Frame, text="CYCLE_LENGTH : ")
    CYCLE_LENGTH_text.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_col += 1
    CYCLE_LENGTH_text_handle = Label(g_PIRA_PULSE_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH']))
    CYCLE_LENGTH_text_handle.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_row += 1
    g_PIRA_PULSE_REGISTER_group_col = 0
    SIGNAL_CHECK_text = Label(g_PIRA_PULSE_REGISTER_group_Frame, text="SIGNAL_CHECK : ")
    SIGNAL_CHECK_text.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_col += 1
    SIGNAL_CHECK_text_handle = Label(g_PIRA_PULSE_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['SIGNAL_CHECK']))
    SIGNAL_CHECK_text_handle.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_row += 1
    g_PIRA_PULSE_REGISTER_group_col = 0
    OUTPUT_COUNT_text = Label(g_PIRA_PULSE_REGISTER_group_Frame, text="_OUTPUT_COUNT : ")
    OUTPUT_COUNT_text.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_col += 1
    OUTPUT_COUNT_text_handle = Label(g_PIRA_PULSE_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT']))
    OUTPUT_COUNT_text_handle.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col,sticky=N+E+W+S)
    g_PIRA_PULSE_REGISTER_group_row += 1
    g_PIRA_PULSE_REGISTER_group_col = 0
    blank12 = Label(g_PIRA_PULSE_REGISTER_group_Frame, text=" ")
    blank12.grid(row=g_PIRA_PULSE_REGISTER_group_row,column=g_PIRA_PULSE_REGISTER_group_col)
    
    ## g_DIMMING_LEVEL_SEL_REGISTER ##################################################
    registar_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_DIMMING_LEVEL_SEL_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=10)
    registar_group_row += 9
        
    DIMMING_LEVEL_SEL_REGISTER_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="DIMMING_LEVEL_SEL_REGISTER")
    DIMMING_LEVEL_SEL_REGISTER_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    
    DIM_LEVEL_1_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="DIM_LEVEL_1 : ")
    DIM_LEVEL_1_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    DIM_LEVEL_1_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_1']))
    DIM_LEVEL_1_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    DIM_LEVEL_2_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="DIM_LEVEL_2 : ")
    DIM_LEVEL_2_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    DIM_LEVEL_2_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_2']))
    DIM_LEVEL_2_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    DIM_LEVEL_3_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="DIM_LEVEL_3 : ")
    DIM_LEVEL_3_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    DIM_LEVEL_3_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_3']))
    DIM_LEVEL_3_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    DIM_LEVEL_4_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="DIM_LEVEL_4 : ")
    DIM_LEVEL_4_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    DIM_LEVEL_4_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_4']))
    DIM_LEVEL_4_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    DIM_LEVEL_5_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="DIM_LEVEL_5 : ")
    DIM_LEVEL_5_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    DIM_LEVEL_5_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_5']))
    DIM_LEVEL_5_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    DIM_CYCLE_COUNT_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="DIM_CYCLE_COUNT : ")
    DIM_CYCLE_COUNT_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    DIM_CYCLE_COUNT_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_CYCLE_COUNT']))
    DIM_CYCLE_COUNT_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    RECHECK_COUNT_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="RECHECK_COUNT : ")
    RECHECK_COUNT_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    RECHECK_COUNT_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['RECHECK_COUNT']))
    RECHECK_COUNT_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    # RECHECK_ERR_COUNT_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="RECHECK_ERR_COUNT : ")
    # RECHECK_ERR_COUNT_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    # g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    # RECHECK_ERR_COUNT_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['RECHECK_ERR_COUNT']))
    # RECHECK_ERR_COUNT_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    # g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    # g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    DIM_WAIT_TIME_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="_DIM_WAIT_TIME : ")
    DIM_WAIT_TIME_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    DIM_WAIT_TIME_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME']))
    DIM_WAIT_TIME_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    LED_ON_TIME_text = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text="_LED_ON_TIME : ")
    LED_ON_TIME_text.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_col += 1
    LED_ON_TIME_text_handle = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_LED_ON_TIME']))
    LED_ON_TIME_text_handle.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_DIMMING_LEVEL_SEL_REGISTER_group_row += 1
    g_DIMMING_LEVEL_SEL_REGISTER_group_col = 0
    blank13 = Label(g_DIMMING_LEVEL_SEL_REGISTER_group_Frame, text=" ")
    blank13.grid(row=g_DIMMING_LEVEL_SEL_REGISTER_group_row,column=g_DIMMING_LEVEL_SEL_REGISTER_group_col)
    
    ## g_N_ILLUMINANCE_RANGE_REGISTER ##################################################
    registar_group_row += 1
    g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=3)
    registar_group_row += 2
        
    N_ILLUMINANCE_RANGE_REGISTER_text = Label(g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame, text="N_ILLUMINANCE_RANGE_REGISTER")
    N_ILLUMINANCE_RANGE_REGISTER_text.grid(row=g_N_ILLUMINANCE_RANGE_REGISTER_group_row,column=g_N_ILLUMINANCE_RANGE_REGISTER_group_col,sticky=N+E+W+S)
    g_N_ILLUMINANCE_RANGE_REGISTER_group_row += 1
    g_N_ILLUMINANCE_RANGE_REGISTER_group_col = 0
    
    ILLUMINANCE_RANGE_MAX_text = Label(g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame, text="_ILLUMINANCE_RANGE_MAX : ")
    ILLUMINANCE_RANGE_MAX_text.grid(row=g_N_ILLUMINANCE_RANGE_REGISTER_group_row,column=g_N_ILLUMINANCE_RANGE_REGISTER_group_col,sticky=N+E+W+S)
    g_N_ILLUMINANCE_RANGE_REGISTER_group_col += 1
    ILLUMINANCE_RANGE_MAX_text_handle = Label(g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MAX']))
    ILLUMINANCE_RANGE_MAX_text_handle.grid(row=g_N_ILLUMINANCE_RANGE_REGISTER_group_row,column=g_N_ILLUMINANCE_RANGE_REGISTER_group_col,sticky=N+E+W+S)
    g_N_ILLUMINANCE_RANGE_REGISTER_group_row += 1
    g_N_ILLUMINANCE_RANGE_REGISTER_group_col = 0
    ILLUMINANCE_RANGE_MIN_text = Label(g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame, text="_ILLUMINANCE_RANGE_MIN : ")
    ILLUMINANCE_RANGE_MIN_text.grid(row=g_N_ILLUMINANCE_RANGE_REGISTER_group_row,column=g_N_ILLUMINANCE_RANGE_REGISTER_group_col,sticky=N+E+W+S)
    g_N_ILLUMINANCE_RANGE_REGISTER_group_col += 1
    ILLUMINANCE_RANGE_MIN_text_handle = Label(g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN']))
    ILLUMINANCE_RANGE_MIN_text_handle.grid(row=g_N_ILLUMINANCE_RANGE_REGISTER_group_row,column=g_N_ILLUMINANCE_RANGE_REGISTER_group_col,sticky=N+E+W+S)
    g_N_ILLUMINANCE_RANGE_REGISTER_group_row += 1
    g_N_ILLUMINANCE_RANGE_REGISTER_group_col = 0
    blank14 = Label(g_N_ILLUMINANCE_RANGE_REGISTER_group_Frame, text=" ")
    blank14.grid(row=g_N_ILLUMINANCE_RANGE_REGISTER_group_row,column=g_N_ILLUMINANCE_RANGE_REGISTER_group_col)
    
    ## g_FRAME_SEL_REGISTER ##################################################
    registar_group_row += 1
    g_FRAME_SEL_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_FRAME_SEL_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S)
    
    g_FRAME_SEL_REGISTER_text = Label(g_FRAME_SEL_REGISTER_group_Frame, text="FRAME_SEL_REGISTER")
    g_FRAME_SEL_REGISTER_text.grid(row=g_FRAME_SEL_REGISTER_group_row,column=g_FRAME_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_FRAME_SEL_REGISTER_group_row += 1
    g_FRAME_SEL_REGISTER_group_col = 0
    
    blank15 = Label(g_FRAME_SEL_REGISTER_group_Frame, text=" ")
    blank15.grid(row=g_FRAME_SEL_REGISTER_group_row,column=g_FRAME_SEL_REGISTER_group_col)
    
    ## g_LED_OUT_SEL_REGISTER ##################################################
    registar_group_row += 1
    g_LED_OUT_SEL_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_LED_OUT_SEL_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S)
    
    g_LED_OUT_SEL_REGISTER_text = Label(g_LED_OUT_SEL_REGISTER_group_Frame, text="LED_OUT_SEL_REGISTER")
    g_LED_OUT_SEL_REGISTER_text.grid(row=g_LED_OUT_SEL_REGISTER_group_row,column=g_LED_OUT_SEL_REGISTER_group_col,sticky=N+E+W+S)
    g_LED_OUT_SEL_REGISTER_group_row += 1
    g_LED_OUT_SEL_REGISTER_group_col = 0
    
    blank16 = Label(g_LED_OUT_SEL_REGISTER_group_Frame, text=" ")
    blank16.grid(row=g_LED_OUT_SEL_REGISTER_group_row,column=g_LED_OUT_SEL_REGISTER_group_col)
    
    # g_LED_HOLD_TIME_REGISTER ##################################################
    registar_group_row += 1
    g_LED_HOLD_TIME_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_LED_HOLD_TIME_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S)
    
    g_LED_HOLD_TIME_REGISTER_text = Label(g_LED_HOLD_TIME_REGISTER_group_Frame, text="LED_HOLD_TIME_REGISTER")
    g_LED_HOLD_TIME_REGISTER_text.grid(row=g_LED_HOLD_TIME_REGISTER_group_row,column=g_LED_HOLD_TIME_REGISTER_group_col,sticky=N+E+W+S)
    g_LED_HOLD_TIME_REGISTER_group_row += 1
    g_LED_HOLD_TIME_REGISTER_group_col = 0
    
    blank17 = Label(g_LED_HOLD_TIME_REGISTER_group_Frame, text=" ")
    blank17.grid(row=g_LED_HOLD_TIME_REGISTER_group_row,column=g_LED_HOLD_TIME_REGISTER_group_col)
    
    ## g_CHECK_ILL_TH_SET_REGISTER ##################################################
    registar_group_col += 2
    registar_group_row = 1
    g_CHECK_ILL_TH_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_CHECK_ILL_TH_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=4)
    registar_group_row += 3
        
    CHECK_ILL_TH_SET_REGISTER_text = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text="CHECK_ILL_TH_SET_REGISTER")
    CHECK_ILL_TH_SET_REGISTER_text.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CHECK_ILL_TH_SET_REGISTER_group_row += 1
    g_CHECK_ILL_TH_SET_REGISTER_group_col = 0
    
    Illuminance_DARK_TH_text = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text="_Illuminance_DARK_TH : ")
    Illuminance_DARK_TH_text.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CHECK_ILL_TH_SET_REGISTER_group_col += 1
    Illuminance_DARK_TH_text_handle = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['_Illuminance_DARK_TH']))
    Illuminance_DARK_TH_text_handle.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CHECK_ILL_TH_SET_REGISTER_group_row += 1
    g_CHECK_ILL_TH_SET_REGISTER_group_col = 0
    CHECK_ILL_TH_text = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text="CHECK_ILL_TH : ")
    CHECK_ILL_TH_text.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CHECK_ILL_TH_SET_REGISTER_group_col += 1
    CHECK_ILL_TH_text_handle = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['CHECK_ILL_TH']))
    CHECK_ILL_TH_text_handle.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CHECK_ILL_TH_SET_REGISTER_group_row += 1
    g_CHECK_ILL_TH_SET_REGISTER_group_col = 0
    ACCEPT_DELTA_text = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text="ACCEPT_DELTA : ")
    ACCEPT_DELTA_text.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CHECK_ILL_TH_SET_REGISTER_group_col += 1
    ACCEPT_DELTA_text_handle = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text=str(AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['ACCEPT_DELTA']))
    ACCEPT_DELTA_text_handle.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_CHECK_ILL_TH_SET_REGISTER_group_row += 1
    g_CHECK_ILL_TH_SET_REGISTER_group_col = 0
    blank18 = Label(g_CHECK_ILL_TH_SET_REGISTER_group_Frame, text=" ")
    blank18.grid(row=g_CHECK_ILL_TH_SET_REGISTER_group_row,column=g_CHECK_ILL_TH_SET_REGISTER_group_col)
    
    ## g_RAW_LIGHT_ILL_TIME_SET_REGISTER ##################################################
    registar_group_row += 1
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=1)
    
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_text = Label(g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame, text="RAW_LIGHT_ILL_TIME_SET_REGISTER")
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_text.grid(row=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_row,column=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_row += 1
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_col = 0
    
    blank19 = Label(g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame, text=" ")
    blank19.grid(row=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_row,column=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_col)
    
    ## g_RAW_DARK_ILL_TIME_SET_REGISTER ##################################################
    registar_group_row += 1
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=1)
    
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_text = Label(g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame, text="RAW_LIGHT_ILL_TIME_SET_REGISTER")
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_text.grid(row=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_row,column=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_col,sticky=N+E+W+S)
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_row += 1
    g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_col = 0
    
    blank20 = Label(g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_Frame, text=" ")
    blank20.grid(row=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_row,column=g_RAW_LIGHT_ILL_TIME_SET_REGISTER_group_col)
    
    ## g_CPU_DATA_1_REGISTER ##################################################
    registar_group_row += 1
    g_CPU_DATA_1_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_CPU_DATA_1_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=1)
    
    g_CPU_DATA_1_REGISTER_text = Label(g_CPU_DATA_1_REGISTER_group_Frame, text="CPU_DATA_1_REGISTER")
    g_CPU_DATA_1_REGISTER_text.grid(row=g_CPU_DATA_1_REGISTER_group_row,column=g_CPU_DATA_1_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_DATA_1_REGISTER_group_row += 1
    g_CPU_DATA_1_REGISTER_group_col = 0
    
    blank21 = Label(g_CPU_DATA_1_REGISTER_group_Frame, text=" ")
    blank21.grid(row=g_CPU_DATA_1_REGISTER_group_row,column=g_CPU_DATA_1_REGISTER_group_col)
    
    ## g_CPU_DATA_2_REGISTER ##################################################
    registar_group_row += 2
    g_CPU_DATA_2_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_CPU_DATA_2_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=1)
    
    g_CPU_DATA_2_REGISTER_text = Label(g_CPU_DATA_2_REGISTER_group_Frame, text="CPU_DATA_2_REGISTER")
    g_CPU_DATA_2_REGISTER_text.grid(row=g_CPU_DATA_2_REGISTER_group_row,column=g_CPU_DATA_2_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_DATA_2_REGISTER_group_row += 1
    g_CPU_DATA_2_REGISTER_group_col = 0
    
    blank22 = Label(g_CPU_DATA_2_REGISTER_group_Frame, text=" ")
    blank22.grid(row=g_CPU_DATA_2_REGISTER_group_row,column=g_CPU_DATA_2_REGISTER_group_col)
    
    ## g_CPU_DATA_3_REGISTER ##################################################
    registar_group_row += 2
    g_CPU_DATA_3_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_CPU_DATA_3_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=1)
    
    g_CPU_DATA_3_REGISTER_text = Label(g_CPU_DATA_3_REGISTER_group_Frame, text="CPU_DATA_3_REGISTER")
    g_CPU_DATA_3_REGISTER_text.grid(row=g_CPU_DATA_3_REGISTER_group_row,column=g_CPU_DATA_3_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_DATA_3_REGISTER_group_row += 1
    g_CPU_DATA_3_REGISTER_group_col = 0
    
    blank23 = Label(g_CPU_DATA_3_REGISTER_group_Frame, text=" ")
    blank23.grid(row=g_CPU_DATA_3_REGISTER_group_row,column=g_CPU_DATA_3_REGISTER_group_col)
    
    ## g_CPU_DATA_4_REGISTER ##################################################
    registar_group_row += 2
    g_CPU_DATA_4_REGISTER_group_Frame = Frame(registar_group_Frame)
    g_CPU_DATA_4_REGISTER_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S)
    
    g_CPU_DATA_4_REGISTER_text = Label(g_CPU_DATA_4_REGISTER_group_Frame, text="CPU_DATA_4_REGISTER")
    g_CPU_DATA_4_REGISTER_text.grid(row=g_CPU_DATA_4_REGISTER_group_row,column=g_CPU_DATA_4_REGISTER_group_col,sticky=N+E+W+S)
    g_CPU_DATA_4_REGISTER_group_row += 1
    g_CPU_DATA_4_REGISTER_group_col = 0
    
    blank24 = Label(g_CPU_DATA_4_REGISTER_group_Frame, text=" ")
    blank24.grid(row=g_CPU_DATA_4_REGISTER_group_row,column=g_CPU_DATA_4_REGISTER_group_col)
    
    
    ## g_N_RECHECK_SETTING ##################################################
    registar_group_row += 1
    g_N_RECHECK_SETTING_group_Frame = Frame(registar_group_Frame)
    g_N_RECHECK_SETTING_group_Frame.grid(row=registar_group_row,column=registar_group_col,sticky=N+E+W+S,rowspan=9)
    registar_group_row += 8
        
    N_RECHECK_SETTING_text = Label(g_N_RECHECK_SETTING_group_Frame, text="N_RECHECK_SETTING")
    N_RECHECK_SETTING_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    
    RECHECK_COUNT_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_RECHECK_COUNT : ")
    RECHECK_COUNT_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    RECHECK_COUNT_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']))
    RECHECK_COUNT_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    OCCUPANCY_PERCENT_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_OCCUPANCY_PERCENT : ")
    OCCUPANCY_PERCENT_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    OCCUPANCY_PERCENT_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_OCCUPANCY_PERCENT']))
    OCCUPANCY_PERCENT_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    RECHECK_BYPASS_OPTION_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_RECHECK_BYPASS_OPTION : ")
    RECHECK_BYPASS_OPTION_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    RECHECK_BYPASS_OPTION_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION']))
    RECHECK_BYPASS_OPTION_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    BYPASS_COUNT_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_BYPASS_COUNT : ")
    BYPASS_COUNT_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    BYPASS_COUNT_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_BYPASS_COUNT']))
    BYPASS_COUNT_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    LOW_RECHECK_ERROR_MAX_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_LOW_RECHECK_ERROR_MAX : ")
    LOW_RECHECK_ERROR_MAX_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    LOW_RECHECK_ERROR_MAX_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_MAX']))
    LOW_RECHECK_ERROR_MAX_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    LOW_RECHECK_ERROR_COUNT_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_LOW_RECHECK_ERROR_COUNT : ")
    LOW_RECHECK_ERROR_COUNT_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    LOW_RECHECK_ERROR_COUNT_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT']))
    LOW_RECHECK_ERROR_COUNT_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    RECHECK_ERROR_MAX_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_RECHECK_ERROR_MAX : ")
    RECHECK_ERROR_MAX_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    RECHECK_ERROR_MAX_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_MAX']))
    RECHECK_ERROR_MAX_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    RECHECK_ERROR_COUNT_text = Label(g_N_RECHECK_SETTING_group_Frame, text="_RECHECK_ERROR_COUNT : ")
    RECHECK_ERROR_COUNT_text.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_col += 1
    RECHECK_ERROR_COUNT_text_handle = Label(g_N_RECHECK_SETTING_group_Frame, text=str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_COUNT']))
    RECHECK_ERROR_COUNT_text_handle.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col,sticky=N+E+W+S)
    g_N_RECHECK_SETTING_group_row += 1
    g_N_RECHECK_SETTING_group_col = 0
    blank25 = Label(g_N_RECHECK_SETTING_group_Frame, text=" ")
    blank25.grid(row=g_N_RECHECK_SETTING_group_row,column=g_N_RECHECK_SETTING_group_col)
    
    
    
    

    main_row += 1
    Quit_btn = Button(MainWindows, text='종료', command=quit)    # quit는 프로그램을 종료시킨다
    Quit_btn.grid(row=main_row,column=main_col)
    # 종료버튼 눌렀을 때 카메라도 종료

    MainWindows.mainloop() # GUI 앱 실행
