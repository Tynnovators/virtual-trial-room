import cv2
import matplotlib.pyplot as plt

gt=cv2.imread(r'modified_GT.jpg', cv2.IMREAD_COLOR)
original = cv2.imread('original.jpg', cv2.IMREAD_COLOR)

gta=cv2.cvtColor(gt,cv2.COLOR_RGB2GRAY)
original=cv2.cvtColor(original,cv2.COLOR_BGR2BGRA)
#thresh=cv2.THRESH_MASK()
gta=cv2.resize(gta,(600,600))
original=cv2.resize(original,(600,600))
ret, gta = cv2.threshold(gta, 120, 255, cv2.THRESH_BINARY)

# #print(gta)
for i in range(len(gta)):
    for j in range(len(gta[0])):
        if(gta[i][j]!=0):
            original[i][j][3]=0

# cv2.imshow('Binary Threshold', gta)

cv2.imwrite("transparent.png",original)

cv2.waitKey(0)
cv2.destroyAllWindows()
