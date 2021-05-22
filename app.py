# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:55:27 2021

@author: balaj
"""
import cv2
cars_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
#classifier loaded

def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.5, 4)
    #for detecting cars and receiving co-ords of cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), color=(255, 0, 0), thickness = 2)
        #putting a rectangle over the cars detected
        #255 0 0 - red
        #just a comment to say that it was a ind code
        #once, now its turned out to be a function
    return frame

#now a dunction to detect in video
def Simulator():
    CarVideo = cv2.VideoCapture('cars.mp4')
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        controlkey = cv2.waitKey(1)
        if ret:
            cars_frame = detect_cars(frame)
            cv2.imshow('frame', cars_frame)
        else:
            break

if __name__ == '__main__':
    Simulator()        

