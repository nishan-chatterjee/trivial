# imports
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# load image
image = cv2.imread("3B1B.png", cv2.IMREAD_COLOR)

# initialize blue and brown to zero
amount_blue = 0
amount_brown = 0

# define image boundaries to iterate through
rows = image.shape[0]
columns = image.shape[1]

# start looking at the image pixel by pixel
for row_index in range(rows):
    for column_index in range(columns):

        # store bgr ratios of pixel
        blue, green, red = image[row_index, column_index]

        # increase count for blue
        if blue >= red != 0 and blue != 0:
            amount_blue += 1
            # to check if blue count matches to image (visual checks)
            image[row_index, column_index] = [244, 164, 96]

            # if blue == red:
            #     # to check if blue count matches to image (visual checks)
            #     image[row_index, column_index] = [255, 255, 255]
            # else:
            #     image[row_index, column_index] = [0, 0, 0]

        # ignore black part
        elif blue == 0 and green == 0 and red == 0:
            pass

        # increase count for brown
        else:
            amount_brown += 1
            # to check if blue count matches to image (visual checks)
            image[row_index, column_index] = [0, 191, 255]
            # image[row_index, column_index] = [0, 0, 0]

# calculating the ratios
blue_part = round(amount_blue/amount_brown, 5)
brown_part = int(amount_brown/amount_brown)
# display results
print("Number of blue pixels = ", amount_blue)
print("Number of brown pixels = ", amount_brown)
print("Ratio of blue to brown = ", blue_part, " : ", brown_part)

output_log = "Blue:Brown = " + str(blue_part) + " : " + str(brown_part)

cv2.putText(image, output_log, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

# display images
cv2.namedWindow("3B1B")
cv2.imshow("3B1B", image)

# save images
cv2.imwrite("3B1B_blue>=red.png", image)

# delay for image to remain open until break
cv2.waitKey(0)
cv2.destroyAllWindows()
