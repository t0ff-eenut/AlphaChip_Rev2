import numpy as np

g_b_Debugging = True
g_RAW_CAM = True
###############################################################

g_CPU_WAKE_UP_CHECK_TIME = {'1ms' : 1
                            ,'2ms' : 2 
                            ,'3ms' : 3 
                            ,'4ms' : 4 
                            ,'5ms' : 5 
                            ,'6ms' : 6 
                            ,'7ms' : 7 
                            ,'8ms' : 8000 
                            }
# 0x00 R/W R/W
g_CPU_SET_REGISTER = {'CPU_DONE' : False                                                  # CPU의 작업이 끝났을 때 Done을 입력(True) -> CPU의 전원을 차단
                      #,'INT_ENABLE' : False                                              # ISP의 Interrupt를 CPU에서 읽어 들이기 허용 (x)
                      ,'CLEAR_INT_NEW_FRAME' : False                                      # 현재 차영상 Image의 데이터 처리가 완료되었다면 True로 signal 소거
                      ,'CPU_ALWAYS_ON' : False                                            # True라면 CPU가 항시 동작
                      ,'CPU_WAKE_UP_CHECK' : False                                        # CPU가 Booting 되면 True로 기입
                      ,'CPU_WAKE_UP_CHECK_TIME' : g_CPU_WAKE_UP_CHECK_TIME['8ms']         # CPU가 켜졌는지 확인할 타임
                      ,'CLK_OUT_DISABLE' : False                                          # 외부로 CLK 출력
                      ,'GPIO_LED_IN_ENABLE' : False                                       # GPIO를 이용하여 LED 출력 -> 부팅 시 설정
                      ,'GPIO_LED_IN_ON_SEL' : False                                       # GPIO의 입력 신호에 따라 동작 방식 설정 -> False : HIGH 신호에 LED 출력, True : LOW 신호에 LED 출력
                      
                      ,'_CLEAR_INT_LOW_GAIN_SET' : False                                  # LOW CIS 설정이 필요한 경우에서 설정을 완료한 경우 True
                      ,'_CLEAR_INT_HIGH_GAIN_SET' : False                                 # HIGH CIS 설정이 필요한 경우에서 설정을 완료한 경우 True
                      ,'_CLEAR_CHANGE_CIS_SETTING' : False                                # CIS Setting이 완료 되었다면 True
                      ,'CLEAR_INT_LOW_RECHECK_ERROR' : False                              # Recheck Error가 발생하여 CIS Setting 및 TP를 수정하였다면 True하여 Signal을 소거
                      ,'CLEAR_INT_RECHECK_ERROR' : False                                  # Recheck Error가 발생하여 CIS Setting 및 TP를 수정하였다면 True하여 Signal을 소거
                      #,'CLEAR_INT_OTP_MODE' : False                                      # OTP MODE (x)
                      #,'CLEAR_INT_DEBUGGER_MODE' : False                                 # Debugger Mode (x)
                      #,'CLEAR_INT_SCAN_MODE' : False                                     # (x)
                      #,'CLEAR_INT_BIST_MODE' : False                                     # (x)
                      ,'_CLEAR_EXT_STANDBY_MODE' : False                                  # Multi Sensor에서 사용 -> STAND BY Mode로 동작하면 True
                      ,'_CLEAR_EXT_ACTIVE_MODE' : False                                   # Multi Sensor에서 사용 -> ACTIVE Mode로 동작하면 True 
                      }

g_N_SCALE = {'64x64' : 0
             ,'16x16' : 1
             }
g_FRAME_SPEED = {'12FRAME' : int((1 / 12) * 1000000) # 단위 us
                ,'6FRAME' : int((1 / 6) * 1000000)
                ,'4FRAME' : int((1 / 4) * 1000000)
                ,'3FRAME' : int((1 / 3) * 1000000)
                ,'2FRAME' : int((1 / 2) * 1000000)
                ,'1FRAME' : int((1 / 1) * 1000000)
                }
