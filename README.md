# youtube_downloader

A script to download videos from youtube.

Modules used:
* bs4
* requests
* pytube

## Usage

You will need a python interpreter to use this scipt. Run the script and enter the name of the video you want to to download.
The video will be downloaded to the directory in which you executed the script.

More updates to this will be comin soon.

I plan to make this a CLA and add many more features.

## Update into a CLA

This scipt have been modified to function as a command line application. Youcan still che ck the original file as it's still there as 'main.py'
While the new files added are 'ytd.py' and 'setup.py'. 

The Module added is:
* click

### Installation

You will need to use your command line to cd into the directory in which you copied the files and then use:

	pip install --editable .

### Using the Command

The synatx of the command is:

    ytd "your search"

And it will download the video to you folder for you. You can also select the directory you want to download the file to by using the option -d:

    ytd -d "address_of_the_directory" "your search" 