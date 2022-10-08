#!/bin/sh

#  Copyright (C) 2022 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com> 
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com> 
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with DameOpenCV; see the file LICENSE.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

import cv2
 
image = cv2.imread('files/img/rgb.png')
B, G, R = cv2.split(image)
# Corresponding channels are separated
 
cv2.imshow("original", image)
cv2.waitKey(0)
 
cv2.imshow("blue", B)
cv2.waitKey(0)
 
cv2.imshow("Green", G)
cv2.waitKey(0)
 
cv2.imshow("red", R)
cv2.waitKey(0)
 
cv2.destroyAllWindows()
