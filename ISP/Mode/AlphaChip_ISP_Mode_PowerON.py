import AlphaChip_Memory
from ISP import AlphaChip_ISP, AlphaChip_ISP_Mode
from CPU import AlphaChip_Firmware
def PowerON():
    if AlphaChip_Memory.g_b_Debugging:
        print()
        print("ISP : MODE : POWER_ON_MODE")   
    AlphaChip_Memory.g_b_change_cis_setting = True                                                           # CIS Setting이 변경 됨
    AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['Power_On_setting']                     # CPU 부팅 이유 표기
    WakeUp_System = AlphaChip_ISP_Mode.threading.Thread(name="WakeUp_System", target=AlphaChip_Firmware.Boot_CPU, daemon=True)
    i_CPU_ON_x_time = g_i_time = AlphaChip_ISP_Mode.time.time() ### Mode 진입 시간
    while True:
        AlphaChip_ISP_Mode.ISP_New_Frame(False)
        g_i_time = AlphaChip_ISP_Mode.time.time()
        if AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_DONE']:
            AlphaChip_ISP_Mode.AlphaChip_ISP_Signal_Clear.clear_signal()
            AlphaChip_Memory.g_INT_STS_REGISTER['WAKE_UP_STS'] = AlphaChip_Memory.g_WAKE_UP_STS['non']                  # CPU가 종료됨을 뜻함
            if AlphaChip_Memory.g_b_Debugging:
                print("ISP : MODE : POWER_ON_MODE : CPU DONE CLEAR")
            ### Stand by Mode 로 전환
            while AlphaChip_Memory.g_INT_STS_REGISTER['SIG_STATE_WAIT']:
                continue
            AlphaChip_ISP.g_i_Mode = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']
            AlphaChip_Memory.g_INT_STS_REGISTER['_CHIP_MODE'] = AlphaChip_Memory.g_N_mode['STAND_BY_MODE']              # STAND BY MODE로 전환
            if WakeUp_System.is_alive():
                WakeUp_System._stop()
            break
        elif not AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK']:
            if g_i_time - i_CPU_ON_x_time > (AlphaChip_Memory.g_CPU_SET_REGISTER['CPU_WAKE_UP_CHECK_TIME'] / 1000) and WakeUp_System.is_alive():
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : POWER_ON_MODE : CPU ON TIME OVER : ", g_i_time - i_CPU_ON_x_time)
                WakeUp_System._stop()
                while WakeUp_System.is_alive():
                    continue
                WakeUp_System.start()
                if AlphaChip_Memory.g_b_Debugging:
                    print("ISP : MODE : WATCH_MODE : CPU Restart")
                i_CPU_ON_x_time = AlphaChip_ISP_Mode.time.time()
            elif not WakeUp_System.is_alive():
                WakeUp_System.start()
                i_CPU_ON_x_time = AlphaChip_ISP_Mode.time.time()
