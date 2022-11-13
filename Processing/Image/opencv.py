import cv2 as cv

from Keyboard.Keyboard import Keyboard

from ..Source.Keyboard import Keyboard
from ..Color.Color import Color
from ..Debug.Debug import Debug
from ColorDetector import ColorDetector

detector = None

def updateColor(color):

	cv.destroyAllWindows()
	detector.setColor(color)
	#detector.detect()
	
def updateMinSaturation(add):

	if(add):
		detector.setMinSaturation(detector.minSaturation()+10)
	else:
		detector.setMinSaturation(detector.minSaturation()-10)

def updateMaxSaturation(add):

	if(add):
		detector.setMaxSaturation(detector.maxSaturation()+10)
	else:
		detector.setMaxSaturation(detector.maxSaturation()-10)
def main():


	cv.destroyAllWindows()

	keyboard = Keyboard()
	result = input("Index of channel : ")
	global detector
	detector  = ColorDetector(int(result))

	color = Color()

	keyboard.addSlot('r', updateColor, color.Red())
	keyboard.addSlot('g', updateColor, color.Green())
	keyboard.addSlot('b', updateColor, color.Blue())
	keyboard.addSlot('y', updateColor, color.Yellow())
	keyboard.addSlot('p', updateMinSaturation, True)
	keyboard.addSlot('m', updateMinSaturation, False)
	keyboard.addSlot('o', updateMaxSaturation, True)
	keyboard.addSlot('l', updateMaxSaturation, False)
	
	detector.setKernel(20)
	detector.setColor(color.Yellow())


	while(True):

		detector.detectColor()
		keyboard.openCVInteract(detector.getKey())
		
		# 	break


if(__name__ == "__main__"):

	main()

