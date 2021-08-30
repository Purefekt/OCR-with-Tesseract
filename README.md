Prereqs
- Poppler installation instructions for different operating systems --> https://pypi.org/project/pdf2image/



Create conda env called **env_name**
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