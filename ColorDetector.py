import numpy as np
import cv2.cv2 as cv2
import matplotlib.pyplot as plt


class ColorDetector(object):

    def __init__(self):
        self.color_boundaries = [(20, 100, 100), (30, 255, 255)]  # in lower and upper limits in B,G,R for yellowish color

    def execute(self, frame):
        original = frame.copy()
        (lower, upper) = self.color_boundaries
        lower = np.array(lower, dtype='uint8')
        upper = np.array(upper, dtype='uint8')
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        yellowish_mask = cv2.inRange(hsv, lower, upper)
        yellowish_mask[yellowish_mask> 0] = 1
        #masked_image = cv2.bitwise_and(frame, hsv, mask=yellowish_mask)

        masked_image = np.expand_dims(yellowish_mask, axis=-1)*original
        masked_image[yellowish_mask == 0] = original[yellowish_mask==0]

        return masked_image



if __name__ == "__main__":

    Video_in = "/Users/beyzacevik/Downloads/Internship_Challenge/data/formwork.mp4"

    examplar = cv2.imread('/Users/beyzacevik/Desktop/dene.jpeg')
    cd = ColorDetector()
    cd.execute(examplar)
    #cap.release()
