from Camera import Camera
from Screen import Screen
from ..Debug.Debug import Debug
from Color.Color import Color
import cv2 as cv

import numpy as np

class ColorDetector(Debug):

	def __init__(self, indexVideoDev):

		super().__init__()

		self.println("Version of OpenCV : "+str(cv.__version__), self.INFO)

		self.__camera = Camera(indexVideoDev)
		self.__screen = Screen()

		self.__key = None
		
		self.__minSaturationValue = 80
		self.__maxSaturationValue = 255

		self.__minValueValue = 80
		self.__maxValueValue = 255

		self.setKernel(20)

	def minSaturation(self):
		return self.__minSaturationValue

	def maxSaturation(self):
		return self.__maxSaturationValue

	def minValue(self):
		return self.__minValueValue

	def maxValue(self):
		return self.__maxValueValue

	def setMinSaturation(self, value):
		if(value>=0 and value <=255):
			self.println("Update of min saturation <"+str(value)+str(">"))
			self.__minSaturationValue = value
			self.__updateIntervals()

	def setMaxSaturation(self, value):
		if(value>=0 and value <=255):
			self.println("Update of max saturation <"+str(value)+str(">"))
			self.__maxSaturationValue = value
			self.__updateIntervals()

	def setMinValue(self, value):
		if(value>=0 and value <=255):
			self.println("Update of min Value <"+str(value)+str(">"))
			self.__minValueValue = value
			self.__updateIntervals()

	def setMaxValue(self, value):
		if(value>=0 and value <=255):
			self.println("Update of max Value <"+str(value)+str(">"))
			self.__maxValueValue = value
			self.__updateIntervals()

	def setKernel(self,size):

		self.__kernelSize = size
		self.println("Set Kernel of ["+str(size)+"*"+str(size)+"]", self.INFO)
		self.__kernel = np.ones((self.__kernelSize, self.__kernelSize),np.uint8)

	def open(self, mask):

		return cv.morphologyEx(mask, cv.MORPH_OPEN, self.__kernel)

	def close(self, mask):

		return cv.morphologyEx(mask, cv.MORPH_CLOSE, self.__kernel)

	def __updateIntervals(self):
		
		self.__lower_bound = np.array([self.__color.minHueValue(), self.__minSaturationValue, self.__minValueValue])   
		self.__upper_bound = np.array([self.__color.maxHueValue(), self.__maxSaturationValue, self.__maxValueValue])

	def setColor(self, color):

		self.__color = color
		self.println("New color ("+str(color)+")")
		self.__updateIntervals()

	def waitKey(self):

		self.__key = cv.waitKey(1) & 0xFF

	def detectColor(self):

		frame = self.__camera.read()
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

		self.__screen.display(self.__color.name()+" Mask", hsv)

		mask = cv.inRange(hsv, self.__lower_bound, self.__upper_bound)
		mask = self.open(mask) #delete small noise

		res = cv.bitwise_and(frame,frame, mask= mask)

		self.__screen.display(self.__color.name()+" TETTE",hsv)

		contours, hierarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

		output = cv.drawContours(frame, contours, -1, (self.__color.blue(), self.__color.green(), self.__color.red()), 1)

		self.__screen.addText(output, "Current color : "+self.__color.name()+" - "+str(len(contours))+" items found", (50,50), 1, self.__color.bgr())
		self.__screen.addText(output, "'r' : detect 'Red'", (50,100), 0.5, (255,255,255))
		self.__screen.addText(output, "'g' : detect 'Green'", (50,130), 0.5, (255,255,255))
		self.__screen.addText(output, "'b' : detect 'Blue'", (50,160), 0.5, (255,255,255))
		self.__screen.addText(output, "'y' : detect 'Yellow'", (50,190), 0.5, (255,255,255))
		self.__screen.addText(output, "'p' : increase 'S' value [+10]", (50,220), 0.5, (255,255,255))
		self.__screen.addText(output, "'m' : decrease 'S' value [-10]", (50,250), 0.5, (255,255,255))
		self.__screen.addText(output, "'o' : increase 'V' value [+10]", (50,280), 0.5, (255,255,255))
		self.__screen.addText(output, "'l' : decrease 'V' value [-10]", (50,310), 0.5, (255,255,255))

		self.__screen.display("Detector", output)
		
		self.__key = cv.waitKey(1) & 0xFF

	def getKey(self):
		return self.__key