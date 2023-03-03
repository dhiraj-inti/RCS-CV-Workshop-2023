import cv2
import mediapipe as mp
import numpy as np

mPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mPose.Pose()

cap = cv2.VideoCapture('D:\SASTRA\RCS\CV Workshop 2023\Pose-Detection-With-CV-main\8.mp4')
#cap = cv2.VideoCapture(0)

drawspec1 = mpDraw.DrawingSpec(thickness=2,circle_radius=3,color=(0,0,255))
drawspec2 = mpDraw.DrawingSpec(thickness=3,circle_radius=8,color=(0,255,0))

while True:
    success,img = cap.read()
    #print(img.shape)
    img = cv2.resize(img,(800,700))
    results = pose.process(img)
    mpDraw.draw_landmarks(img,results.pose_landmarks,mPose.POSE_CONNECTIONS,drawspec1, drawspec2)

    h,w,c = img.shape
    imgBlank = np.zeros([h,w,c])
    imgBlank.fill(255)
    mpDraw.draw_landmarks(imgBlank, results.pose_landmarks, mPose.POSE_CONNECTIONS, drawspec1, drawspec2)

    cv2.imshow('poseDetection',img)
    cv2.imshow('extractedPose', imgBlank)
    cv2.waitKey(1)