#!/usr/bin/env python3
import argparse
from time import sleep
import cv2

def main():

    parser=argparse.ArgumentParser(description='Definição do path para a imagem e abertura da mesma')
    
    parser.add_argument("-fp1","--find_path1",type=str)
    parser.add_argument("-fp2","--find_path2",type=str)
    
    args=vars(parser.parse_args())
    
    image_filename1= args["find_path1"]
    image_filename2= args["find_path2"]
    
    
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image
    image2 = cv2.imread(image_filename2, cv2.IMREAD_COLOR) # Load an image
  
    cv2.imshow('image1', image1)
    cv2.imshow('image2', image2)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()