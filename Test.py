import evdev
import RPi.GPIO as GPIO
import RPIO.PWM as PWM

#setting headder pins
GPIO.setmode(GPIO.BCM)
ChnlL = 13
ChnlR = 12
ChnlW = 11
PWM.setup(1)
PWM.init_channel(ChnlL, 3000)
PWM.init_channel(ChnlR, 3000)
PWM.init_channel(ChnlW, 3000)

#Initializing throttle and direction
RThrot = 0
LThrot = 0
sigLimit = 2900

#set direction pins
DirPinL = 23
DirPinR = 24
DirPinW = 25
GPIO.setup(DirPinL, GPIO.OUT)
GPIO.setup(DirPinR, GPIO.OUT)
GPIO.setup(DirPinW, GPIO.OUT)
PWMPinL = 17
PWMPinR = 27
PWMPinW = 18
PWM.add_channel_pulse(ChnlL, PWMPinL, 0, 0)
PWM.add_channel_pulse(ChnlR, PWMPinR, 0, 0)
PWM.add_channel_pulse(ChnlW, PWMPinW, 0, 0)

from evdev import InputDevice, categorize, ecodes
#create 'gamepad' object to store data
gamepad = InputDevice('/dev/input/event3')

#print device info
print(gamepad)

#Temporary Weapon Code. 50% duty cycle
GPIO.output(DirPinW, GPIO.LOW)
PWM.clear_channel_gpio(ChnlW, PWMPinW)
PWM.add_channel_pulse(ChnlW, PWMPinW, 0, 1500)

#evdev takes care of pooling controller in a loop
for event in gamepad.read_loop():
	#check analog sticks
	if event.type == ecodes.EV_ABS:
		if event.code == 1:
			LThrot = float(int(-(event.value / 255)+128))
			#clear pwm output pulse and add updated. MAX DUTY CYCLE 50% FOR TESTS
			PWM.clear_channel_gpio(ChnlL, PWMPinL)
			PWM.add_channel_pulse(ChnlL, PWMPinL, 0, int(abs(sigLimit*(LThrot/128))))
			
			#set dirrection
			if LThrot > 0:
				GPIO.output(DirPinL, GPIO.LOW)
			else:
				GPIO.output(DirPinL, GPIO.HIGH)
				
			#print for testing
			print ('Left: ' + str(LThrot))
			
		elif event.code == 4:
			RThrot = float(int(-(event.value / 255)+128))
			#clear pwm output pulse and add updated. MAX DUTY CYCLE 50% FOR TESTS
			PWM.clear_channel_gpio(ChnlR, PWMPinR)
			PWM.add_channel_pulse(ChnlR, PWMPinR, 0, int(abs(sigLimit*(RThrot/128))))
			
			#set dirrection
			if RThrot > 0:
				GPIO.output(DirPinR, GPIO.LOW)
			else:
				GPIO.output(DirPinR, GPIO.HIGH)
				
			#print for testing
			print ('Right: ' + str(RThrot))
	
