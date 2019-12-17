import os
import PIL
import easygui
import math
import argparse

from datetime import datetime
from os import environ as env
from PIL import Image, ImageDraw, ImageFont


#global variables
text_array = None
positions = None
file_path = None
initial_image = None
image_size = None
input_text = None
text_position = None
save_file_name = None

def Initialize():
  global text_position,image_size,save_file_name,input_text,file_path,positions,text_array
  #initiate the parser
  parser = argparse.ArgumentParser()

  # add long and short argument
  parser.add_argument('-i', '--image', action='store',help="This takes the image path",required=True)
  parser.add_argument('-s','--size',action='store',help='enter the image size', default="instagram")
  parser.add_argument('-t','--text',help='enter the text, you can use this variable multiple times',dest='texts',action='append')
  parser.add_argument('-p','--position',action='append',help='enter position pattaining to the text', dest='positions')
  parser.add_argument('-sa','--save',help='enter filename with extension',action='store',required=True)
  args = parser.parse_args()
  if args.image :
    file_path = args.image
  if args.size :
    image_size = args.size 
  if args.save :
    save_file_name = args.save
  if args.texts :
    text_array = args.texts
  if args.positions :
    positions = args.positions

def main(txt,pos):
  ReadImageFile(initial_image,image_size,file_path,txt,pos)  

def ReadImageFile(init_image, im_size, file_path, txt,pos):
  global image_size, initial_image
  if initial_image == None :
    initial_image = Image.open(file_path)
  ResizeImage(initial_image,image_size,txt,pos)

def ResizeImage( opened_image, image_size,txt,pos):
  image = opened_image
  
  if image_size == 'instagram':
    image = opened_image.resize((1080,1080),resample=0,box=None)   
  elif image_size == 'twitter':
    image = opened_image.resize((440,220),resample=0,box=None) 
  elif image_size == 'facebook':
    image = opened_image.resize((1200,630),resample=0,box=None) 
  TextPosition(txt,pos,image)

def TextPosition(my_text, position, editabe_image):
  global initial_image

  base = editabe_image.convert('RGBA')
  txt = Image.new('RGBA',base.size,(255,255,255,0))
  canvas = ImageDraw.Draw(txt)
  w,h = canvas.textsize(my_text)
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
  initial_image = output.convert('RGB')
  
  
def SaveImage():
  if not os.path.exists('edited images'):
    os.makedirs('edited images')
  if os.path.exists('edited images/'+ save_file_name):
    print("a file already exists with this name, will you lik to override it (y/n)")
    option = input()
    if option == 'y':
      initial_image.save('edited images/' + save_file_name)
      print("Image is saved successfully")
    else :
      print("process aborted successfully...")
  else :
    initial_image.save('edited images/' + save_file_name)
    print("Image is saved successfully...")

  
if __name__ == '__main__':
  Initialize()
  if text_array != None :
    if positions != None :
      if len(positions) == len(text_array) :
        for i in range(0,len(text_array)):  
          main(text_array[i],positions[i])      
      else:
        print("make sure there is equal numbers of positions as texts")   
      if len(positions) == len(text_array) :       
        SaveImage()
    else :
      print("enter atleast one text and position...")
  else :
    print("enter atleast one text and position...")