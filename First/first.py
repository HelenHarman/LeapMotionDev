import sys, time
sys.path.insert(0, "/Users/helen/Documents/MotionLeap/LeapDeveloperKit_2.1.3+21998_mac/LeapSDK/lib")
import Leap

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Finger


# directions given with cable on left of motion leap
X_AXES = 0
Y_AXES = 1
Z_AXES = 2 # Screen to 0 to You

##---------------------------------------------
class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);


    def on_frame(self, controller):

    	frame = controller.frame()
        self.handleFrame(frame)
    #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
        #print "Frame available"

    def handleFrame(self, frame):
        print "Number of fingers = " + str(len(frame.fingers))
        
        for finger in frame.fingers:
            if finger.type() == Finger.TYPE_THUMB:
                print finger.joint_position(Finger.JOINT_TIP)[Z_AXES] #TODO when less than 0 light up
                time.sleep(3)
            """
            if finger.type() == Finger.TYPE_THUMB:
                print 0
            elif finger.type() == Finger.TYPE_INDEX:
                print 1
            elif finger.type() == Finger.TYPE_MIDDLE:
                print 2
            elif finger.type() == Finger.TYPE_RING:
                print 3
            elif finger.type() == Finger.TYPE_PINKY:
                print 4
            """

##---------------------------------------------


def main():
	listener = SampleListener()
	controller = Leap.Controller()
	#print controller.frame()

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


if __name__ == "__main__":
    main()