# 히스토그램 비교

import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread("./img/taekwonv1.jpg")
img2 = cv2.imread("./img/taekwonv2.jpg")
img3 = cv2.imread("./img/taekwonv3.jpg")
img4 = cv2.imread("./img/dr_ochanomizu.jpg")

# query 창에 img1 출력
cv2.imshow("query", img1)

imgs = [img1, img2, img3, img4]
hists = []
for i, img in enumerate(imgs):
    plt.subplot(1, len(imgs), i+1)
    plt.title("img%d"%(i+1))
    plt.axis("off")
    plt.imshow(img[:,:,::-1])
    
    # 각 이미지 HSV로 변환
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0,256])
    
    # 0~1로 정규화
    cv2.normalize(hist,hist,0,1,cv2.NORM_MINMAX)
    hists.append(hist)
    
query = hists[0]

# CORREL : 상관관계(1:완전 일치, -1:최대 불일치, 0:무관계)
# CHISQR : 카이제곱(유사성) (0:완전 일치, -1:최대 불일치, 0:무관계)
# INTERSECT : 교차(교차점의 작은 값 정규화) (1:완전 일치, 0:최대 불일치)
# BHATTACHARYYA : 바타차야(두 분포의 중첩되는 부분) (0:완전 일치, 1:최대 불일치)

methods = {"CORREL":cv2.HISTCMP_CORREL, "CHISQR":cv2.HISTCMP_CHISQR,\
           "INTERSECT":cv2.HISTCMP_INTERSECT, "BHATTACHARYYA":cv2.HISTCMP_BHATTACHARYYA}
for j, (name, flag) in enumerate(methods.items()):
    print("%-10s"%name, end="\t")
    
    # img1과 각 이미지의 히스토그램 비교
    for i, (hist, img) in enumerate(zip(hists,imgs)):
        ret = cv2.compareHist(query, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT:
            ret = ret/np.sum(query)
        print("img%d:%7.2f"%(i+1, ret), end="\t")
    print()
plt.show()