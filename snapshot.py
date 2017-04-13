from PIL import ImageGrab
import numpy as np

def getSnapshot(rect):
	bbox = rect
	image = ImageGrab.grab(bbox)
	return image
