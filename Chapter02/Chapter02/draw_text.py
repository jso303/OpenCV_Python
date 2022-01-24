import cv2

img = cv2.imread("./img/Ch02_img/blank_500.jpg")

# putText(글씨를 표시할 이미지, 표시할 문자열, 좌표(x,y), 글꼴, 글꼴 크기, 색(파,초,빨) )

cv2.putText(img, "Plain", (50,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
cv2.putText(img, "Simplex", (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
cv2.putText(img, "Duplex", (50,110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))
cv2.putText(img, "Simplex", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0))

cv2.putText(img, "Complex Small", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
cv2.putText(img, "Complex", (50, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
cv2.putText(img, "Triplex", (50, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
cv2.putText(img, "Complex", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))

cv2.putText(img, "Script Simple", (50, 330), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,0))
cv2.putText(img, "Script Complex", (50, 370), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,0))

cv2.putText(img, "Plain Italic", (50, 430), \
    cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0,0,0))
cv2.putText(img, "Complex Italic", (50, 470), \
    cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0,0,0))

cv2.imshow("draw text", img)
cv2.waitKey()
cv2.destroyAllWindows()