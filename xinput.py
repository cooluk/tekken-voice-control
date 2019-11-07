
import pyvjoy
import time
#Pythonic API, item-at-a-time

j = pyvjoy.VJoyDevice(1)

#turn button number 15 on
# while(1) :
#     j.set_button(1,1)
#     time.sleep(0.1)
#     j.set_button(1,0)
#     time.sleep(0.1)
#     j.reset()

# j.set_button(2,1)
# j.set_button(2,0)

# j.set_button(3,1)
# j.set_button(3,0)

# j.set_button(4,1)
# j.set_button(4,0)

# j.set_button(5,1)
# j.set_button(5,0)
#Notice the args are (buttonID,state) whereas vJoy's native API is the other way around.


#Set X axis to fully left
#j.set_axis(pyvjoy.HID_USAGE_X, 0x1) #up

#Set X axis to fully right
#j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)
# j.data.lButtons = 19

#Also implemented:

#N
wAxisX = 0x4000 
wAxisY = 0x4000

#UP
wAxisY = 0x1

#DOWN
wAxisY = 0x8000

#LEFT
wAxisX = 0x1

#RIGHT
wAxisX = 0x8000

#LP
btn = 1

#RP
btn = 4

#LK
btn = 2

#RK
btn = 3


wAxisX = 0x4000
wAxisY = 0x4000

j.data.wAxisY = wAxisY
j.data.wAxisX = wAxisX

j.update()


# ELECTRIC
time.sleep(0.20)
wAxisX = 0x8000 #6
#j.data.wAxisY = wAxisY
j.data.wAxisX = wAxisX
j.update()
time.sleep(0.15)

wAxisX = 0x4000
wAxisY = 0x4000 #N
j.data.wAxisY = wAxisY
j.data.wAxisX = wAxisX
j.update()
time.sleep(0.05)

wAxisY = 0x8000 #2
j.data.wAxisY = wAxisY
#j.data.wAxisX = wAxisX
j.update()
time.sleep(0.020)

#wAxisY = 0x8000
wAxisX = 0x8000 #23
#j.data.wAxisY = wAxisY
j.data.wAxisX = wAxisX
j.update()
j.set_button(4,1)
# j.set_button(1,0)
#j.update()
time.sleep(0.05)

wAxisX = 0x4000
wAxisY = 0x4000 #N
j.data.wAxisY = wAxisY
j.data.wAxisX = wAxisX
j.update()
#time.sleep(0.20)





# j.reset()
# j.reset_buttons()
# j.reset_povs()
