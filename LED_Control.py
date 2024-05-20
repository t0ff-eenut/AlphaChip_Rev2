import RPi.GPIO as GPIO
import time
GPIO.cleanup()

# Pseudo 출력을 위한 INIT
g_i_Pseudo_0_OUT_PinNumber = 26  # Pseudo Signal
GPIO.setmode(GPIO.BCM)
GPIO.setup(g_i_Pseudo_0_OUT_PinNumber, GPIO.OUT)     # set 16 pin as output pin

# g_i_Pseudo_0_Controller
try:
    while True:
        GPIO.output(g_i_Pseudo_0_OUT_PinNumber, True)
        time.sleep(3)
        GPIO.output(g_i_Pseudo_0_OUT_PinNumber, False)
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
