# This is for learning about neoPixel control on a micro:bit using python
from microbit import *
import neoPixelPlus
numLEDs0=80
numLEDs1=156
numLEDs2=136


red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

np0 = neoPixelPlus.neoPixelPlus(pin2, numLEDs0)
np1 = neoPixelPlus.neoPixelPlus(pin0, numLEDs1)
np2 = neoPixelPlus.neoPixelPlus(pin1, numLEDs2)

np0.gradient(red,green)
np1.gradient(blue,red)
np2.gradient(green,blue)


while True:
	np0.rotate(-1)
	np1.rotate(1)
	np2.rotate(1)
	np0.show()
	np1.show()
	np2.show()


