import cv2
import mediapipe as mp
import numpy as np

red = (0,0,255)
blue = (255,0,0)
green = (0,255,0)
purple = (255,0,255)

# Slope

def Gredient(pt1 , pt2):
    y = (pt2[1] - pt1[1])
    x = (pt2[0] - pt1[0])
    if x != 0:
        return y/x
    else:
        return 0

cap = cv2.VideoCapture("D:/Faradars/FVBME003/Video/S4/Files and codes/clips/6.mp4")

E_Pose = mp.solutions.pose
Pose = E_Pose.Pose()
Draw = mp.solutions.drawing_utils
blank = np.zeros((600,800,3))

while True:
    _ , frame = cap.read()
    frame = cv2.resize(frame , (800,600))
    frameRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    output = Pose.process(frameRGB)
    #print(output.pose_landmarks)
    landmarklist = []
    if output.pose_landmarks:
        Draw.draw_landmarks(frame , output.pose_landmarks
                            , E_Pose.POSE_CONNECTIONS)
        Draw.draw_landmarks(blank, output.pose_landmarks
                            , E_Pose.POSE_CONNECTIONS)
        for index , landmark in enumerate(output.pose_landmarks.landmark):

            height , width , channel = frame.shape
            x , y = int(landmark.x*width) , int(landmark.y * height)
           # print(index, x , y)
            landmarklist.append([index , x , y])
        #cv2.circle(frame , (landmarklist[13][1] , landmarklist[13][2]) ,
                 # 15 , purple , -1)
        x11, y11 = landmarklist[11][1:]
        x12, y12 = landmarklist[12][1:]
        x13, y13 = landmarklist[13][1:]
        x14, y14 = landmarklist[14][1:]
        x15, y15 = landmarklist[15][1:]
        x16, y16 = landmarklist[16][1:]
        cx1  = (landmarklist[12][1] + landmarklist[11][1])//2
        cy1 =  (landmarklist[12][2] + landmarklist[11][2])//2
        cx2 = (landmarklist[24][1] + landmarklist[23][1])//2
        cy2 = (landmarklist[24][2] + landmarklist[23][2])//2
        m1 = abs(Gredient(landmarklist[15][1:] , landmarklist[11][1:]))
        if abs(y13-y11)<15 and abs(y14-y12)<15 and 0<m1<1:
            cv2.line(blank , (x15,y15) , (x13,y13) , blue , 4)
            cv2.line(blank, (x13, y13), (x11, y11), blue, 4)
            cv2.line(blank, (x11, y11), (x12, y12), blue, 4)
            cv2.line(blank, (x12, y12), (x14, y14), blue, 4)
            cv2.line(blank, (x14, y14), (x16, y16), blue, 4)
            cv2.line(blank, (cx1, cy1), (cx2, cy2), blue, 4)
            cv2.putText(blank , "T Shape" , (20,100) , cv2.FONT_HERSHEY_SIMPLEX ,
                        1 , blue , 3)
            #print("T")

        m2 = abs(Gredient(landmarklist[15][1:] , landmarklist[11][1:]))
        if abs(y13+25<y11) and abs(y14+25<y12) and 3<m2<4:
            cv2.line(blank, (x15, y15), (x13, y13), blue, 4)
            cv2.line(blank, (x13, y13), (x11, y11), blue, 4)
            cv2.line(blank, (x11, y11), (x12, y12), blue, 4)
            cv2.line(blank, (x12, y12), (x14, y14), blue, 4)
            cv2.line(blank, (x14, y14), (x16, y16), blue, 4)
            cv2.line(blank, (cx1, cy1), (cx2, cy2), blue, 4)
            cv2.putText(blank, "Y Shape", (20, 100), cv2.FONT_HERSHEY_SIMPLEX,
                        1, blue, 3)
            #print("Y")






    cv2.imshow("Pose" , frame)
    cv2.imshow("Blank" , blank)
    blank = np.zeros((600, 800, 3))

    cv2.waitKey(1)