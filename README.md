# Summary
This repository contains modules for basic ocr on image and pdf, correcting skew in scanned documents, auto noise type detector and noise reduction and watermark removal. Detailed examples on how to use these modules are given in seperate jupyter notebooks and how the code is working is detailed in pdf documentation.

## Prerequisite
- Tesseract
    - Mac -> ```brew install tesseract```
    - Linux -> ```sudo apt-get install tesseract-ocr```
- Poppler installation instructions for different operating systems --> https://pypi.org/project/pdf2image/


## Install with Conda
Create conda env called **env_name** (or any name)
```
conda create --name env_name python=3.8
```
activate this environment
```
conda activate env_name
```
Clone this repo and cd to the repository directory, then run this command to install all packages
```
conda install --file requirements.txt --channel default --channel anaconda --channel conda-forge
```
Once all packages are installed, use this command to add conda environment to jupyter notebook as a kernel
```
python -m ipykernel install --user --name=env_name
```

## Summary on all files in this repo
```
/
├── CREATE AGAIN
```

- ```assets/``` -> directory containing pdf and image files which are used to demo the modules
- ```modules/noise_reduction_apply.py``` -> class where 