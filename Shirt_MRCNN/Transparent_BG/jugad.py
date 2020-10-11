import cv2

img=cv2.imread('FS15.jpg', cv2.IMREAD_COLOR)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, gta = cv2.threshold(img2, 250, 255, cv2.THRESH_BINARY)


x_end,y_end=0,0
x,y=0,0
flag=0
for i in range(len(gta)):
    for j in range(len(gta[0])):
        if(gta[i][j]!=255):
            x=i
            y=j
            flag=1
            break
    if(flag):
        break
flag=0
for i in range(len(gta)-1,0,-1):
    for j in range(len(gta[0])-1,0,-1):
        print(gta[i][j])
        if(gta[i][j]!=255):
            x_end=i
            y_end=j
            flag=1
            break
    if(flag):
        break

print(x,y,x_end,y_end)
cv2.imwrite("modified_GT.jpg", img[x:x_end - 1, y:y_end - 1])
# cv2.imshow("juu",img)
cv2.waitKey(0)
cv2.destroyAllWindows()