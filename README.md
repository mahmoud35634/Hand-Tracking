<h1>Hand-Tracking</h1>
This project makes a datection on hand landmarks and tracking it in real time



## Requirements
* opencv 
* mediapipe
<h2>Installation in python
pip install opencv-python
pip install mediapipe
You can see what the mediapipe used in https://mediapipe.dev/ 


<img src="https://raw.githubusercontent.com/kulin-patel/Hand-Tracking/master/hand_landmarks.png" width="700" height="200" >

<img src="https://raw.githubusercontent.com/kulin-patel/Hand-Tracking/master/Output.png" width="500" height="500">
<h1>Project Description</h1>
 
import libraries:
```python
import cv2
from cv2 import utils
import time
import mediapipe
```

Using libraries:
* drawing_utils module :to draw detections and landmarks over images
* hands module:contains the Hands class that we will use to perform the detection of hand landmarks

After That create an object of class Hands you can see the paramters for Hands(): https://techtutorialsx.com/2021/04/10/python-hand-landmark-estimation/
 

  
```cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
mphands = mediapipe.solutions.hands
mpdraw = mediapipe.solutions.drawing_utils
hands = mphands.Hands()
```

Using while loop for True condition to open Camera
multi_hand_landmarks: if detect multiple hands
HandLandmark containing the 21 hand landmarks indexes

```
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
```
