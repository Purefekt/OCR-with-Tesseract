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
Project root/
├── assets/
│   ├── ...
├── other_scripts/
│   ├── ....
├── modules/
│   ├── __init__.py
│   ├── noise_reduction_apply.py
│   ├── noise_type_detector.py
│   ├── ocr.py
│   ├── orientation_correction.py
│   └── watermark_removal.py
├── pdf_documentation/
│   ├── Automatic_Noise_Detection_and_Removal_Pipeline.pdf
│   ├── Gaussian_Noise_Removal.pdf
│   ├── Orientation_Correction.pdf
│   └── Watermark_removal.pdf
├── README.md
├── requirements.txt
└── watermark_stain_removal_example.ipynb
├── noise_detection_and_reduction_pipeline.ipynb
├── ocr_example.ipynb
├── orientation_correction_example.ipynb
```

- ```assets/``` -> directory containing pdf and image files which are used to demo the modules
- ```other_scripts/``` -> directory containing extra scripts which were used to prototype the different modules
- ```modules/noise_reduction_apply.py``` -> class with methods to remove noise from images
- ```modules/noise_type_detector.py``` -> class with methods to identify if the noise in an image is gaussian or impulse
- ```modules/ocr.py``` -> class with methods to run OCR on single image or entire pdf
- ```modules/orientation_correction.py``` -> class with methods to identify angle of skew and correct the orientatio by rotating the image
- ```modules/watermark_removal.py``` -> class with method to remove watermarks from scanned documents
- ```pdf_documentation/Automatic_Noise_Detection_and_Removal_Pipeline.pdf``` -> this pdf explains how the automatic noise detection and removal pipeline works
- ```pdf_documentation/Gaussian_Noise_Removal.pdf``` -> this pdf explains how i implemented a new gaussian noise removal algorithm from the given paper
- ```pdf_documentation/Orientation_Correction.pdf``` -> this pdf explains how the orientation correction works and how well it works at different angles of skew
- ```pdf_documentation/Watermark_removal.pdf``` -> this pdf explains how the watermark removal works
- ```requirements.txt``` -> package information for installation with conda
- ```watermark_stain_removal_example.ipynb``` -> jupyter notebook explaining how to use the ```watermark_removal.py``` module
- ```noise_detection_and_reduction_pipeline.ipynb``` -> jupyter notebook explaining how to use the ```noise_type_detector.py``` and ```noise_reduction_apply.py``` modules
- ```ocr_example.ipynb``` -> jupyter notebook explaining how to use the ```ocr.py``` module
- ```orientation_correction_example.ipynb``` -> jupyter notebook explaining how to use the ```orientation_correction.py``` module