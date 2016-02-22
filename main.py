import sys
from configparser import ConfigParser
import operations_ui
import utils, mosaic


class PicLab:

    def print_menu(self):
        while True:
            print('''\nType the number of the desired operation
                     (1) Convert to grayscale
                     (2) Resize image
                     (3) Convert to sepia
                     (4) Create pixelated image
                     (5) Create dataset of pictures
                     (6) Create mosaic of pictures
                     (0) Quit''')
            number = input('Choose a number: ')
            self.operation_dispatcher(number)


    def operation_dispatcher(self, number):
        if number == '1':
            result = operations_ui.insert_input_graycolor_image(self.elaborated_folder)
        elif number == '2':
            result = operations_ui.insert_input_resize_image(self.elaborated_folder)
        elif number == '3':
            result = operations_ui.insert_input_sepia_image(self.elaborated_folder)
        elif number == '4':
            result = operations_ui.insert_input_pixelated_image(self.thumbs_folder, self.mosaic_folder, self.mosaic_tile_size, self.num_clusters, self.ratio)
        elif number == '5':
            result = mosaic.create_dataset(self.dataset_folder, self.thumbs_folder, self.ext, self.num_clusters, self.thumb_size)
        elif number == '6':
            result = operations_ui.insert_input_mosaic_image(self.thumbs_folder, self.mosaic_folder, self.mosaic_tile_size, self.num_clusters, self.ratio)
        elif number == '0':
            sys.exit()
        else:
            print('Operation not valid')

        if result:
            print('operation completed successfully')


    def __init__(self):
        config = ConfigParser()
        config.read('picLab.ini')
        self.elaborated_folder = (config.get('PATH', 'elaborated_folder'))
        self.thumbs_folder = (config.get('PATH', 'thumbs_folder'))
        self.mosaic_folder = (config.get('PATH', 'mosaic_folder'))
        self.dataset_folder = (config.get('PATH', 'dataset_folder'))
        self.ext = (config.get('PIC_INFO', 'ext')).split(',')
        self.thumb_size = int(config.get('MOSAIC', 'thumb_size'))
        self.ratio = int(config.get('MOSAIC', 'ratio'))
        self.mosaic_tile_size = int(config.get('MOSAIC', 'mosaic_tile_size'))
        self.num_clusters = int(config.get('MOSAIC', 'num_clusters'))
        if not utils.check_path_validity_traversable(self.elaborated_folder):
            print("Paths in config are not valid")
            sys.exit()
        self.print_menu()


if __name__ == '__main__':
    PicLab()

