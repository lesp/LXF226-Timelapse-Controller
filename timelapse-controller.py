ffrom picamera import PiCamera
from gpiozero import MCP3008, Button
from time import sleep
from datetime import datetime

pot1 = MCP3008(channel=0)
pot2 = MCP3008(channel=1)
button = Button(17)
camera = PiCamera()

def capture():
    for i in range(timer):
        timestamp = datetime.now().isoformat()
        camera.capture('/home/pi/%s.jpg' % timestamp)
        sleep(delay)
    
camera.start_preview(fullscreen=False, window = (0, 0, 640, 480))
try:
    timer = int(input("How long in minutes should the timelapse run for?"))
    delay = int(input("How long is the delay, in seconds, between shots?"))
    while True:
        brightness = round(pot1.value * 100)
        print("Brightness",brightness)
        contrast = round(pot2.value * 100)
        print("Contrast",contrast)
        camera.brightness = brightness
        camera.contrast = contrast
        settings = "Brightness: "+str(brightness)+" Contrast: "+str(contrast)
        print(settings)
        camera.annotate_text = settings
        sleep(0.1)
        button.when_held = capture
except KeyboardInterrupt:
    camera.stop_preview()
finally:
    print("TIMELAPSE EXITING")
