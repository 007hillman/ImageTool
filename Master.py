import os
import PIL
import easygui
import math

from datetime import datetime
from os import environ as env
from PIL import Image, ImageDraw, ImageFont


##image.save('edited_images/image.png')
option = None
save_option = None
initial_image = None
image_size = None
input_text = None
text_position = None

def main():

  ReadImageFile(initial_image,image_size)  

def ReadImageFile(init_image, im_size):
  global image_size, initial_image
  if init_image == None:
    if im_size== None:
      print("enter the image size [small,medium,large] : ")
      image_size= input()
    file_path = easygui.fileopenbox()
    initial_image = Image.open(file_path)
  ResizeImage(initial_image,image_size)

def ResizeImage( opened_image, image_size):
  image = opened_image
  
  if image_size == 'small':
    image = opened_image.resize((128,72),resample=0,box=None)   
  elif image_size == 'medium':
    image = opened_image.resize((512,288),resample=0,box=None) 
  elif image_size == 'large':
    image = opened_image.resize((1024,576),resample=0,box=None) 
  print("enter text : ")
  input_text = input()
  print("enter text position as top_right or middle_center or bottom_left etc : ")
  text_position = input()
  TextPosition(input_text,text_position,image)

def TextPosition(my_text, position, editabe_image):
  global initial_image

  base = editabe_image.convert('RGBA')
  txt = Image.new('RGBA',base.size,(255,255,255,0))
  canvas = ImageDraw.Draw(txt)
  w,h = canvas.textsize(my_text)
  color = "black"
  fill_color = "black"
  fnt = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 18)
  
  if position == 'top_left':
    #canvas.rectangle([0,0,(1.5*w),(1.5*h)],fill=color)
    canvas.text((0,0), my_text,fill=fill_color,font = fnt)
  elif position == 'top_center':
    #canvas.rectangle([(editabe_image.width-w)/2,0,(editabe_image.width +(2.3*w))/2,(1.5*h)],fill=color)
    canvas.text(((editabe_image.width -w)/2,0), my_text,fill=fill_color,font = fnt)
  elif position ==  'top_right': 
    #canvas.rectangle([(editabe_image.width-(1.5*w)),0,(editabe_image.width +w),(1.5*h)],fill=color)
    canvas.text((editabe_image.width-(1.5*w),0), my_text,fill=fill_color,font = fnt)
  elif position == 'middle_left':
    #canvas.rectangle([0,(editabe_image.height-h)/2,(1.5*w),(editabe_image.height+(1.5*h))/2],fill=color)
    canvas.text((0,(editabe_image.height - h)/2), my_text,fill=fill_color,font = fnt)
    
  elif position == 'middle_center': 
    #canvas.rectangle([(editabe_image.width-w)/2,(editabe_image.height-h)/2,(editabe_image.width +(2.5*w))/2,(editabe_image.height+(1.5*h))/2],fill=color)
    canvas.text(((editabe_image.width - w)/2,(editabe_image.height - h)/2), my_text,fill=fill_color,font = fnt)
  elif position == 'middle_right':
    #canvas.rectangle([(editabe_image.width-(1.5*w)),(editabe_image.height-h)/2,(editabe_image.width +w),(editabe_image.height+(1.5*h))/2],fill=color)
    canvas.text((editabe_image.width - (1.5*w),(editabe_image.height - h)/2), my_text,fill=fill_color,font = fnt)
  elif position == 'bottom_left': 
    #canvas.rectangle([0,(editabe_image.height-(1.5*h)),(1.5*w),(editabe_image.height +h)],fill=color)
    canvas.text((0,editabe_image.height-(1.5*h)), my_text,fill=fill_color,font = fnt) 
  elif position ==  'bottom_center':
    #canvas.rectangle([(editabe_image.width - w)/2,(editabe_image.height-(1.5*h)),(editabe_image.width +(2.5*w))/2,(editabe_image.height +h)],fill=color)
    canvas.text(((editabe_image.width - w)/2,editabe_image.height-(1.5*h)), my_text,fill=fill_color,font = fnt)
  elif position == 'bottom_right':
    #canvas.rectangle([(editabe_image.width-(1.5*w)),(editabe_image.height-(1.5*h)),(editabe_image.width +w),(editabe_image.height +h)],fill=color)
    canvas.text((editabe_image.width-(1.5*w) ,editabe_image.height-(1.5*h)), my_text,fill=fill_color, font = fnt)

  output = Image.alpha_composite(base, txt)
  initial_image = output
  
  
def SaveImage():
  print("Image is saved successfully")

  
if __name__ == '__main__':
  main()
  print("will you like to add another text (y/n) : ")
  option = input()
  while option == "y":
    main()
    print("will you like to add another text (y/n) : ")
    option = input()
  initial_image.show()
  print("will you like to save (y/n) : ")
  save_option = input()
  if save_option=="y":
    SaveImage()