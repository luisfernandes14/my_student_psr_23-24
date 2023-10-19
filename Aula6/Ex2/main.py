#!/usr/bin/env python3
import cv2

def main():
    # Inicialization
    capture = cv2.VideoCapture(0)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    
    #Execution

    while True:
        _, image = capture.read()  # get an image from the camera
        cv2.imshow(window_name,image)
        if cv2.waitKey(113) == ord('q'): #quit program
            break

    

if __name__ == '__main__':
    main()