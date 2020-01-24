#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
from networktables import NetworkTables
import numpy as np
import argparse
import cv2
import time
import imutils
x = 0 #programın ileride hata vermemesi için x 0 olarak tanımlıyorum
y = 0 # programın ileride hata vermemesi için y 0 olarak tanımlıyorum
NetworkTables.initialize(server='roborio-8208-frc.local') # Roborio ile iletişim kuruyoruz
table = NetworkTables.getTable("Vision") # table oluşturuyoruz

#rengin algılanması
colorLower = (60, 255, 204)
colorUpper = (95, 255, 251)
#converter.py ile convert ettiğiniz rengi buraya giriniz
camera = cv2.VideoCapture(0) #  webcamin bagli oldugu port varsayilan 0
camera.set(15, -10)

while True: #yazılımımız çalıştığı sürece aşağıdaki işlemleri tekrarla
     
     (grabbed, frame) = camera.read() # grabbed ve frame değişkenini camera.read olarak tanımlıyoruz.


     frame = imutils.resize(frame, width=320, height=240) # görüntü genişliğini ayarlıyorum
     frame = imutils.rotate(frame, angle=0) # görüntüyü sabitliyoruz

     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # görüntüyü hsv formatına çeviriyoruz
     mask = cv2.inRange(hsv, colorLower, colorUpper) # hsv formatına dönen görüntünün bizim belirttiğimiz renk sınırları içerisinde olanları belirliyor
     mask = cv2.erode(mask, None, iterations=2) # bizim renklerimizi işaretliyor
     mask = cv2.dilate(mask, None, iterations=2) # bizim renklerimizin genişliğini alıyor


     cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	 cv2.CHAIN_APPROX_SIMPLE)[-2]
     center = None


     if len(cnts) > 0:

		     c = max(cnts, key=cv2.contourArea)
		     ((x, y), radius) = cv2.minEnclosingCircle(c)
		     M = cv2.moments(c)
		     center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


		     if radius > 10: #algılanacak hedefin minumum boyutu
			     cv2.circle(frame, (int(x), int(y)), int(radius),
				 (0, 255, 255), 2)
			     cv2.circle(frame, center, 5, (0, 0, 255), -1)
     else:
          x = 0
          y = 0
          r = 0

     print("x : ")
     print(x) # kameradan gelen görüntüde bizim rengimiz varsa x kordinatı
     print("y : ")
     print(y) # kameradan gelen görüntüde bizim rengimiz varsa y kordinatı
     cv2.imshow("test", frame)
     cv2.waitKey(1)


     table.putNumber("X", x) # roborioya değeri göndermek
     table.putNumber("Y", y)
     
