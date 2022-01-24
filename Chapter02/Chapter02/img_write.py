import cv2

img_file = "./img/Chapter02_img/girl.jpg"
save_file = "./img/Chapter02_img/girl_gray.jpg"

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img)     # 파일로 저장, 포멧은 확장자에 따라 다름
cv2.waitKey()
cv2.destroyAllWindows()