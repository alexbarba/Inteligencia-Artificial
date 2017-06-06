# import the necessary packages
from pieceDetector import *
from boardProcess import *
import argparse
import imutils
import cv2

def createContours(image):
	# convert the resized image to grayscale, blur it slightly,
	# and threshold it
	resized = imutils.resize(image, width=300)
	ratio = image.shape[0] / float(resized.shape[0])
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)[1]
	
	# find contours in the thresholded image and initialize the
	# shape detector
	contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	piece = []
	
	for cnt in contours[1]:
			cnt_len = cv2.arcLength(cnt, True)
			cont = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
			if cv2.contourArea(cont) > 100 and cv2.contourArea(cont) < 28000:
				piece.append(cnt)
	
	return piece



def drawContours(cnts, image):
	resized = imutils.resize(image, width=300)
	ratio = image.shape[0] / float(resized.shape[0])
	sd = pieceDetector()
	for c in cnts:
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		M = cv2.moments(c)
		if (M["m10"] > 0 and M["m00"] > 0 and M["m01"] > 0):
			#print(M, "\n\n")
			
			cX = int((M["m10"] / M["m00"]) * ratio)
			cY = int((M["m01"] / M["m00"]) * ratio)
			#print(cX, cY,"\n\n")
			
			shape = sd.detect(c)
		 
			# multiply the contour (x, y)-coordinates by the resize ratio,
			# then draw the contours and the name of the shape on the image
			c = c.astype("float")
			c *= ratio
			c = c.astype("int")
			cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
			cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (255, 255, 255), 2)
		 
			# show the output image
			cv2.imshow("Image", image)
			cv2.waitKey(0)
			


if __name__ == '__main__':
	# construct the argument parse and parse the arguments
	"""
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
		help="path to the input image")
	args = vars(ap.parse_args())
	
	image = cv2.imread(args["image"])
	"""
	image = cv2.imread("board.jpg")
	image = cv2.resize(image, (600,600))
	image = recognizeBoard(image)
	cv2.imwrite("recognizeBoard.jpg", image )
	#cnts = createContours(image)
	#drawContours(cnts, image)		
