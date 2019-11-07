
import pyvjoy
import time

def electric() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    # ELECTRIC

    time.sleep(0.20)
    wAxisX = 0x8000 #6
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
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    j.set_button(4,1)
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()
     
def narak() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    # ELECTRIC

    time.sleep(0.20)
    wAxisX = 0x8000 #6
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
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    j.set_button(3,1)
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

def soccerkick() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()

    time.sleep(0.20)
    wAxisX = 0x1 #4
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.15)

    j.set_button(3,1)
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

def mashin() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    time.sleep(0.20)
    wAxisX = 0x8000 #6
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
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

    time.sleep(0.3)
    j.set_button(4,1)
    time.sleep(0.03)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    
    j.update()

    time.sleep(0.05)

def getup() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()

    j.set_button(4,1)

    # ELECTRIC



def wave() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    # ELECTRIC

    time.sleep(0.20)
    wAxisX = 0x8000 #6
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
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

 
while(1) :
    key = input('커맨드를 입력하세요 : ')

    print('입력된 커맨드 : ' + key)

    if key == '나락' :
        narak()
    elif key == '초풍' :
        electric()

    elif key == '뻥발' :
        soccerkick()

    elif key == '웨캔마신' :
        mashin()
    
    elif key == '일어나' :
        getup()

    elif key == '웨이브' :
        wave()

    else :
        print('뭐래는거야')
