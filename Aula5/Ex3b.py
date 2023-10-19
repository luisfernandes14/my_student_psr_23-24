#!/usr/bin/env python3

import cv2
import argparse
from functools import partial
#Partial 




def onTrackbar(val,image_gray,window_name):
    _,thresh=cv2.threshhold(image_gray,val,255,cv2.THRESH_BINARY)
    cv2.imshow(window_name,thresh)


def main():

    val=200
    window_name = 'window - Ex3a'
    image_gray = None

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
   
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    cv2.imshow('Original',image )  # Display the image

    cv2.createTrackbar("Threshold" %val,window_name,0,255,partial(onTrackbar,image_gray=image_gray,window_name=window_name))

    cv2.setTrackbarPos("threshgold",window_name,val)
    onTrackbar(val,image_gray,window_name)

    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()