import numpy as np
from PIL import ImageGrab
import cv2
import time

#controls: https://stackoverflow.com/questions/43483121/simulate-xbox-controller-input-with-python

def screen_record():
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0,0,800,640))), cv2.COLOR_BGR2RGB)
        processed = process_img(printscreen)
        print('capturing at {} fps'.format(1/(time.time()-last_time)))
        last_time = time.time()
        cv2.imshow('window', printscreen)
        cv2.imshow('processed', processed)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def process_img(image):
    #original_image = image
    # convert to gray
    #processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(image, threshold1=200, threshold2=300)
    return processed_img

def main():
    screen_record()


if __name__ == "__main__":
    main()