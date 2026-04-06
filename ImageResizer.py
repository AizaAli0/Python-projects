import cv2

#Cofiguration Parameters
source = "scarletwitch.jpg"
destination = 'newImage.png'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow("tile", src)


#calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent /100)
new_height = int(src.shape[0] * scale_percent /100)

#Resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)