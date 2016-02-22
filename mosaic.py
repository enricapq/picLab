import glob
from os.path import basename
import core, dataset_thumbs, image_utils, dominant_color


def create_dataset(dataset_folder, thumbs_folder, ext, num_clusters, thumb_size):
    for pathfile in glob.iglob(dataset_folder + '/**/*', recursive=True):
        filename = basename(pathfile)
        if filename.endswith(tuple(ext)):
            image = image_utils.open_image(pathfile, "RGB")
            color, image = dominant_color.find_dominant_color_and_generate_thumb(image, filename, thumbs_folder,
                                                                                 num_clusters, thumb_size, True)
            dataset_thumbs.write_pic(color.red, color.green, color.blue, filename)
    return True


def pic_in_tiles(uri, thumbs_folder, mosaic_folder, mosaic_tile_size, num_clusters, ratio, use_images):
    """
    use_images: if True, each tile is replaced with an image else with dominant color
    """
    normalized_image = image_utils.enlarge_crop_img(uri, mosaic_tile_size, ratio)
    if not normalized_image:
        # img is too small
        return False
    target_image = image_utils.create_image("RGB", normalized_image.size, "white")
    grid_crops_original_image = image_utils.subdivide_img(normalized_image, mosaic_tile_size)
    rgb_matrix_dataset = dataset_thumbs.load_dataset_in_matrix()
    core.find_dominant_color_and_replace(grid_crops_original_image, target_image, num_clusters, rgb_matrix_dataset,
                                         thumbs_folder, mosaic_tile_size, use_images)
    image_utils.save_image(target_image, basename(uri), mosaic_folder)
    return True
