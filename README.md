# OCR with Tesseract
This project uses poetry for virtual environment and package management. First install poetry on your machine. Once installed, open terminal and cd to this directory and run ```poetry install```. This will install all the neccessary dependencies. If you get an error then run ```poetry install``` again since poppler needs cmake to be installed which will be installed in the first installation, then it should work.

## Checking the virtual environment and python interpreter
Poetry stores the virtual environment in the following directories based on the type of system:
- Unix - ```~/.cache/pypoetry/virtualenvs```
- MacOS - ```~/Library/Caches/pypoetry/virtualenvs```
- Windows - ```C:\Users\<username>\AppData\Local\pypoetry\Cache\virtualenvs or %LOCALAPPDATA%\pypoetry\Cache\virtualenvs```

You can also cd to the project directory in terminal and ```poetry env info``` will show you this information.  
You must change the python interpreter to this in order to run this in the text editor/IDE of your choice.

## Running the project