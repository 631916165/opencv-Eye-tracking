#导入库
import cv2
import numpy as np
import os

os.chdir('C:/Users/root\Desktop')
cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    if ret is False:
        break
    rows,cols,_ = frame.shape
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #去除噪音
    frame_gray = cv2.GaussianBlur(frame_gray,(7,7),0)
    _,threshold = cv2.threshold(frame_gray,5,255,cv2.THRESH_BINARY_INV)
    contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        #准确绘画眼睛
        (x,y,w,h) = cv2.boundingRect(cnt)
        # cv2.drawContours(frame,[cnt],-1,(0,0,255),3)#绘画出瞳孔轮廓
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.line(frame,(x + int(w/2),0),(x + int(w/2),rows),(0,255,0),2)
        cv2.line(frame,(0,y + int(h/2)),(cols,y + int(h/2)),(0,255,0),2)
        break
    print(type(contours))
    print(len(contours))
    #轮廓数组
    print(hierarchy)
    cv2.imshow("Frame",frame)
    cv2.imshow("frame_gray",frame_gray)
    cv2.imshow("tongkong",threshold)
    key = cv2.waitKey(30)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()