g_N_mode = {'IDLE_MODE' : 0
            ,'POWER_ON_MODE': 1
            ,'STAND_BY_MODE': 2
            ,'WATCH_MODE' : 3
            ,'LOW_RECHECK_MODE' : 4
            ,'LED_ON' : 5
            ,'DETECT_MODE' : 6
            ,'ACTIVE_MODE': 7
            ,'RECHECK_MODE' : 8
          }
g_WAKE_UP_STS = {'non' : 0 
                 ,'Power_On_setting' : 1
                 ,'_Low_Gain_setting' : 2
                 ,'_High_Gain_setting' : 3
                 ,'_Raw_Gain_setting' : 4
                 ,'_TP_Setting' : 5
                 }
g_LED_DIMMING_LEVEL = {'_LED_LEVEL_0' : 0,
                       '_LED_LEVEL_1' : 10,
                       '_LED_LEVEL_2' : 20,
                       '_LED_LEVEL_3' : 30,
                       '_LED_LEVEL_4' : 40,
                       '_LED_LEVEL_5' : 50,
                       '_LED_LEVEL_6' : 60,
                       '_LED_LEVEL_7' : 70,
                       '_LED_LEVEL_8' : 80,
                       '_LED_LEVEL_9' : 90,
                       '_LED_LEVEL_10' : 100
                       }
# 0x04 W R/W
g_FRAME_BUF_STS = {'non' : 0
                   ,'FRAME_BUF 0 R/W' : 1
                   ,'FRAME_BUF 1 R/W' : 2
                   ,'FRAME_BUF 0,1 R/W' : 3
                   }
g_INT_STS_REGISTER = {'INT_ENABLE' : False                                    #
                      ,'FRAME_BUF_STS' : g_FRAME_BUF_STS['non']                 # 현재 사용하는 Frame Buffer Memory -> 0:Buffer_1 1:Buffer_2
                      ,'_PSEUDO_LED_STS' : False                              # 현재 Pseudo Signal, LED Signal 상태를 출력
                      ,'_LED_LEVEL' : 0                                       # 
                      ,'_CHIP_SCALE' : 0                                      #
                      ,'_CHIP_FRAME_SPEED' : 0                                #
                      ,'_CHIP_MODE' : g_N_mode['IDLE_MODE']               # 현재 Chip의 Mode 상태를 표현함
                      ,'_INT_LOW_GAIN_SET' : False                            # LOW INTTIME이 최대 또는 최소일 때 True -> CPU를 부팅하여 GAIN 조절이 필요함
                      ,'_INT_HIGH_GAIN_SET' : False                           # HIGH INTTIME이 최대 또는 최소일 때 True -> CPU를 부팅하여 GAIN 조절이 필요함
                      ,'INT_LOW_RECHECK_ERROR' : False                        # Low Recheck Error가 발생하면 True로 설정                      
                      ,'INT_RECHECK_ERROR' : False                            # Recheck Error가 발생하면 True로 설정
                      #,'INT_OTP_MODE' : False                                # (x)
                      #,'INT_DEBUGGER_MODE' : False                           # (x)
                      #,'INT_SCAN_MODE' : False                               # (x)
                      #,'INT_BIST_MODE' : False                               # (x)
                      ,'_EXT_STANDBY_MODE' : False                            # 외부 Stand By Mode로 전환 Signal이 들어오면 True
                      ,'_EXT_ACTIVE_MODE' : False                             # 외부 Active Mode로 전환 Signal이 들어오면 True
                      ,'WAKE_UP_STS' : g_WAKE_UP_STS['non']                   # CPU의 부팅 이유를 나타냄
                      ,'SIG_STATE_WAIT' : False                               # CIS와 ISP간 통신 중일 때 True
                      ,'INT_NEW_FRAME' : False                                # 
                      ,'_CHANGE_CIS_SETTING' : False                          # CIS Setting이 변경되면 True
                      }

