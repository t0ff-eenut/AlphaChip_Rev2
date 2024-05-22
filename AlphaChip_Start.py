import AlphaChip_Memory
from CIS import AlphaChip_CIS
from ISP import AlphaChip_ISP, AlphaChip_ISP_LED, AlphaChip_ISP_Pseudo, AlphaChip_ISP_Active_Signal, AlphaChip_ISP_Button

AlphaChip_Memory.g_b_Debugging = True
if AlphaChip_Memory.g_b_Debugging:
    import Tkinter_Display_Start
    import threading
    
def System_Init():

    # LED 출력을 위한 INIT
    LED_Frequancy = 500 #Hz
    AlphaChip_ISP_LED.GPIO.cleanup()
    AlphaChip_ISP_LED.g_i_LED_0_OUT_PinNumber = 12                                                                      # PWM LED
    AlphaChip_ISP_LED.GPIO.setmode(AlphaChip_ISP_LED.GPIO.BCM)
    AlphaChip_ISP_LED.GPIO.setup(AlphaChip_ISP_LED.g_i_LED_0_OUT_PinNumber, AlphaChip_ISP_LED.GPIO.OUT)                 # set 12 pin as LED output pin
    AlphaChip_ISP_LED.g_i_LED_0_Controller = AlphaChip_ISP_LED.GPIO.PWM(AlphaChip_ISP_LED.g_i_LED_0_OUT_PinNumber, LED_Frequancy)
    AlphaChip_ISP_LED.g_i_LED_0_Controller.start(0)
    
    # Pseudo 출력을 위한 INIT
    AlphaChip_ISP_Pseudo.g_i_Pseudo_0_OUT_PinNumber = 16                                                                # Pseudo Signal
    AlphaChip_ISP_Pseudo.GPIO.setmode(AlphaChip_ISP_Pseudo.GPIO.BCM)
    AlphaChip_ISP_Pseudo.GPIO.setup(AlphaChip_ISP_Pseudo.g_i_Pseudo_0_OUT_PinNumber, AlphaChip_ISP_Pseudo.GPIO.OUT)     # set 16 pin as Pseudo output pin
    
    ############################################################################################################ 확인 필요 ########################################################################################################
    # 외부 Active Signal을 위한 INIT
    AlphaChip_ISP_Active_Signal.g_i_Active_Output_PinNumber = 25                                                                            # Active Signal OUT
    AlphaChip_ISP_Active_Signal.GPIO.setmode(AlphaChip_ISP_Active_Signal.GPIO.BCM)
    AlphaChip_ISP_Active_Signal.GPIO.setup(AlphaChip_ISP_Active_Signal.g_i_Active_Output_PinNumber, AlphaChip_ISP_Active_Signal.GPIO.OUT)   # set 25 pin as output pin
    AlphaChip_ISP_Active_Signal.g_i_Active_Input_PinNumber = 24                                                                             # Active Signal IN
    AlphaChip_ISP_Active_Signal.GPIO.setmode(AlphaChip_ISP_Active_Signal.GPIO.BCM)
    AlphaChip_ISP_Active_Signal.GPIO.setup(AlphaChip_ISP_Active_Signal.g_i_Active_Input_PinNumber, AlphaChip_ISP_Active_Signal.GPIO.IN)     # set 24 pin as input pin
    
    AlphaChip_ISP_Button.g_i_Ext_Button_PinNumber = 26                                                                                      # Button Signal IN
    AlphaChip_ISP_Button.GPIO.setmode(AlphaChip_ISP_Button.GPIO.BCM)
    AlphaChip_ISP_Button.GPIO.setup(AlphaChip_ISP_Button.g_i_Ext_Button_PinNumber, AlphaChip_ISP_Button.GPIO.IN)                            # set 23 pin as input pin
    
    ############################################################################################################ 확인 필요 ########################################################################################################

    AlphaChip_ISP_Pseudo.GPIO.output(AlphaChip_ISP_Pseudo.g_i_Pseudo_0_OUT_PinNumber, True)
    AlphaChip_ISP_LED.g_i_LED_0_Controller.ChangeDutyCycle(0)
    
    AlphaChip_CIS.g_Sensor_mode = 2 # HQ카메라 MODE
    if AlphaChip_Memory.g_b_Debugging:
        # GUI_Debug
        display_thread = threading.Thread(name="display_thread", target=Tkinter_Display_Start.Display(), daemon=True)
        display_thread.start()

        print("run")
        
        # OpenCV
        AlphaChip_CIS.cv2.namedWindow("image", AlphaChip_CIS.cv2.WINDOW_NORMAL)
        AlphaChip_CIS.cv2.resizeWindow("image", 480, 480)
        AlphaChip_CIS.cv2.moveWindow("image", 0, 0)
        AlphaChip_CIS.cv2.namedWindow("F_Delta_Frame_W", AlphaChip_CIS.cv2.WINDOW_NORMAL)
        AlphaChip_CIS.cv2.resizeWindow("F_Delta_Frame_W", 480, 480)
        AlphaChip_CIS.cv2.moveWindow("F_Delta_Frame_W", 480, 0)
        AlphaChip_CIS.cv2.startWindowThread()

System_Init()
AlphaChip_Memory.g_b_Camera = True
AlphaChip_CIS.PiCamera_INIT() # HQ 카메라 INIT
AlphaChip_ISP.ISP() # AlphaChip 동작 시작