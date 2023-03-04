import cv2

# read an image from file
img = cv2.imread("download.png")

# print(img)
# print(img.shape)
# cv2.imshow("image loaded",img)
# cv2.waitKey(0) #0-infinite time, time in milliseconds

# write the image to a file
# cv2.imwrite("new_data.png",img)

# take a selfie from camera 😂
# vid = cv2.VideoCapture(0)
# ret, frame = vid.read()
# cv2.imwrite("your_selfie.png",frame)

# flipped_image = cv2.flip(img, 0) # 0 - flip vertically
# cv2.imshow("flipped image vertically ", flipped_image)

# flipped_image = cv2.flip(img, 1) # 1 - flip horizontally
# cv2.imshow("image flipped horizontally", flipped_image)

#cropping
# crop = img[50:180, 100:300]  
# cv2.imshow('original', img)
# cv2.imshow('cropped', crop)
# cv2.waitKey(0)


#color spaces - BGR,RGB, HSV : COLOR_BGR2GRAY
