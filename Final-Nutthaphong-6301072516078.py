import cv2

#วิธีเปิด VDO 

cap = cv2.VideoCapture("left_output-1.avi") 

#อ่านไฟล์สำหรับการจำแนก
while(cap.isOpened()): #การวนการทำงานของ VDO 
    ret,frame = cap.read()  

    frame = cv2.resize(frame,(1200,700)) 

    cv2.imshow("video",frame)

    if cv2.waitKey(5) & 0xFF == ord('n'): # ความเร็วของ VDO และปุ่มหยุดการทำงานของ VDO
        break

cap.release()
cv2.destroyAllWindows()

