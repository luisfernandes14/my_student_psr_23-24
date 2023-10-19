#!/usr/bin/env python3

import cv2

def main():

    image_filename = "/home/luis/Desktop/PSR/my_student_psr_23-24/Aula5/Images/atlascar2_thresholded.png" #também podia ser pelo caminho como se fosse cd
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()