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
	python3 Master.py -t "this text will appear top center" -i D9P8_6SX4AADXM4.jpeg -p top_center -sa image.jpg -t "this text will appear bottom center" -p bottom_center

NB: use the inverted commas only when the text is made up of more than one word with spaces. meaning there is no need when entering the image size which is just one word
The arguments can come in any order except for the text and its position which must appear in order
this will run a test on the sample image in that folder
- For help on the various options run the command
	python3 Master.py -h 

