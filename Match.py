import cv2  
import numpy as np  
from matplotlib import pyplot as plt  
 

'''
TM_SQDIFF_NORMED
'''
def judgematch(source, template, threshold):
	img1 = source.copy()
	w, h, way = template.shape[::-1]
	method = cv2.TM_SQDIFF_NORMED
	res = cv2.matchTemplate(img1,template,method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	if min_val > threshold:
		return False, min_val
	# top_left = min_loc
	# bottom_right = (top_left[0] + w, top_left[1] + h)
	return True, min_val





'''
img = cv2.imread("chuji.png",0)  	
img2 = img.copy()
template = cv2.imread("chuji-sign.png",0)  
w,h = template.shape[::-1]  
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'] 

meth = 'cv2.TM_SQDIFF_NORMED'
img = img2.copy()  

method = eval(meth)  

res = cv2.matchTemplate(img,template,method)  
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) 
print(min_val,max_val,min_loc,max_loc) 

if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:  
    top_left = min_loc  
else:  
    top_left = max_loc  
bottom_right = (top_left[0] + w, top_left[1] + h)  

cv2.rectangle(img,top_left, bottom_right, (0,255,0), 3)  

print (meth)  
plt.subplot(221), plt.imshow(img2, cmap="gray")  
plt.title('Original Image'), plt.xticks([]),plt.yticks([])  
plt.subplot(222), plt.imshow(template, cmap="gray")  
plt.title('template Image'),plt.xticks([]),plt.yticks([])  
plt.subplot(223), plt.imshow(res, cmap="gray")  
plt.title('Matching Result'), plt.xticks([]),plt.yticks([])  
plt.subplot(224), plt.imshow(img, cmap="gray")  
plt.title('Detected Point'),plt.xticks([]),plt.yticks([])  
plt.show()  
'''