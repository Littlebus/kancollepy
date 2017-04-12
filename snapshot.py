from PIL import ImageGrab
import numpy as np

def getSnapshot(rect):
	print(rect)
	bbox = rect
	image = ImageGrab.grab(bbox)
	return image
