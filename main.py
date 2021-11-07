import cv2
from oculai.ColorDetector import *
# input
Video_in = "/Users/beyzacevik/Downloads/Internship_Challenge/data/formwork.mp4"

# output
Video_out = "/Users/beyzacevik/Downloads/Internship_Challenge/data/formwork_out2.mp4"


# Video Settings
winName = 'output'

cv2.resizeWindow(winName, 500, 500)
cap = cv2.VideoCapture(Video_in)

fps = int(cap.get(cv2.CAP_PROP_FPS))
length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(3))
height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(Video_out, fourcc, fps, (width, height))

n_frame = 0
frames = []

while cap.isOpened():
    # get frame from video
    ret, frame = cap.read()
    print('video_progress: ', round(n_frame*100/length_video, 1), '%')

    if ret:

        # Do something
        color_detector = ColorDetector()
        frame = color_detector.execute(frame)

        out.write(frame)
        cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
        cv2.imshow('output', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
    n_frame += 1

cap.release()