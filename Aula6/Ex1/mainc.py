#!/usr/bin/env python3

#split da imagem dos planos R G B

import cv2
import argparse
import numpy as np

def main():
    #Inicialização
    parser=argparse.ArgumentParser(description='Definição do path para a imagem e abertura da mesma')
    parser.add_argument("-if","--image_filename",help="Digite qual o caminho para a imagem",required=False,default="/home/luis/Desktop/PSR/my_student_psr_23-24/Aula5/Images/atlascar2_thresholded.png",type=str)
    args=vars(parser.parse_args())    
    
    #Execution
    image_filename=args("image_filename")
    image_rgb=cv2.imread(image_filename,cv2.IMREAD_COLOR)
    h,w,nc = image_rgb.shape

    xc=int(w/2)
    yc=int(h/2)     
    cv2.circle(image_rgb, (xc,yc), 55,(255,0,0),-1)


    #Visualização
    
    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


    cv2.destroyWindow("image_rgb")




if __name__ == '__main__':
    main()