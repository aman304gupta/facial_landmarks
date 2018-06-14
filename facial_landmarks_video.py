##importing
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2

## For adding command line aarguments

ap = argparse.ArgumentParser()
ap.add_argument("-p","--shape-predictor",required=True,\
                help="path to facial landmark predictor")
## -p is just short form, above is required
##help-- what this argument actually does

ap.add_argument("-r","--picamera",type=int,default=-1,\
                help="whether raspberry camera used or not")
args = vars(ap.parse_args())

detector = dlib.get_frontal_face_detector() ## use dlib's fucntion to detect face_utils
## dlib shape_predictor function will basically give the pose..
predictor = dlib.shape_predictor(args["shape_predictor"]) ## shape_predictor argument  will basically give path #

vs = VideoStream(usePiCamera = args["picamera"] >0).start() ## An imutils function
time.sleep(2.0) ## Python fucntion to stop execution fr 2 secs

while True:

    frame = vs.read() ## returns the next frame
    frame = imutils.resize(frame, width = 400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0) ## This basically gives bounding box for the faces

    for rect in rects: ## Iterating over all the faces

        shape = predictor(gray, rect) ## dlib will predict landmarks for this face
        shape = face_utils.shape_to_np(shape)

        for (x,y) in shape:

            cv2.circle(frame, (x,y), 1, (0,0,255), -1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"): ##i.e exit infinite loop by pressing q
        break
cv2.destroALLWindows()
vs.stop()## Imutils function for stopping
