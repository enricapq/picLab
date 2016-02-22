# picLab

A simple [Python 3](https://www.python.org/download/releases/3.0/) project to elaborate pictures and create mosaic of images


## Overview
Main operations available:

* Convert to grayscale
* Resize Image
* Convert to sepia tone
* Create pixelated image
* Create mosaic of pictures


## Requirements

* install [Pillow](https://pypi.python.org/pypi/Pillow)
* install [NumPy] (http://www.numpy.org/)
* install [SciPy] (http://www.scipy.org/scipylib/)
* install [progressbar33] (https://pypi.python.org/pypi/progressbar33/)

## Configure

In the file picLab.ini specify the variables:

`dataset_folder` path of the folder containing the images (4000 is a good number) to use to create mosaic of pictures
`thumbs_folder` path of the folder containign the saved thumbs
`elaborated_folder` path of the folder containing the elaborated images
`mosaic_folder` path of the folder containing the mosaic

`ratio` ratio between the size of the final mosaic picture and the initial image
`mosaic_tile_size` size of the square tile that will compose the mosaic


## Run program

Start the program typing `python main.py`