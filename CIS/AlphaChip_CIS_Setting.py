import AlphaChip_Memory, display
from CIS import AlphaChip_CIS
def CIS_Gain_Set(i_cis_mode, i_gain_value):
    
    AlphaChip_CIS.g_PICAM_RAW.stop()
    
    if i_cis_mode == AlphaChip_Memory.g_CIS_MODE['LOW']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CIS : Change LOW Gain")
            display.insert_Low_Gain_text.delete(0,10)
            display.insert_Low_Gain_text.insert(0, str(i_gain_value))    
    elif i_cis_mode == AlphaChip_Memory.g_CIS_MODE['HIGH']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CIS : Change HIGH Gain")
            display.insert_High_Gain_text.delete(0,10)
            display.insert_High_Gain_text.insert(0, str(i_gain_value))        
    elif i_cis_mode == AlphaChip_Memory.g_CIS_MODE['RAW']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CIS : Change RAW Gain")
            display.insert_Raw_Gain_text.delete(0,10)
            display.insert_Raw_Gain_text.insert(0, str(i_gain_value))
    AlphaChip_CIS.g_PICAM_RAW.set_controls({"AnalogueGain": int(i_gain_value)})
    
    AlphaChip_CIS.g_PICAM_RAW.start()
    

def CIS_INT_Set(i_cis_mode, i_inttime_value):
    
    AlphaChip_CIS.g_PICAM_RAW.stop()
    
    if i_cis_mode == AlphaChip_Memory.g_CIS_MODE['LOW']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CIS : Change LOW INTTIME")
            display.insert_Low_Inttime_text.delete(0,10)
            display.insert_Low_Inttime_text.insert(0, str(i_inttime_value)) 
    elif i_cis_mode == AlphaChip_Memory.g_CIS_MODE['HIGH']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CIS : Change HIGH INTTIME")
            display.insert_High_Inttime_text.delete(0,10)
            display.insert_High_Inttime_text.insert(0, str(i_inttime_value)) 
    elif i_cis_mode == AlphaChip_Memory.g_CIS_MODE['RAW']:
        if AlphaChip_Memory.g_b_Debugging:
            print("CIS : Change RAW INTTIME")
            display.insert_Raw_Inttime_text.delete(0,10)
            display.insert_Raw_Inttime_text.insert(0, str(i_inttime_value)) 
    AlphaChip_CIS.g_PICAM_RAW.set_controls({"ExposureTime": int(i_inttime_value)})
    
    AlphaChip_CIS.g_PICAM_RAW.start()
    
    
def CIS_Frame_Set(i_frame_speed):
    
    AlphaChip_CIS.g_PICAM_RAW.stop()
    
    if AlphaChip_Memory.g_b_Debugging:
        print("CIS : Change Frame Speed") 
    AlphaChip_CIS.g_PICAM_RAW.set_controls({"FrameDurationLimits": (int(i_frame_speed),0)})
    
    AlphaChip_CIS.g_PICAM_RAW.start()
    
    
