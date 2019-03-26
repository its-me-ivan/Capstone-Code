import evdev
#from evdev import InputDevice, categorize, ecodes
#create 'gamepad' object to store data
gamepad = evdev.InputDevice('/dev/input/event3')

#print device info
print(gamepad)

#Show available capabilities
print(gamepad.capabilities(verbose=True))
