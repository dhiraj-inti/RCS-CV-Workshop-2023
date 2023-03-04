import cv2

# define a video capture object
vid = cv2.VideoCapture(0) #0 for our laptop camera

while(True):

	ret, frame = vid.read()

	cv2.imshow('frame', frame)
	
	# q for quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
