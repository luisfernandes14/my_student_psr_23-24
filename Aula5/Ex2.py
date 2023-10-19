#!/usr/bin/env python3

import cv2

def main():

    image_filename = "/home/luis/Desktop/PSR/my_student_psr_23-24/Aula5/Images/atlascar2.png" #também podia ser pelo caminho como se fosse cd
    image_rgb= cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image_gray=cv2.cvtColor(image_rgb,cv2.COLOR_BGR2GRAY)

    retval, image_thresholded = cv2.threshold(image_gray, 234, 255, cv2.THRESH_BINARY)

    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow('image_gray', image_gray)
    cv2.imshow('image_thresholded', image_thresholded)
    
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()