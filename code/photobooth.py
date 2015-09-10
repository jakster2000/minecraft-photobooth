from mcpi import minecraft​
import time
import picamera

mc = minecraft.Minecraft.create()

def take_the_pic():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture('selfie.jpg')

def where_am_i():
    while True:
        x, y, z = mc.player.getPos()
           
        time.sleep(3)
        
        if x >= 10.5 and y == 9.0 and z == -44.3:
        #print "You are at the photobooth!"
        
            mc.postToChat("Out Of Service!")
            
