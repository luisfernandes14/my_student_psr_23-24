#!/usr/bin/env python3
import argparse
from time import sleep
import cv2

def main():

    parser=argparse.ArgumentParser(description='Definição do path para a imagem e abertura da mesma')
    parser.add_argument("-fp","--find_path",help="Digite qual o caminho para a imagem",required=False,default="/home/luis/Desktop/PSR/my_student_psr_23-24/Aula5/Images/atlascar2_thresholded.png",type=str)
    args=vars(parser.parse_args())
    print(args)
    
    image_filename = args["find_path"]
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()