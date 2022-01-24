import cv2

img_file = "./img/Ch02_img/girl.jpg"
img = cv2.imread(img_file)
title = "IMG"
x, y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF
    print(key, chr(key))
    if key == ord('a'):     # 좌로 이동
        x -= 10
    elif key == ord('d'):   # 우로 이동
        x += 10
    elif key == ord('w'):   # 위로 이동
        y -= 10
    elif key == ord('s'):   # 아래로 이동
        y += 10
    elif key == ord('q') or key == 27:
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y)
    
    