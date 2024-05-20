import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)
#spi.max_speed_hz=50000 # 50kHz
#    time.sleep(0.0005)
# spi.max_speed_hz=30000000 # 30MHz
spi.max_speed_hz=31200000 # 31.2MHz
#spi.max_speed_hz=15600000 # 15.6MHz

## 버퍼 크기 cat /sys/module/spidev/parameters/bufsiz  ---  4096
######### ######## ######## ######## ######## ######## ######## ######## ########
# 0 # 1 # # 8bit # # 8bit # # 8bit # # 8bit # # 8bit # # 8bit # # 8bit # # 8bit #
######### ######## ######## ######## ######## ######## ######## ######## ########

# 64 x 64 = 8번 전송 * 512

send = []
data = []
receive = []
receive_data = []

equal = False
channel = 0
repeat = 0

# def Equal(data, receive_data):
#     global equal
#     for i in range(0,6,1):
#         if data[i] != receive_data[i]:
#             return False
#     return True

def Data_Creat(number):
    global send
    send = []
    for i in range(64 * number,64 * (number+1),1):
        temp = [i%256]
        #print(type(temp))
        send.extend(temp)



# try:
#     while repeat < 5:
#         for i in range(0, size-2, 1):
#             data[i] += 1
#         send[0] = 0
#         send[1] = 1
#         equal = False
#         for i in range(2, size, 1):
#             send[i] = data[i-2]
#         print("command : ", send[0], send[1], "Pixel_Data : ", send[2], send[3], send[4], send[5], send[6], send[7])
#         spi.writebytes2(send)
#         # #time.sleep(0.001)
#         time.sleep(0.0005)
        
#         while not equal:
#             send = [1,0,0,0,0,0,0,0]
#             print("command : ", send[0], send[1])
#             receive = spi.xfer3(send)
#             print("receive : ", receive)
#             for i in range(2, size, 1):
#                 receive_data[i - 2] = receive[i]
#             print("data : ", data)  
#             print("receive_data : ", receive_data)
#             equal = Equal(data, receive_data)
#             print("equal = ", equal)
#             #time.sleep(1)
#             print()
#         repeat += 1
#     spi.close()
# except KeyboardInterrupt:
#     spi.close()


try:
    start = time.time()
    for i in range(0,int((64*64)/64),1):
    #for i in range(0,4,1):
        # send = [0,0,0,0,0,0,0,1]
        # spi.writebytes2(send)
        # time.sleep(0.044)
        #time.sleep(0.022)
        #time.sleep(0.015)
    #send = [int(i/256),i%56,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256,int(i/256),i%256]
        print(i,"번째")
        Data_Creat(i)
        print("send ", send)
        receive = spi.xfer3(send)
        time.sleep(0.02777)
        print("receive ", receive)
        data = send
    end = time.time()
    print("걸린시간 : ", end - start)
    spi.close()
except KeyboardInterrupt:
    spi.close()