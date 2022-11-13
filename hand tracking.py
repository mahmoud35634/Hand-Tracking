import cv2
from cv2 import utils
import time
import mediapipe

cap = cv2.VideoCapture(0)

pTime = 0
cTime = 0

mphands = mediapipe.solutions.hands

mpdraw = mediapipe.solutions.drawing_utils
hands = mphands.Hands()

while True:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processing = hands.process(img)
    if processing.multi_hand_landmarks:
        # print(processing.multi_hand_landmarks)
        for handlms in processing.multi_hand_landmarks:
            # print(handlms)
            for id, lm in enumerate(handlms.landmark):
                # print(id,lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(frame, (cx, cy), 8, (255, 244, 0), cv2.FILLED)

            mpdraw.draw_landmarks(frame, handlms, mphands.HAND_CONNECTIONS)

    cv2.imshow('Frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()