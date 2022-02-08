import cv2
url = 'rtsp://admin:admin@192.168.1.214:8000/'#根据摄像头设置IP及rtsp端口
cap = cv2.VideoCapture(url)#读取视频流
if not cap.isOpened():
    print("失败")
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
