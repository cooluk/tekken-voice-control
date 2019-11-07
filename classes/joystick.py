import pyvjoy
import time

class Joystick :

    joystickConn = None

    wAxisX = None
    wAxisY = None

    def __init__(self) :
        self.joystickConn = pyvjoy.VJoyDevice(1)

    def setAxis(self, xAxis, yAxis) :
        self.wAxisX = xAxis
        self.wAxisY = yAxis

    def setNutral(self) :
        self.wAxisX = 0x4000
        self.wAxisY = 0x4000

        self.joystickConn.update()

    def setLeft(self) :
        self.wAxisX = 0x1
        self.joystickConn.update()

    def setRight(self) :
        self.wAxisX = 0x8000
        self.joystickConn.update()

    def setUp(self) :
        self.wAxisY = 0x1
        self.joystickConn.update()

    def setDown(self) :
        self.wAxisY = 0x8000
        self.joystickConn.update()
        
    def axisExec(self) :
        self.joystickConn.update()

    def inputBtn(self, btn) :

        btnCode = {'lp' : 1, 'rp' : 4, 'lk' : 2, 'rk' : 3}

        self.joystickConn.set_button(btnCode[btn], 1)



    