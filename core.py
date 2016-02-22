import dominant_color
import search_in_3d_matrix
import random
from PIL import Image
import image_utils
from progressbar import Bar, ProgressBar, SimpleProgress


def verify_image_size_and_resize(image, tile_size):
    if image.size > (tile_size, tile_size):
        return image_utils.resize_image(image,(tile_size, tile_size))
    return image


def get_candidate_image(candidate_images, thumbs_folder):
    """
    :param candidate_images: array of filename
    :param thumbs_folder: folder containing thumbnails
    """
    output = None
    while not output and candidate_images:
        filename_candidate = candidate_images.pop(random.randrange(len(candidate_images)))
        output = image_utils.open_image(thumbs_folder + filename_candidate, "RGB")
    return output


def find_matching_picture(dominant_color, rgb_matrix_dataset, thumbs_folder, tile_size):
    """
    Find the best picture according to the dominant color
    :param dominant_color: rgb color object
    :param rgb_matrix_dataset: pictures dataset ordered in a matrix by rbg color
    :return: none if picture is not found, otherwise returns an image object
    """
    found_image = None
    empty_matrix = False
    while not found_image and not empty_matrix:
        best_cell = search_in_3d_matrix.find_nearest_match(rgb_matrix_dataset, dominant_color)
        if best_cell:
            candidate_images = rgb_matrix_dataset[best_cell.red][best_cell.green][best_cell.blue].split(',')
            found_image = get_candidate_image(candidate_images, thumbs_folder)
            if not found_image:
                # not exists image in the cell -> delete containt cell
                rgb_matrix_dataset[best_cell.red][best_cell.green][best_cell.blue] = None
        else:
            empty_matrix = True
    if found_image:
        return verify_image_size_and_resize(found_image, tile_size)

    return None


def replace_image(target_img, replacement_img, tile_size, x, y):
    """
    x: position x of the tile in the original image, y: position y of the tile in the original image
    """
    target_img.paste(replacement_img, (x * tile_size, y * tile_size, x * tile_size + tile_size, y * tile_size + tile_size))



def find_dominant_color_and_replace(grid_original_image, target_image, num_clusters, rgb_matrix_dataset, thumbs_folder, tile_size, use_images):
    total_tiles = len(grid_original_image) * len(grid_original_image[1])
    pbar = ProgressBar(widgets=[SimpleProgress(), Bar()], maxval=total_tiles).start()
    i = 0
    for x in range(len(grid_original_image)):
        for y in range(len(grid_original_image[1])):
            i += 1
            pbar.update(i)
            original_tile = grid_original_image[x][y]
            tile_dominant_color, _ = dominant_color.find_dominant_color_and_generate_thumb(original_tile, None, None, num_clusters, tile_size, False)
            if use_images:
                replacement_image = find_matching_picture(tile_dominant_color, rgb_matrix_dataset, thumbs_folder, tile_size)
            else:
                replacement_image = Image.new("RGB", (tile_size, tile_size), (tile_dominant_color.red, tile_dominant_color.green, tile_dominant_color.blue))

            replace_image(target_image, replacement_image, tile_size, x, y)
    pbar.finish()