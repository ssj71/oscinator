#spencer jacksonTypeError: argument 1 has unexpected type 'NoneType'

# this is where the magic happens
from pythonosc import udp_client

#yeah it's a singleton.
client =  udp_client.SimpleUDPClient("127.0.0.1", 9000)

def initOSC(ui):
    client = udp_client.SimpleUDPClient(ui.url.text(), ui.port.value())

def sendOSC(path, value):
    client.send_message(path,value)

def buton(txt):
    sendOSC(txt.text(),127)
def butoff(txt):
    sendOSC(txt.text(),0)

def slid(txt,sld):
    sendOSC(txt.text(),sld.value())

def setup(ui):
    #buttons
    ui.pushButton.pressed.connect(lambda:buton(ui.push))
    ui.pushButton.released.connect(lambda:butoff(ui.release))

    ui.pushButton_2.pressed.connect(lambda:buton(ui.push2))
    ui.pushButton_2.released.connect(lambda:butoff(ui.release2))

    ui.pushButton_3.pressed.connect(lambda:buton(ui.push3))
    ui.pushButton_3.released.connect(lambda:butoff(ui.release3))

    ui.pushButton_4.pressed.connect(lambda:buton(ui.push4))
    ui.pushButton_4.released.connect(lambda:butoff(ui.release4))

    #sliders
    ui.verticalSlider.valueChanged.connect(lambda:slid(ui.slide,ui.verticalSlider))
    ui.verticalSlider_2.valueChanged.connect(lambda:slid(ui.slide2,ui.verticalSlider_2))
    ui.verticalSlider_3.valueChanged.connect(lambda:slid(ui.slide3,ui.verticalSlider_3))
    ui.verticalSlider_4.valueChanged.connect(lambda:slid(ui.slide4,ui.verticalSlider_4))

    #port config
    ui.url.editingFinished.connect(lambda:initOSC(ui))
    ui.port.valueChanged.connect(lambda:initOSC(ui))
