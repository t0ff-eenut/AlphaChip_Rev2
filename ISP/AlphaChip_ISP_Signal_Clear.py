import AlphaChip_Memory
from CIS import AlphaChip_CIS
def clear_signal():
#while True:
    #print("Clear")
    if AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE'] == True: #
        AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK'] = False
        AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE'] = False

    if AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NEW_FRAME'] == True: #
        AlphaChip_Memory.g_INT_STS_REGISTER['INT_NEW_FRAME'] = False
        AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_NEW_FRAME'] = False

    if AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_RECHECK_ERROR'] == True:
        AlphaChip_Memory.g_INT_STS_REGISTER['INT_RECHECK_ERROR'] = False
        AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_RECHECK_ERROR'] = False

    if AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_INT_LOW_GAIN_SET'] == True:
        AlphaChip_Memory.g_INT_STS_REGISTER['_INT_LOW_GAIN_SET'] = False
        AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_INT_LOW_GAIN_SET'] = False

    if AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_INT_HIGH_GAIN_SET'] == True:
        AlphaChip_Memory.g_INT_STS_REGISTER['_INT_HIGH_GAIN_SET'] = False
        AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_INT_HIGH_GAIN_SET'] = False

    # if AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_OTP_MODE'] == True:
    #     AlphaChip_Memory.g_INT_STS_REGISTER['INT_OTP_MODE'] = False
    #     AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_OTP_MODE'] = False

    # if AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_DEBUGGER_MODE'] == True:
    #     AlphaChip_Memory.g_INT_STS_REGISTER['INT_DEBUGGER_MODE'] = False
    #     AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_DEBUGGER_MODE'] = False

    # if AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_SCAN_MODE'] == True:
    #     AlphaChip_Memory.g_INT_STS_REGISTER['INT_SCAN_MODE'] = False
    #     AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_SCAN_MODE'] = False

    # if AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_BIST_MODE'] == True:
    #     AlphaChip_Memory.g_INT_STS_REGISTER['INT_BIST_MODE'] = False
    #     AlphaChip_Memory.g_CPU_SET_REGISTER['CLEAR_INT_BIST_MODE'] = False

    if AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_CHANGE_CIS_SETTING'] == True:
        AlphaChip_Memory.g_INT_STS_REGISTER['_CHANGE_CIS_SETTING'] = False
        AlphaChip_Memory.g_CPU_SET_REGISTER['_CLEAR_CHANGE_CIS_SETTING'] = False
