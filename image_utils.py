from PIL import Image, ImageFile
import scipy
import scipy.misc
import numpy as np

ImageFile.LOAD_TRUNCATED_IMAGES = True


def open_image(uri, image_mode="RGB"):
    try:
        im = Image.open(uri)
    except:
        return None
    if im.mode != image_mode:
        im = im.convert(image_mode)
    return im


def save_image(image, filename_with_ext, path):
    image.save(path + filename_with_ext)
    return True


def create_image(mode, size, color=0):
    return Image.new("RGB", size, color)


def resize_image(image, thumb_size):
    """ tuple (width, height) """
    return image.resize(thumb_size)


def convert_scipy_image_to_n_colors(ar, shape, codes, vecs):
    # convert image with the n most-frequent colors:
    for i, code in enumerate(codes):
        ar[scipy.r_[scipy.where(vecs == i)], :] = code
    return scipy.misc.toimage(ar.reshape(*shape))


def subdivide_img(source_image, dim_tile):
    width, height = source_image.size
    rows = int(height / dim_tile)
    columns = int(width / dim_tile)
    grid = [[None for w in range(rows)] for h in range(columns)]
    for x in range(columns):
        for y in range(rows):
            grid[x][y] = source_image.crop(
                (x * dim_tile, y * dim_tile, x * dim_tile + dim_tile, y * dim_tile + dim_tile))
    return grid


def enlarge_crop_img(uri, thumb_size, ratio):
    img = open_image(uri, image_mode="RGB")
    if (img.size[0] < thumb_size) or (img.size[1] < thumb_size):
        # image too small
        return None
    mod_width = img.size[0] % thumb_size
    mod_height = img.size[1] % thumb_size
    if mod_width != 0 or mod_height != 0:
        new_width = img.size[0] - mod_width
        new_height = img.size[1] - mod_height
        width = np.size(img, 1)
        height = np.size(img, 0)
        left = int(np.floor((width - new_width) / 2.))
        top = int(np.floor((height - new_height) / 2.))
        right = int(np.floor((width + new_width) / 2.))
        bottom = int(np.floor((height + new_height) / 2.))
        img = img.crop((left, top, right, bottom))
    new_width = img.size[0] * ratio
    new_height = img.size[1] * ratio
    return img.resize((new_width, new_height))
