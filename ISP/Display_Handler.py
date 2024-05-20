import tkinter_Display
import AlphaChip_Memory


def Handler():
    


    # # tkinter_display.product_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET['TARGET']))
    target_name = ["PiRA_1", "PiRA_2", "SSL_1", "SSL_2", "Debug"]
    mode_name = ["Power_ON", "Standby", "Occupancy_Check", "Low_Recheck", "Active", "High_Recheck", "LED_ON", "LED_Dimming", "LED_Dimming_Recheck", "LED_OFF"]
    scale_name = ["64x64", "32x32", "16x16", "8x8"]    
    tkinter_Display.CPU_DONE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE']))
    tkinter_Display.INT_ENABLE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['INT_ENABLE']))
    tkinter_Display.CLEAR_INT_NEW_FRAME_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NEW_FRAME']))
    tkinter_Display.CLEAR_INT_AREA_CHECK_ON_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_AREA_CHECK_ON']))
    tkinter_Display.CLEAR_INT_AREA_CHECK_OFF_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_AREA_CHECK_OFF']))
    tkinter_Display.CLEAR_INT_RECHECK_ERROR_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_RECHECK_ERROR']))
    tkinter_Display.CLEAR_INT_LED_SET_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_LED_SET']))
    tkinter_Display.CPU_ALWAYS_ON_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_ALWAYS_ON']))
    tkinter_Display.CLEAR_INT_WATCH_GAIN_SET_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_WATCH_GAIN_SET']))
    tkinter_Display.CLEAR_INT_NORMAL_GAIN_SET_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NORMAL_GAIN_SET']))
    tkinter_Display.CLEAR_INT_OTP_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_OTP_MODE']))
    tkinter_Display.CLEAR_INT_DEBUGGER_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_DEBUGGER_MODE']))
    tkinter_Display.CLEAR_INT_SCAN_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_SCAN_MODE']))
    tkinter_Display.CLEAR_INT_BIST_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_BIST_MODE']))
    tkinter_Display.CLK_OUT_DISABLE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CLK_OUT_DISABLE']))
    tkinter_Display.CPU_WAKE_UP_CHECK_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']))
    tkinter_Display.CPU_WAKE_UP_CHECK_TIME_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME']))
    tkinter_Display.GPIO_LED_IN_ENABLE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['GPIO_LED_IN_ENABLE']))
    tkinter_Display.GPIO_LED_IN_ON_SEL_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['GPIO_LED_IN_ON_SEL']))
    tkinter_Display.CLEAR_EXT_STANDBY_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_EXT_STANDBY_MODE']))
    tkinter_Display.CLEAR_EXT_ACTIVE_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_EXT_ACTIVE_MODE']))
    tkinter_Display.CLEAR_CHANGE_CIS_SETTING_text_handle.configure(text = str(AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_CHANGE_CIS_SETTING']))
    
    tkinter_Display.FRAME_BUF_STS_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['FRAME_BUF_STS']))
    tkinter_Display.LED_STS_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['LED_STS']))
    tkinter_Display.INT_NEW_FRAME_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME']))
    tkinter_Display.INT_AREA_CHECK_ON_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_AREA_CHECK_ON']))
    tkinter_Display.INT_AREA_CHECK_OFF_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_AREA_CHECK_OFF']))
    tkinter_Display.INT_RECHECK_ERROR_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_RECHECK_ERROR']))
    tkinter_Display.WAKE_UP_STS_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS']))
    tkinter_Display.SIG_STATE_WAIT_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']))
    tkinter_Display.INT_LED_SET_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_LED_SET']))
    tkinter_Display.INT_WATCH_GAIN_SET_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_WATCH_GAIN_SET']))
    tkinter_Display.INT_NORMAL_GAIN_SET_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_NORMAL_GAIN_SET']))
    tkinter_Display.INT_OTP_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_OTP_MODE']))
    tkinter_Display.INT_DEBUGGER_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_DEBUGGER_MODE']))
    tkinter_Display.INT_SCAN_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_SCAN_MODE']))
    tkinter_Display.INT_BIST_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['INT_BIST_MODE']))
    tkinter_Display.CHIP_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE']))
    tkinter_Display.EXT_STANDBY_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_STANDBY_MODE']))
    tkinter_Display.EXT_ACTIVE_MODE_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_EXT_ACTIVE_MODE']))
    tkinter_Display.CHANGE_CIS_SETTING_text_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING']))
    tkinter_Display.LED_LEVEL_handle.configure(text = str(AlphaChip_Memory.g_INT_STS_REGISTER['_LED_LEVEL']))
    
    
    tkinter_Display.Illuminance_data_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_STS_REGISTER['Illuminance_data']))
    tkinter_Display.Result_data_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_STS_REGISTER['Result_data']))
    tkinter_Display.LUX_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_STS_REGISTER['_LUX']))
    
    tkinter_Display.start_line_num_new_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['start_line_num_new']))
    tkinter_Display.line_count_new_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['line_count_new']))
    tkinter_Display.start_line_num_old_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['start_line_num_old']))
    tkinter_Display.line_count_old_text_handle.configure(text = str(AlphaChip_Memory.g_RESULT_AREA_REGISTER['line_count_old']))
    
    tkinter_Display.LOW_TP1_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_TP1']))
    tkinter_Display.LOW_8_TP2_MIN_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MIN']))
    tkinter_Display.LOW_8_TP2_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_8_TP2_MAX']))
    tkinter_Display.LOW_64_TP2_MIN_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_64_TP2_MIN']))
    tkinter_Display.LOW_64_TP2_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_LOW_64_TP2_MAX']))
    tkinter_Display.HIGH_TP1_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_TP1']))
    tkinter_Display.HIGH_8_TP2_MIN_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_8_TP2_MIN']))
    tkinter_Display.HIGH_8_TP2_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_8_TP2_MAX']))
    tkinter_Display.HIGH_64_TP2_MIN_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_64_TP2_MIN']))
    tkinter_Display.HIGH_64_TP2_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_TH_DATA_REGISTER['_HIGH_64_TP2_MAX']))
    
    tkinter_Display.HIGH_INTEGRATION_TIME_UD_SEL_text_handle.configure(text = str(AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME_UD_SEL']))
    tkinter_Display.HIGH_INTEGRATION_TIME_text_handle.configure(text = str(AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_INTEGRATION_TIME']))
    tkinter_Display.HIGH_AMP_GAIN_text_handle.configure(text = str(AlphaChip_Memory.g_N_HIGH_CIS_SET_REGISTER['_HIGH_AMP_GAIN']))
    
    tkinter_Display.LOW_INTEGRATION_TIME_UD_SEL_text_handle.configure(text = str(AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME_UD_SEL']))
    tkinter_Display.LOW_INTEGRATION_TIME_text_handle.configure(text = str(AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_INTEGRATION_TIME']))
    tkinter_Display.LOW_AMP_GAIN_text_handle.configure(text = str(AlphaChip_Memory.g_N_LOW_CIS_SET_REGISTER['_LOW_AMP_GAIN']))
    
    tkinter_Display.RAW_INTEGRATION_TIME_text_handle.configure(text = str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_INTEGRATION_TIME']))
    tkinter_Display.RAW_AMP_GAIN_text_handle.configure(text = str(AlphaChip_Memory.g_N_RAW_CIS_SET_REGISTER['_RAW_AMP_GAIN']))
    
    tkinter_Display.OFFSET_PIXEL_DATA_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['OFFSET_PIXEL_DATA']))
    tkinter_Display.SUS_AMP_SEL_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SUS_AMP_SEL']))
    tkinter_Display.SUS_LED_BIAS_MARGIN_SEL_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SUS_LED_BIAS_MARGIN_SEL']))
    tkinter_Display.SUS_CIS_BIAS_MARGIN_SEL_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SUS_CIS_BIAS_MARGIN_SEL']))
    tkinter_Display.TARGET_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['TARGET']))
    tkinter_Display.SEL_PN_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['SEL_PN']))
    tkinter_Display.IR_CHECK_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['IR_CHECK']))
    tkinter_Display.CLK_GATING_EN_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['CLK_GATING_EN']))
    tkinter_Display.SCALE_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE']))
    tkinter_Display.SCALE_AVG_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_SCALE_AVG']))
    tkinter_Display.CIS_SETTING_text_handle.configure(text = str(AlphaChip_Memory.g_CIS_DATA_SET_REGISTER['_CIS_SETTING']))
    
    tkinter_Display.HIGH_INT_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MAX']))
    tkinter_Display.HIGH_INT_MIN_text_handle.configure(text = str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_HIGH_INT_MIN']))
    tkinter_Display.LOW_INT_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MAX']))
    tkinter_Display.LOW_INT_MIN_text_handle.configure(text = str(AlphaChip_Memory.g_INT_TIME_SET_REGISTER['_LOW_INT_MIN']))
    
    tkinter_Display.PSEUDO_R_WIDTH_text_handle.configure(text = str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['PSEUDO_R_WIDTH']))
    tkinter_Display.PSEDO_L_WIDTH_text_handle.configure(text = str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['PSEDO_L_WIDTH']))
    tkinter_Display.CYCLE_LENGTH_text_handle.configure(text = str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['CYCLE_LENGTH']))
    tkinter_Display.SIGNAL_CHECK_text_handle.configure(text = str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['SIGNAL_CHECK']))
    tkinter_Display.OUTPUT_COUNT_text_handle.configure(text = str(AlphaChip_Memory.g_PIRA_PULSE_REGISTER['_OUTPUT_COUNT']))
    
    tkinter_Display.DIM_LEVEL_1_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_1']))
    tkinter_Display.DIM_LEVEL_2_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_2']))
    tkinter_Display.DIM_LEVEL_3_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_3']))
    tkinter_Display.DIM_LEVEL_4_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_4']))
    tkinter_Display.DIM_LEVEL_5_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_LEVEL_5']))
    tkinter_Display.DIM_CYCLE_COUNT_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['DIM_CYCLE_COUNT']))
    tkinter_Display.RECHECK_COUNT_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['RECHECK_COUNT']))
    tkinter_Display.DIM_WAIT_TIME_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_DIM_WAIT_TIME']))
    tkinter_Display.LED_ON_TIME_text_handle.configure(text = str(AlphaChip_Memory.g_DIMMING_LEVEL_SEL_REGISTER['_LED_ON_TIME']))
    
    tkinter_Display.ILLUMINANCE_RANGE_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MAX']))
    tkinter_Display.ILLUMINANCE_RANGE_MIN_text_handle.configure(text = str(AlphaChip_Memory.g_N_ILLUMINANCE_RANGE_REGISTER['_ILLUMINANCE_RANGE_MIN']))
    
    tkinter_Display.Illuminance_DARK_TH_text_handle.configure(text = str(AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['_Illuminance_DARK_TH']))
    tkinter_Display.CHECK_ILL_TH_text_handle.configure(text = str(AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['CHECK_ILL_TH']))
    tkinter_Display.ACCEPT_DELTA_text_handle.configure(text = str(AlphaChip_Memory.g_CHECK_ILL_TH_SET_REGISTER['ACCEPT_DELTA']))
    
    tkinter_Display.RECHECK_COUNT_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_COUNT']))
    tkinter_Display.OCCUPANCY_PERCENT_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_OCCUPANCY_PERCENT']))
    tkinter_Display.RECHECK_BYPASS_OPTION_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_BYPASS_OPTION']))
    tkinter_Display.BYPASS_COUNT_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_BYPASS_COUNT']))
    tkinter_Display.LOW_RECHECK_ERROR_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_MAX']))
    tkinter_Display.LOW_RECHECK_ERROR_COUNT_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_LOW_RECHECK_ERROR_COUNT']))
    tkinter_Display.RECHECK_ERROR_MAX_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_MAX']))
    tkinter_Display.RECHECK_ERROR_COUNT_text_handle.configure(text = str(AlphaChip_Memory.g_N_RECHECK_SETTING['_RECHECK_ERROR_COUNT']))

    