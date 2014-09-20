##
# @Description : Motion LEAP control used to send commands to Serial. Arduino then reads serial.
#
# @Created : September 2014 By Helen Harman
# @Modified: 20th September 2014
#
##

import sys, time, os
import serial

sys.path.insert(0, "/Users/helen/Documents/MotionLeap/LeapDeveloperKit_2.1.3+21998_mac/LeapSDK/lib")
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Finger

# directions given with cable on left of motion leap
X_AXES = 0
Y_AXES = 1 # motion leap is at 0, move upwards for higher number
Z_AXES = 2 # Screen to 0 to You

ser = serial.Serial('/dev/tty.usbmodem1421', 9600)


##-----------------------------------------------------------------------------------------

class SampleListener(Leap.Listener):
    
    def on_connect(self, controller):
        print "Connected"
        self.previousCommand = ""
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE); # currently unused TODO : flash lights on swipe action.
    
    ##-----------------------------------------------------------------------
    
    def on_frame(self, controller):
        
    	frame = controller.frame()
        self.handleFrame(frame)
    #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
    
    ##-----------------------------------------------------------------------
    
    
    ##
    #
    def handleFrame(self, frame):
        thumb = 0
        finger1 = 0
        finger2 = 0
        finger3 = 0
        finger4 = 0
        tone = 0
        lowestFinger = 100; # if a finger is lower than 100 the piezo will make a sound.

        for finger in frame.fingers:
            if finger.type() == Finger.TYPE_THUMB:
                thumb, tone, lowestFinger = self.handleFinger(finger, tone, lowestFinger)
    
            elif finger.type() == Finger.TYPE_INDEX:
                finger1, tone, lowestFinger = self.handleFinger(finger, tone, lowestFinger)
    
            elif finger.type() == Finger.TYPE_MIDDLE:
                finger2, tone, lowestFinger = self.handleFinger(finger, tone, lowestFinger)
    
            elif finger.type() == Finger.TYPE_RING:
                finger3, tone, lowestFinger = self.handleFinger(finger, tone, lowestFinger)
    
            elif finger.type() == Finger.TYPE_PINKY:
                finger4, tone, lowestFinger = self.handleFinger(finger, tone, lowestFinger)

        ser.flushInput()
        ser.write([thumb, finger1, finger2, finger3, finger4, tone])
        #print ser.readline()
        time.sleep(0.4)
            
    ##-----------------------------------------------------------------------


    ##
    # Gets if the light sound be on and if the piezo should make a sound.
    #
    def handleFinger(self, finger, tone, lowestFinger):
        light = 0 # light off = 0, light on = 1

        if finger.joint_position(Finger.JOINT_TIP)[Z_AXES] < 0 :
            light = 1
        
        # thumb has no sound. Only plays sound for the lowest positioned finger
        if (finger.joint_position(Finger.JOINT_TIP)[Y_AXES] < lowestFinger) :
            lowestFinger = finger.joint_position(Finger.JOINT_TIP)[Y_AXES]
            tone = finger.type()

        return light, tone, lowestFinger


##-----------------------------------------------------------------------------------------

def main():
	listener = SampleListener()
	controller = Leap.Controller()
    
	controller.add_listener(listener)
    
    # Keep this process running until Enter is pressed
	print "Press Enter to quit..."
    
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		# Remove the sample listener when done
		controller.remove_listener(listener)

##-----------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()