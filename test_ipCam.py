import cv2
import numpy as np

# print("Before URL")
# cap = cv2.VideoCapture('rtsp://admin:dmpk1234@10.0.0.100/H264?ch=1&subtype=0')
cap1 = cv2.VideoCapture('rtsp://admin:dmpk1234@10.0.0.100:554/cam/realmonitor?channel=1&subtype=0')
cap2 = cv2.VideoCapture('rtsp://admin:dmpk1234@10.0.0.101:554/cam/realmonitor?channel=1&subtype=0')
cv2.namedWindow("Cams", cv2.WINDOW_NORMAL)
print("After URL")

while True:

    #print('About to start the Read command')
    ret2, frame2 = cap2.read()
    ret1, frame1 = cap1.read()


    frame2_resized = cv2.resize(frame2, (1024, 768))
    frame1_resized = cv2.resize(frame1, (1024, 768))
   
    numpy_vertical = np.vstack((frame1_resized, frame2_resized))
    #print('About to show frame of Video.')
    
    cv2.imshow("Cams",numpy_vertical)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
