import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		"""
		input: c - contour - outline of the shape trying to identify
		Algo Used - contour approximation - RAMER_DOUGLAS_PEUCKER
		- reducing the number of points in a curve with reduced 
			set of points
		- assumption - curve can be approximated by a series of
			short line segments resulting in approximated curve
			that consist of subset of points of orignal curve
		- approxPolyDouglasPuecker(c, 1-5% of perimeter )

		"""
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04*peri, True)

		side = len(approx)
		
		# if the shape is triangle, it will have 3 vertices
		if side == 3:
			shape = "Triangle"

		#if the shape has 4 vertices, wither a square or rectangle
		elif side == 4:
			# compute the bounding box of the contour and use the 
			# bounding box to compute the aspect ratio
			(x,y,w,h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# square will have aspect ratio that is equal to 1
			# else a rectangle
			shape = "Square" if ar >= 0.95 and ar <=1.05 else "Rectangle"

		# if 5 vertices are there then pentagon
		elif side == 5:
			shape = "Pentagon"

		# otherwise, we assume the shape is a circle
		else:
			shape = "Circle"
		
		# return the name of the shape
		return shape