import cv2
rtsp = 'http://192.168.0.102:4747/video'
rtsp = 'http://192.168.0.102:8080/video'
rtsp = 0

vc = cv2.VideoCapture(rtsp)

while True:
	ret, frame = vc.read()

	cv2.imshow("frames",frame)
	q = cv2.waitKey(1)
	if q==ord('q'):
		break
vc.release()
cv2.destroyAllWindows()