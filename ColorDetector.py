import numpy as np
import cv2.cv2 as cv2
import matplotlib.pyplot as plt


class ColorDetector(object):

    def __init__(self, image, hsv):
        self.image = image
        self.hsv_image = hsv
        self.color_boundaries = [(0, 100, 100), (30, 255, 255)]  # in lower and upper limits in B,G,R for yellowish color

    def detect_color(self):

        (lower, upper) = self.color_boundaries
        lower = np.array(lower, dtype='uint8')
        upper = np.array(upper, dtype='uint8')
        yellowish_mask = cv2.inRange(self.hsv_image, lower, upper)
        masked_image = cv2.bitwise_and(self.hsv_image, self.hsv_image, mask=yellowish_mask)
        cv2.imshow("imagee", np.hstack([self.image, self.hsv_image, masked_image]))
        return masked_image
        #cv2.waitKey(0)

if __name__ == "__main__":

    Video_in = "/Users/beyzacevik/Downloads/Internship_Challenge/data/formwork.mp4"

    cap = cv2.VideoCapture(Video_in)
    frames = list()

    while cap.isOpened():

        ret, frame = cap.read()

        if ret:
            print('ok')
            frames.append(frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            color_detector = ColorDetector(frame, hsv)
            prediction_frame = color_detector.detect_color()
            frames.append(prediction_frame)
        else:
            break
        break
    print(len(frames))
    cv2.imshow("images all", np.hstack(frames))
    cv2.destroyAllWindows()
    cap.release()


