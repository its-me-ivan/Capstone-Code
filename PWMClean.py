import RPIO.PWM as PWM

PWM.setup(30)

PWM.init_channel(1, 3000)

PWM.clear_channel_gpio(1, 18)

PWM.clear_channel(1)

PWM.cleanup()

