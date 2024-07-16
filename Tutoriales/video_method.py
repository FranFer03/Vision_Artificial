import cv2 

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,ima = cap.read()
    if ret == True:
        cv2.imshow("video",ima)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()