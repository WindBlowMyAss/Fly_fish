#以下是最常用的读取视频流的方法
import cv2
url = 'rtsp://admin:HK88888888@192.168.1.214:554/11'
cap = cv2.VideoCapture(url)
if not cap.isOpened():
    print("error")
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()