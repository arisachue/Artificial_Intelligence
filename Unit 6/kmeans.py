# -*- coding: utf-8 -*-

import urllib.request
import io
from PIL import Image
import random

K = 8

def twentyseven_color_naivequant(pixel, width, height):
    for w in range(0, width):
        for h in range(0, height):
            r, g, b = pixel[w, h]
            if r < 255 // 3:
                r = 0
            elif r > 255*2//3:
                r = 255
            else: 
                r = 127
            if g < 255 // 3:
                g = 0
            elif g > 255*2//3:
                g = 255
            else: 
                g = 127
            if b < 255 // 3:
                b = 0
            elif b > 255*2//3:
                b = 255
            else: 
                b = 127
            pixel[w, h] = (r, g, b)
    return pixel

def eight_color_naivequant(pixel, width, height):
    for w in range(0, width):
        for h in range(0, height):
            r, g, b = pixel[w, h]
            if r < 128:
                r = 0
            else: 
                r = 255
            if g < 128:
                g = 0
            else: 
                g = 255
            if b < 128:
                b = 0
            else: 
                b = 255
            pixel[w, h] = (r, g, b)
    return pixel

def squared_error(p, mean):
    r, g, b = p
    rm, gm, bm = mean
    return (r-rm)**2 + (g-gm)**2 + (b-bm)**2

def find_min(p, means):
    val = []
    for m in means:
        val.append((m, squared_error(p, m)))
    min_error = sorted(val, key=lambda c: c[1])
    return min_error[0][0], min_error[0][1]

def average(l):
    return sum(l)/len(l)
    
def k_means(pixel, width, height):
    means = dict()
    for i in range(0, K):
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        means[pixel[x,y]] = []
    for w in range(0, width):
        for h in range(0, height):
           key, error = find_min(pixel[w,h], means)
           means[key].append(pixel[w,h])
    
            
URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
f = io.BytesIO(urllib.request.urlopen(URL).read()) # Download the picture at the url as a file object
img = Image.open(f) # You can also use this on a local file; just put the local filename in quotes in place of f.
# img.show() # Send the image to your OS to be displayed as a temporary file
# print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
w, h = img.size
pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
eight_color_naivequant(pix, w, h)
img.show() # Now, you should see a single white pixel near the upper left corner
img.save("my_image.png") # Save the resulting image. Alter your filename as necessary.