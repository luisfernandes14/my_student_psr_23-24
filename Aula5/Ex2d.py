#!/usr/bin/env python3

import cv2
import numpy as np


def main():

    image_filename = "/home/luis/Desktop/PSR/my_student_psr_23-24/Aula5/Images/color_segmenter.png" #também podia ser pelo caminho como se fosse cd
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #lower_bound = np.array([38,100, 100])
    #upper_bound = np.array([76,255,255])

    #imagemask=cv2.inRange(image,lower_bound,upper_bound)

    cv2.imshow('window', image_hsv)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()