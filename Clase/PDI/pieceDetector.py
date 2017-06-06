#!/usr/bin/env python
import cv2

class pieceDetector:
	def __init__(self):
		pass

	def detect(self, c):
		piece = "unknown"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.06 * peri, True)

		if len(approx) == 3:
			piece = "peon"

		elif len(approx) == 4:
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			piece = "alfil" if ar >= 0.9 and ar <= 1.1 else "caballo"

		elif len(approx) == 5:
			piece = "torre"
		
		elif len(approx) == 6:
			piece = "dama"
		
		else:
			piece = "king"
		
		return piece

		
