import cv2
import json

facexml = cv2.CascadeClassifier('face.xml')
# eyexml= cv2.CascadeClassifier('eyegl.xml')

webcam = cv2.VideoCapture(0)        # open web cam

while True:
	ret, frame = webcam.read()      # get frame
  
	if frame is None:
		break
		
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        # rgb to gray
	gray = cv2.equalizeHist(gray)
		
	faces = facexml.detectMultiScale(frame)               # use xml

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)  # draw a rectangle

		x2 = str(x+w/2)
		y2 = str(y+h/2)
		font = cv2.FONT_HERSHEY_PLAIN
		cv2.putText(frame ,x2, (x, y-10) ,font,2,(255,0,0), 2, cv2.LINE_AA)    # write x & y
		cv2.putText(frame ,y2, (x+150, y-10) ,font,2,(255,0,0), 2, cv2.LINE_AA)

		dict_xy = {                         
			"x" : x2,
			"y" : y2
		}
		with open('json_cv.json','w') as f:  #write in json
			json.dump(dict_xy, f, indent=2)

		print("x: ", x2 , "  " , "y : " , y2)

		# roi_gray = gray[y:y+h, x:x+w]
		# roi_color = frame[y:y+h, x:x+w]
		# eyes = eyexml.detectMultiScale(roi_gray)      		# eye detect ...
		# for (ex,ey,ew,eh) in eyes:
		# cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	
	cv2.imshow("tashkhis chehreh :) ", frame)        # show 

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):              # exit by press key Q
		break
 


cv2.destroyAllWindows()              # close wiindow
