
import mediapipe as mp
import cv2 as cv
import pyautogui
cam = cv.VideoCapture(0)

face_maesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
screen_w ,screen_h = pyautogui.size()
while 1>0:
    _, frame = cam.read()
    frame = cv.flip(frame,1)
    rgb_Frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    output = face_maesh.process(rgb_Frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w , _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id , landmark in enumerate( landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv.circle(frame,(x,y),3 , (0,255,0))
            if id == 1:
                screen_x = int(landmark.x * screen_w)
                screen_y = int(landmark.y * screen_h)
                pyautogui.moveTo(screen_x,screen_y)
        left = [ landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv.circle(frame,(x,y),3 , (0,255,255))
        if (left[0].y - left[1].y)<0.008:
            pyautogui.click()
    cv.imshow("Eye Contolled Mouse", frame)
    cv.waitKey(1)
