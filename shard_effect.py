# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:55:52 2019
replace pine needles with target photo
so pine needles are replaced by target photo pixels
gives the effect of photo shards
@author Liz J Goldstein: Owner
"""

from PIL import Image 
import random
   
#Open the image files 
img = Image.open("liz2.jpg")
plant = Image.open("pine2.JPG")


#This program works with images that are square and the same size
#Feed the images through the changeImageSize function to get same size images
img = img.resize((500,500))
plant=plant.resize((500,500))
#image_b.show()

#Create Output Image
raw_output1=plant

height=raw_output1.height
width=raw_output1.width

#load data so faster processing
img_load = img.load()
plant_load = plant.load()


#iterate through each pixel and get the r, g, b values
for i in range(width):
    for j in range(height):
        r=plant_load[i,j][0] 
        g=plant_load[i,j][1]
        b=plant_load[i,j][2]
        #When the pixel is greenish (meaning if below statement is true), replace it with portrait pixels
        if 30 <= r < 255 and 115 < g <= 255 and 130 <= b < 255:
           #fill in green pixel with pixel in same spot in background photo 
            back_color = img_load[i,j] 
            raw_output1.putpixel((i,j),back_color) #Set the output pixel 
        else:
            #select random color
            back_color1=random.randint(1,255)
            back_color2=random.randint(1,255)
            back_color3=random.randint(1,255)
            
            #remaining pixels are a random color
            #raw_output1.putpixel((i,j), (back_color1, back_color2, back_color3))
            
            #remaining pixels are black
            #raw_output1.putpixel((i,j), (0, 0, 0))
            
            #remaining pixels are white
            raw_output1.putpixel((i,j), (255, 255, 255))


#Save the resulting image in C 
raw_output1.save("shards.png")
raw_output1.show()

