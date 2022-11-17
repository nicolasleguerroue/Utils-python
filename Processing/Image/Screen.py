import cv2 as cv

class Screen():

	def __init__(self):
		pass

	@staticmethod
	def display(title, image):

		cv.imshow(title, image)

	@staticmethod
	def addText(image, text="Default text", coordinates=(50,50), lineWidth=1, color=[255,255,255]):

		assert type(coordinates) is tuple
		assert type(color) is tuple

		cv.putText(image, text, coordinates, cv.FONT_HERSHEY_SIMPLEX, lineWidth, color)

	@staticmethod
	def clear(self):

		cv.destroyAllWindows()

def main():
	pass


if( __name__ == "__main__"):
	main()