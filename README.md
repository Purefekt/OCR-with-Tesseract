# OCR with Tesseract

## Pre-requisites
- [Python3](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)
- [Tesseract](https://guides.library.illinois.edu/c.php?g=347520&p=4121425)

First you must install "Poppler", on macos install it easily with homebrew ```brew install poppler```, or follow this [link](http://macappstore.org/poppler/) for more details.  
This project uses poetry for virtual environment and package management. Open terminal and cd to this directory and run ```poetry install```. This will install all the neccessary dependencies.

## Checking the virtual environment and python interpreter
Poetry stores the virtual environment in the following directories based on the type of system:
- Unix - ```~/.cache/pypoetry/virtualenvs```
- MacOS - ```~/Library/Caches/pypoetry/virtualenvs```
- Windows - ```C:\Users\<username>\AppData\Local\pypoetry\Cache\virtualenvs or %LOCALAPPDATA%\pypoetry\Cache\virtualenvs```

You can also cd to the project directory in terminal and ```poetry env info``` will show you this information.  
You must change the python interpreter to this in order to run this in the text editor/IDE of your choice.

## Running the project