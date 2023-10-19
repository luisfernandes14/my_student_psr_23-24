#!/usr/bin/env python3

import cv2
import argparse

# Global variables
val=0
window_name = 'window - Ex3a'
image_gray = None

def onTrackbar(val):
    _,thresh=cv2.threshhold(image_gray,val,255,cv2.THRESH_BINARY)
    cv2.imshow(window_name,thresh)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    cv2.imshow('Original',image )  # Display the image
    cv2.createTrackbar("Threshold" %val,window_name,0,255,onTrackbar)
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()