g_N_ILLUMINANCE_STS_REGISTER = {'Illuminance_data' : 0                   # 현재 조도계산 결과 값
                                ,'Illuminance_data_x' : 0                #
                                ##########################################
                                ,'Illuminance_delta_signal' : 0          # 1Bit
                                ,'Illuminance_delta' : 0                 # 8bit
                                ##########################################
                                }

# 0x08 W R/W
g_RESULT_STS_REGISTER = {'Result_data' : 0                       # 현재 Frame - 이전 Frame 차영상 연산 결과 값
                         }

###################################################################################0
# 0x0C R R/W
g_TP1_REGISTER = {'_LOW_TP1' : 0                                  # 저조도용 TP1
                  ,'_HIGH_TP1' : 0                                # 고조도 TP1
                  
                  ####################
                  ,'_LOW_LIGHT_Delta_TH' : 0                      # 8bit
                  ,'_HIGH_LIGHT_Delta_TH' : 0                     # 8bit
                  ####################
                  
                  }

# 0x10 R R/W
g_TP2_16_LOW_REGISTER = {'_LOW_16_TP2_MIN' : 0
                         
                         ,'_LOW_16_TP2_MAX' : 0
                         }

# 0x14 R R/W
g_TP2_64_LOW_REGISTER = {'_LOW_64_TP2_MIN' : 0
                         
                         ,'_LOW_64_TP2_MAX' : 0
                         }

# 0x18 R R/W
g_TP2_64_HIGH_REGISTER = {'_HIGH_64_TP2_MIN' : 0                   # 고조도 64x64 재실 판단
                         
                         ,'_HIGH_64_TP2_MAX' : 0                  # 고조도 64x64 점등, 소등 판단
                  #     ,'_TP2_SET_MARGIN_16' : 0   # 8x8 TP2 Margin
                  #     ,'_TP2_SET_MARGIN_64' : 0   # 8x8 TP2 Margin
                      }
# 0x1C R/W R/W
g_N_CIS_SET_REGISTER = {'_LOW_AMP_GAIN' : 8                       # 저조도 GAIN
                        ,'_LOW_INTEGRATION_TIME' : 100000         # 저조도 INTTIME
                        ,'_LOW_INTEGRATION_TIME_UD_SEL' : 1       # 저조도에서 사용하는 HIGH CIS Setting 사용 중, ISP가 INTTIME을 조절하는 경우에 증감 Step 크기
                        
                        ,'_HIGH_AMP_GAIN' : 2                     # 고조도 GAIN
                        ,'_HIGH_INTEGRATION_TIME' : 25000         # 고조도 INTTIME
                        ,'_HIGH_INTEGRATION_TIME_UD_SEL' : 1      # 고조도에서 사용하는 HIGH CIS Setting 사용 중, ISP가 INTTIME을 조절하는 경우에 증감 Step 크기
                        }

# 0x20 R R/W
g_N_RAW_CIS_SET_REGISTER = {'_RAW_AMP_GAIN' : 4                         # 조도측정용 GAIN
                            ,'_RAW_INTEGRATION_TIME' : 50000            # 조도측정용 INTTIME
                            
                            ,'_ILLUMINANCE_DARK_TH' : 0                 #
                            ,'_DAY_CHACK' : True                              #
                            ,'_ILLUMINANCE_CHECK_TIME' : 0                    #
                            #####################################################
                            # ,'_X_ILLUMINANCE' : 0
                            # ,'_ILLUMINANCE_MARGIN' : 5
                            #####################################################
                            }

# 0x24 R R/W
g_INT_TIME_SET_REGISTER = {'_LOW_INT_MAX' : 100000                # LOW INTTime 최대 값
                           
                           ,'_LOW_INT_MIN' : 700                  # LOW INTTime 최소 값
                           
                           ,'_HIGH_INT_MAX' : 100000              # HIGH INTTime 최대 값
                           
                           ,'_HIGH_INT_MIN' : 700                 # HIGH INTTime 최소 값
                           }

