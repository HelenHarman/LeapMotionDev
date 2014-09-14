import sys
sys.path.insert(0, "/Users/helen/Documents/MotionLeap/LeapDeveloperKit_2.1.3+21998_mac/LeapSDK/lib")
import Leap

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
##---------------------------------------------
class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);


    def on_frame(self, controller):

    	frame = controller.frame()
    	print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
        print "Frame available"
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