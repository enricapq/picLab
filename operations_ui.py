import utils, transformer, mosaic


def ask_input_image_uri(message):
    while True:
        uri = input(message)
        if not utils.check_file_exists(uri):
            print('URI not valid')
            return False
        else:
            return uri


def ask_input_dir_uri(message):
    while True:
        uri = input(message)
        if not utils.check_path_validity_traversable(uri):
            print('URI not valid')
            return False
        else:
            return uri


def ask_input_integer(message):
    while True:
        integer = input(message)
        try:
            casted_integer = int(integer)
            return casted_integer if casted_integer > 0 else print("Value is zero or negative")
        except:
            print("Value is not a valid integer")


def insert_input_resize_image(elaborated_folder):
    uri = None
    width = None
    height = None
    while not uri:
        uri = ask_input_image_uri('Type the URI of the image you want to edit: ')
    while not width:
        width = ask_input_integer('Type the width: ')
    while not height:
        height = ask_input_integer('Type the height: ')
    return transformer.resize_and_save_pic(uri, width, height, elaborated_folder)


def insert_input_graycolor_image(elaborated_folder):
    uri = ask_input_image_uri('Type the URI of the image you want to edit: ')
    if uri:
        return transformer.to_gray_and_save_pic(uri, elaborated_folder)
    else:
        return False


def insert_input_sepia_image(elaborated_folder):
    uri = ask_input_image_uri('Type the URI of the image you want to edit: ')
    if uri:
        return transformer.to_sepia_and_save_pic(uri, elaborated_folder)
    else:
        return False


def insert_input_pixelated_image(thumbs_folder, mosaic_folder, mosaic_tile_size, num_clusters, ratio):
    uri = ask_input_image_uri('Type the URI of the image you want to edit: ')
    if uri:
        return mosaic.pic_in_tiles(uri, thumbs_folder, mosaic_folder, mosaic_tile_size, num_clusters, ratio, False)
    else:
        return False


def insert_input_mosaic_image(thumbs_folder, mosaic_folder, mosaic_tile_size, num_clusters, ratio):
    uri = ask_input_image_uri('Type the URI of the image you want to edit: ')
    if uri:
        return mosaic.pic_in_tiles(uri, thumbs_folder, mosaic_folder, mosaic_tile_size, num_clusters, ratio, True)
    else:
        return False