# 0x28 R R/W
g_N_ILLUMINANCE_RANGE_REGISTER = {'_ILLUMINANCE_RANGE_MAX' : 127
                                  ,'_ILLUMINANCE_RANGE_MIN' : 64
                                  }

# 0x2C R R/W
g_FR_CYCLE_REGISTER = {}

# 0x30 R R/W
g_SUS_LED_BIAS_MARGIN_SEL = {'5us' : 5 #us 
                            ,'10us' : 10 #us 
                            ,'20us' : 20 #us 
                            ,'30us' : 30 #us  
                            }
g_SUS_CIS_BIAS_MARGIN_SEL = {'5us' : 5 #us 
                            ,'10us' : 10 #us 
                            ,'20us' : 20 #us 
                            ,'30us' : 30 #us  
                            }
g_N_TARGET = {'PIRA_1' : 0
              ,'PIRA_2' : 1
              ,'SSL_1' : 2
              ,'SSL_2' : 3
              ,'Debug' : 4 # CIS 해상도, LOW-HIGH Setting 변경할 수 있게 하여 결과값을 직접 볼 수 있게 함
              }
g_CIS_DATA_SET_REGISTER = {'OFFSET_PIXEL_DATA' : 0                      # ADC에서 중복으로 카운트 된 개수를 뺌
                           ,'_OFFSET_SIGN' : True
                           ,'_OFFSET_ENABLE' : True
                           ,'SUS_AMP_SEL' : False                       # SUS AMP Signal Option 
                           ,'SUS_LED_BIAS_MARGIN_SEL' : g_SUS_LED_BIAS_MARGIN_SEL['5us']
                           ,'SUS_CIS_BIAS_MARGIN_SEL' : g_SUS_CIS_BIAS_MARGIN_SEL['5us']
                           ,'SEL_PN' : False                            # CIS로부터 데이터를 입력 받을 때, False : negedge, True : Posedge
                           ,'TARGET' : g_N_TARGET['PIRA_1']              # 제품 설정
                           ,'CLK_GATING_EN' : False                     # 클럭 게이팅 사용 여부
                           }

# 0x34 R R/W
g_PIRA_PULSE_REGISTER = {'_PSEDO_WIDTH' : 50                # Pseudo Signal 출력 폭
                         ,'_PSEDO_WIDTH_STEP' : 50          # Pseudo Signal 출력 주기
                         ,'CYCLE_LENGTH' : 700              #
                         ,'_OUTPUT_COUNT' : 1               # Pseudo Signal 출력 횟수
                         ,'SIGNAL_CHECK' : True             # True : Signal을 뿌렸음에도 전등이 점등하지 않았다면 다시 Signal 출력
                         }

# 0x38 R R/W
g_LED_DIMMING_LEVEL_SET_REGISTER = {'DIM_LEVEL_0' : g_LED_DIMMING_LEVEL['_LED_LEVEL_0']
                                    ,'DIM_LEVEL_1' : g_LED_DIMMING_LEVEL['_LED_LEVEL_1']
                                    ,'DIM_LEVEL_2' : g_LED_DIMMING_LEVEL['_LED_LEVEL_3']
                                    ,'DIM_LEVEL_3' : g_LED_DIMMING_LEVEL['_LED_LEVEL_5']
                                    ,'DIM_LEVEL_4' : g_LED_DIMMING_LEVEL['_LED_LEVEL_7']
                                    ,'DIM_LEVEL_5' : g_LED_DIMMING_LEVEL['_LED_LEVEL_10']
                                    ,'DIM_CYCLE_COUNT' : 5
                                    ##############################
                                    ,'_DIM_WAIT_TIME' : 100         # ms
                                    ,'_FLIKER_SPEED' : 1            # s
                                    ,'_FLIKER_COUNT' : 10
                                    ##############################
                                    }

