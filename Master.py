import os
import PIL
import math
import argparse
import tweepy
from tweepy.auth import OAuthHandler
import facebook
import json

from datetime import datetime
from os import environ as env
from PIL import Image, ImageDraw, ImageFont
# importing google_images_download module 
from google_images_download import google_images_download 
from instabot import Bot


#global variables
text_array = None
positions = None
file_path = None
initial_image = None
image_size = None
input_text = None
text_position = None
save_file_name = None
edited_image_path = ''
social_medias = None
capt = ''
FLAG = True
source = 'local'

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
fb_access_token = os.environ.get('FACEBOOK_ACCESS_TOKEN')


def InstagramConnect():
  global capt, edited_image_path
  bot = Bot()
  bot.login(ask_for_code=True)
  bot.upload_photo(edited_image_path, caption=capt)

def TwitterConnect() :
  global edited_image_path,consumer_key,consumer_secret,access_token,access_token_secret
  edited_image_path = 'edited images/' + save_file_name
  if not consumer_key :
    print('consumer key absent. Set the environmental variables')
  else :
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    user = api.me()
    print('successfully conected to '+user.name + '\n enter a caption if any : ')
    caption = ''+input()
    api.update_with_media(edited_image_path , caption)

def FacebookConnect():
  global capt,edited_image_path,fb_access_token
  print(fb_access_token)
  fb = facebook.GraphAPI(access_token=fb_access_token)
  # Upload an image with a caption.
  fb.put_photo(image=open(edited_image_path, 'rb'),message=capt)
  
def ImageDownload():
  response = google_images_download.googleimagesdownload()   #class instantiation
  print('enter search text : ')
  search = input()
  arguments = {"keywords":search,"limit":1,"print_urls":True}   #creating list of arguments
  p = response.download(arguments)   #passing the arguments to the function
  paths = str(p).split("['")
  if len(paths) ==1 : 
    return
  paths = paths[1].split("']")
  return paths[0]
  #return paths

def Initialize():
  global text_position,image_size,save_file_name,input_text,file_path,positions,text_array,capt,social_medias
  #initiate the parser
  parser = argparse.ArgumentParser()

  # add long and short argument
  parser.add_argument('-i', '--image', action='store',help="This takes the image path")
  parser.add_argument('-s','--size',action='store',help='enter the image size', default="instagram")
  parser.add_argument('-t','--text',help='enter the text, you can use this variable multiple times',dest='texts',action='append')
  parser.add_argument('-p','--position',action='append',help='enter position pattaining to the text', dest='positions')
  parser.add_argument('-sa','--save',help='enter filename with extension',action='store',required=True)
  parser.add_argument('-sm','--social',action='append',help='enter the name of the social media', dest='socials') 
  parser.add_argument('-c','--caption',action='store',help='enter the image caption', default="")
  args = parser.parse_args()
  if args.image :
    file_path = args.image
  else :
    print("You didn't enter the file path. Tool will now attempt to download from google")
    file_path = ImageDownload()
    if file_path==None :
      print('No Image file found, try again..')
      return
  if args.size :
    image_size = args.size 
  if args.save :
    save_file_name = args.save
  if args.texts :
    text_array = args.texts
  if args.positions :
    positions = args.positions
  if args.caption:
    capt = args.caption
  if args.socials: 
    social_medias = args.socials

def main(txt,pos):
  ReadImageFile(initial_image,image_size,file_path,txt,pos)  

def ReadImageFile(init_image, im_size, file_path, txt,pos):
  global image_size, initial_image
  if initial_image == None :
    if file_path == None :
      return
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
  global social_medias ,edited_image_path
  if not os.path.exists('edited images'):
    os.makedirs('edited images')
  if os.path.exists('edited images/'+ save_file_name):
    print("A file is already saved with this name %s, will you like to override it (y/n)" %(save_file_name))
    option = input()
    if option == 'y':
      initial_image.save('edited images/' + save_file_name)
      edited_image_path = 'edited images/' + save_file_name
  else :
    initial_image.save('edited images/' + save_file_name)  
    edited_image_path = 'edited images/' + save_file_name
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
        print("Image is saved successfully...")
        if len(social_medias) != 0 :
          for i in range(0,len(social_medias)):
            if social_medias[i]=='facebook':
              FacebookConnect()
            if social_medias[i]=='twitter' :
              TwitterConnect()
            if social_medias[i] == 'instagram':
              InstagramConnect()
    else :
      print("enter atleast one text and position...")
  else :
    print("enter atleast one text and position...")
