# This is for learning about neoPixel control on a micro:bit using python
from microbit import *
import neopixel
numLEDs=80
color1=(255,0,0)
color2=(0,255,0)
color3=(0,0,255)

np = neopixel.NeoPixel(pin2, numLEDs)

for index in range(numLEDs):
	if (index%3 == 0):
		np[index]=color1
	elif (index%3 == 1):
		np[index]=color2
	elif (index%3 == 2):
		np[index]=color3

np.show()




