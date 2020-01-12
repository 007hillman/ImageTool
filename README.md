# ImageTool
This tool will add text to an image at a selected position
PREREQUIRES
- Make sure you have python installed 
- Make sure you have pip installed using the command
	sudo apt install python3-pip 	OR
	sudo apt install python-pip
  depending on the version of python you have installed
-Make sure you install the virtual environment using command
	sudo apt install -y python3-venv
- Now for this app run
	sudo apt install python3-tk
	sudo apt-get install ttf-mscorefonts-installer
for the last command press "TAB" to select an option.

RUNNING THE APP
- After cloning the tool, navigate to the folder with the master.py on the terminal and enter the code
	virtualenv venv -p python3  
-start the virtual environment with the command
	source venv/bin/activate
- now run the commands
	pip install pillow
	pip install easygui
- to run the app enter the command
	python3 Master.py -i img_path -sa save_name.jpg -t text -p position
an example will be : 
	python3 Master.py -t "this text will appear top center" -p top_center -sa image.jpg -t "this text will appear bottom center" -p bottom_center

NB: use the inverted commas only when the text is made up of more than one word with spaces. meaning there is no need when entering the image size which is just one word
The arguments can come in any order except for the text and its position which must appear in order
this will run a test on the sample image in that folder
- For help on the various options run the command
	python3 Master.py -h 
- if you have twitter authentication and token keys , store them in these environmental variables by entering these code in the terminal 
	export CONSUMER_KEY="enter your twitter consumer key here"
	export CONSUMER_SECRET="enter your twitter consumer secret here"
	export ACCESS_TOKEN="enter your access token here"
	export ACCESS_TOKEN_SECRET="enter your access token secret here"
- install libraries tweepy and google image download with commands:
	pip install google_images_download
	pip install tweepy
- If you don't enter an image path ( a value for -i) the tool is going to redirect you to a google search and demand you put in a search query.
hint: to search for better quality images, add hd to your query

- Install the facebook sdk with command 
	pip install facebook-sdk==2.0.0
-you'll also need to add an access token to environmental variables using this command
	export FACEBOOK_ACCESS_TOKEN="enter your USER token here"
NB: enter your facebook user token and not access token and also make sure your token has permissions. facebook has got very strict developpers laws
test with this code

-In order to post to social media sites, when running, add the variable -c "the caption of the post" then -sm facebook -sm instagram -sm twitter
you can enter one social media or many as above
- Open the file user_info.json and enter your info. save it and launch the app