# 0x3C R R/W
g_OUT_PUT_SET_REGISTER = {'PIRA_REG_SEL' : 15
                          ,'SSL_LED_SEL' : 15
                          ,'CPU_CTRL_EN' : False
                          ,'CPU_LED_ON' : False
                          
                          ,'EXT_BUTTON_TIMER' : 1
                          ,'RESET_LED_SEL' : 15
                          }
# 0x40 R R/W
g_N_FRAME_SEL_REGISTER = {'IDLE_MODE' : g_FRAME_SPEED['12FRAME']
                          ,'POWER_ON_MODE' : g_FRAME_SPEED['12FRAME']
                          ,'STAND_BY_MODE' : g_FRAME_SPEED['12FRAME']
                          ,'WATCH_MODE' : g_FRAME_SPEED['12FRAME']
                          ,'LOW_RECHECK_MODE' : g_FRAME_SPEED['12FRAME']
                          ,'LED_ON' : g_FRAME_SPEED['12FRAME']
                          ,'ACTIVE_MODE_1' : g_FRAME_SPEED['12FRAME']
                          ,'ACTIVE_MODE_2' : g_FRAME_SPEED['12FRAME']
                          ,'RECHECK_MODE' : g_FRAME_SPEED['12FRAME']
                          }
# 0x44 R R/W
g_N_TIMER_SET_REGISTER = {'_WATCH_MODE_TIME' : 300
                          ,'_MODE_TIME' : 600
                          
                          ,'_LED_ON_TIME' : 15
                          }
# 0x48 R R/W
g_N_RECHECK_SETTING = {'_RECHECK_COUNT' : 8
                       ,'_OCCUPANCY_ACKNOWIEDGMENT_COUNT' : 0
                       ,'_LOW_RECHECK_ERROR_MAX' : 10
                       ,'_LOW_RECHECK_ERROR_COUNT' : 0
                       ,'_RECHECK_ERROR_MAX' : 10
                       ,'_RECHECK_ERROR_COUNT' : 0
                       ,'_BYPASS_COUNT' : 3
                       ,'_RECHECK_BYPASS_OPTION' : False
                       ############################
                       ,'g_i_big_move_TP2' : 1000
                       ###########################
                       }

# 0x4C R R/W
g_CPU_DATA_1_REGISTER = {}
# 0x50 - R/W
g_CPU_DATA_2_REGISTER = {}
# 0x54 - R/W
g_CPU_DATA_3_REGISTER = {}
# 0x58 - R/W
g_CPU_DATA_4_REGISTER = {}
# 0x5C R R/W
g_CPU_DATA_5_REGISTER = {}
# 0x60 - R/W
g_CPU_DATA_6_REGISTER = {}
# 0x64 - R/W
g_CPU_DATA_7_REGISTER = {}
# 0x68 - R/W
g_CPU_DATA_8_REGISTER = {}

################################################################
g_b_FRAME_SRAM_SW = False
g_F_FRAME_BUFF_64 = np.zeros((2,64,64), np.uint8)
g_F_FRAME_BUFF_16 = np.zeros((2,16,16), np.uint8)
g_F_A_FRAME_BUFF= [g_F_FRAME_BUFF_64, g_F_FRAME_BUFF_16]
g_F_A_FRAME_BUFF_ZERO = [True] * 2

g_b_FRAME_READY = False # ISP에서 사용하는 NewFrame Signal

g_i_illuminance_target = 0
#######################################################################
g_b_A_Illuminance_buffer = [0] * g_N_RECHECK_SETTING['_RECHECK_COUNT']
g_i_Illuminance_buffer_memory_point = 0
g_i_Illuminance_Buffer_delta = 0
g_i_Illuminance_Buffer_avg = 0
######################################################################
g_b_A_Occupancy_buffer = [False] * g_N_RECHECK_SETTING['_RECHECK_COUNT']
g_i_Occupancy_buffer_memory_point = 0


g_Ext_Botton_Push = False

g_CIS_MODE = {'LOW' : 0
              ,'HIGH' : 1
              ,'RAW' : 2}
g_Ext_Light_TH = 20


################