import cv2
import mediapipe as mp
import pyautogui as ptg

cap = cv2.VideoCapture(0)
hand_dectector = mp.solutions.hands.Hands()
drawing = mp.solutions.drawing_utils
screen_w,screen_h = ptg.size()

index_y=0
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    _ , frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_h , frame_w , _ = frame.shape
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_dectector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    # print(hands)
    if hands:
        for hand in hands:
            drawing.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                # print(x,y)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10,color=(0,255,255)) 
                    index_x = screen_w/frame_w*x
                    index_y = screen_h/frame_h*y
                    ptg.moveTo(index_x,index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10,color=(0,255,255)) 
                    thumb_x = screen_w/frame_w*x
                    thumb_y = screen_h/frame_h*y
                    
                    if abs(index_y - thumb_y) <50:
                        print('Clicked')
                        ptg.click()
                        ptg.sleep(1)
    
    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1)
    