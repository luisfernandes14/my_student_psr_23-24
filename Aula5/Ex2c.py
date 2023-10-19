#!/usr/bin/env python3

#split da imagem dos planos R G B

import cv2

def main():

    image_filename = "/home/luis/Desktop/PSR/my_student_psr_23-24/Aula5/Images/atlascar2.png" #também podia ser pelo caminho como se fosse cd
    image_rgb= cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    
    
    image_b,image_g,image_r = cv2.split(image_rgb)


    retval, image_b_thresholded = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    retval, image_g_thresholded = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    retval, image_r_thresholded = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)

    image_rgb_thresholded=cv2.merge([image_b_thresholded,image_g_thresholded,image_r_thresholded])
    
    
    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow('image_rgb_thresholded', image_rgb_thresholded)
    #cv2.imshow('image_thresholded', image_thresholded)
    
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()