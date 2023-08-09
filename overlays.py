import cv2 as cv2
import cvzone

image = cv2.imread("native.png")

pirate = cv2.imread("pirate.png",cv2.IMREAD_UNCHANGED)
final_image = cvzone.overlayPNG(image,pirate)
cv2.imshow("image",final_image)
cv2.waitKey(0)