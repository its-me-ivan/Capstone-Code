import time
import RPi.GPIO as GPIO
import RPIO.PWM as PWM

#setting headder pins
#Chnl = 13
PWM.setup(1)
PWM.init_channel(1, 3000)

#PWMPinW = 18
PWM.add_channel_pulse(1, 18, 0, 1000)
PWM.add_channel_pulse(1, 23, 0, 1500)


while True:
	time.sleep(1)
