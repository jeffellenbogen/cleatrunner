# This is for learning about neoPixel control on a micro:bit using python
from microbit import *
import neopixel
numLEDs1=80
numLEDs2=120

color1=(255,0,0)
color2=(0,255,0)
color3=(0,0,255)

np = neopixel.NeoPixel(pin2, numLEDs1)
np2 = neopixel.NeoPixel(pin1, numLEDs2)

for index in range(numLEDs1):
	if (index%3 == 0):
		np[index]=color1
	elif (index%3 == 1):
		np[index]=color2
	elif (index%3 == 2):
		np[index]=color3

np.show()


def rotate(strip, direction):
	length = len(strip)
	# Rotate pixels left
	if (direction == -1):
		tempPixelData = strip[0]
		for index in range(length-1):
			strip[index]=strip[index+1]
		strip[length-1]=tempPixelData	


while True:
	rotate(np,-1)
	np.show()



