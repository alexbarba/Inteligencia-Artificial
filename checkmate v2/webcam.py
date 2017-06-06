#!/usr/bin/env python
import cv2
import os
import glob
directory = 'captures'
if not os.path.exists(directory):
    os.makedirs(directory)

class webcam():
	
	def __init__(self):
		self.cam = cv2.VideoCapture(1)
		self.cam.set(cv2.CAP_PROP_FRAME_WIDTH,12800);
		self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT,800);
		self.img_counter = self.counter()
		
	def counter(self):
		return len(glob.glob1(directory,"board*.png"))
	
	def camSquare(self):
		dif = (max(self.frame.shape[:2]) - min(self.frame.shape[:2]))
		return self.frame[0:min(self.frame.shape[:2]), int(dif/2):int(max(self.frame.shape[:2])-dif/2)]
		
	def capture(self):
		# SPACE pressed
		img_name = "board{}.png".format(self.img_counter)
		cv2.imwrite(os.path.join(directory, img_name), self.frame)
		print("{} written!".format(img_name))
		
	def webcamView(self):
		cv2.namedWindow("webCamView")
		img_counter = 0
		while True:
			ret, self.frame = self.cam.read()
			self.frame = self.camSquare()
			cv2.imshow("webCamView", self.frame)
			if not ret:
				break
			k = cv2.waitKey(1)

			if k%256 == 27:
				# ESC pressed
				print("Escape hit, closing...")
				break
			elif k%256 == 32:
				self.capture()
		cv2.destroyAllWindows()

if __name__ == '__main__':
	
	cam = webcam()
	cam.webcamView()
	
	
