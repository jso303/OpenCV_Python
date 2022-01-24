import cv2

title = "mouse event"
img = cv2.imread("./img/Ch02_img/blank_500.jpg")
cv2.imshow(title, img)

colors = {"black" : (0,0,0),
          "red" : (0,0,255),
          "blue" : (255,0,0),
          "green" : (0,255,0)
          }

def onMouse(event, x, y, flags, param):
    print(event, x, y, flags)
    color = colors["black"]
    # 왼쪽 버튼을 누른 경우
    if event == cv2.EVENT_LBUTTONDOWN:
        # 컨트롤키, 시프트키 같이 누른 경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:  
            color = colors["green"]
        # 시프트키 누른 경우
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors["blue"]
        # 컨트롤키 누른 경우
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors["red"]
        cv2.circle(img, (x,y), 30, color, -1)   # 왼쪽 버튼을 제외한 다른 키를 누르지 않는 경우
        cv2.imshow(title, img)                  # 검은색 원을 좌표에 그림
        
cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()