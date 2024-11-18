# This is for learning about neoPixel control on a micro:bit using python
from microbit import *
import neoPixelPlus
numLEDs1=81
numLEDs2=120

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

np0 = neoPixelPlus.neoPixelPlus(pin2, numLEDs1)
np1 = neoPixelPlus.neoPixelPlus(pin1, numLEDs2)


np0.gradient(red,green)
np1.gradient(blue,red)


while True:
	np0.rotate(-1)
	np1.rotate(1)
	np0.show()
	np1.show()


