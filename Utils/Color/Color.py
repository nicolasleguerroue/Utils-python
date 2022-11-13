#!/usr/bin/python
# -*- coding: utf-8 -*-


class Color():

	def __init__(self, r=255, g=255, b=255, name="", minHueValue=0, maxHueValue=0):
	
		self.__red = r
		self.__green = g
		self.__blue = b
		self.__hsv = self.__toHSV(r,g,b)
		self.__name = name
		self.__minHueValue = minHueValue
		self.__maxHueValue = maxHueValue

	def name(self):

		return self.__name


	def hsv(self):
		return self.__hsv

	def blue(self):	
		"""Get blue color"""

		return self.__blue

	def green(self):	
		"""Get green color"""

		return self.__green
		
	def red(self):	
		"""Get red color"""

		return self.__red

	def rgb(self):

		return (self.__red, self.__green, self.__blue)

	def bgr(self):

		return (self.__blue, self.__green, self.__red)
	@staticmethod
	def Red():
		return Color(255,0,0, "Red", 170, 180)

	@staticmethod
	def Green():
		return Color(0,255,0, "Green", 40, 80)

	@staticmethod
	def Blue():
		return Color(0,0,255,"Blue", 100, 140)

	@staticmethod
	def Yellow():
		return Color(255,255, 0,"Yellow", 20, 30)
		
	def minHueValue(self):
		return self.__minHueValue

	def maxHueValue(self):
		return self.__maxHueValue

	def __toHSV(self, r, g, b):
 
		r, g, b = r / 255.0, g / 255.0, b / 255.0
 		# h, s, v = hue, saturation, value
		cmax = max(r, g, b)    # maximum of r, g, b
		cmin = min(r, g, b)    # minimum of r, g, b
		diff = cmax-cmin       # diff of cmax and cmin.
 
    	# if cmax and cmax are equal then h = 0
		if(cmax == cmin):
			h = 0
		# if cmax equal r then compute h
		elif (cmax == r):
			h = (60 * ((g - b) / diff) + 360) % 360
    	# if cmax equal g then compute h
		elif (cmax == g):
			h = (60 * ((b - r) / diff) + 120) % 360
    	# if cmax equal b then compute h
		elif (cmax == b):
			h = (60 * ((r - g) / diff) + 240) % 360
		# if cmax equal zero
		if(cmax == 0):
			s = 0
		else:
			s = (diff / cmax) * 100
 
    	# compute v
		v = cmax * 100
		return h, s, v

	def __str__(self):
		return "Color '"+self.__name+"' <"+str(self.__red)+", "+str(self.__green)+", "+str(self.__blue)+"> [HSV="+str(self.__hsv)+"]"
 

if(__name__ == "__main__"):


	color = Color(45, 215, 0)
	print(Color.Red())
	print(Color.Green())
	print(Color.Blue())
	print(color)

		

