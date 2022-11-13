import cv2 as cv
from ..Debug.Debug import Debug

class Camera(Debug):

	def __init__(self, indexVideoDev):

		super().__init__()

		#Init
		self.__capture = None
		self.__indexVideoDev = indexVideoDev

		try:
			self.__capture = cv.VideoCapture(self.__indexVideoDev)
		except:
			self.println("Cannot open video device (video"+str(self.__indexVideoDev)+")", self.ERROR)

		#Take One picture to get 
		self.__width = self.__capture.get(cv.CAP_PROP_FRAME_WIDTH) 
		self.__height = self.__capture.get(cv.CAP_PROP_FRAME_HEIGHT)
		
		self.println("Camera : "+str(self.__width)+"*"+str(self.__height), self.INFO)


	def width(self):
		return self.__width

	def height(self):
		return self.__height

	def read(self):
		_, frame = self.__capture.read()
		return frame