import scipy
import scipy.misc
import scipy.cluster
from pixelcolor import PixelColor
from image_utils import resize_image, convert_scipy_image_to_n_colors, save_image


def calculate_dominant_colors(image, num_clusters):
    ar = scipy.misc.fromimage(image)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])
    codes, _ = scipy.cluster.vq.kmeans(ar.astype(float), num_clusters)
    vecs, _ = scipy.cluster.vq.vq(ar, codes)
    return ar, shape, codes, vecs


def calculate_dominant_color_from_clusters(codes, vecs):
    counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences
    index_max = scipy.argmax(counts)  # find most frequent
    peak = codes[index_max]
    return PixelColor(int(peak[0]), int(peak[1]), int(peak[2]))


def find_dominant_color_and_generate_thumb(image, pic, thumbs_folder, num_clusters, thumb_size, save_thumb):
    """
    Find dominant color of a picture and returns color
    If save_thumb is True than create and save thumbnail with the num_clusters common colors
    """
    image = resize_image(image, (thumb_size, thumb_size))
    ar, shape, codes, vecs = calculate_dominant_colors(image, num_clusters)
    dominant_color = calculate_dominant_color_from_clusters(codes, vecs)
    if save_thumb:
        im = convert_scipy_image_to_n_colors(ar, shape, codes, vecs)
        if save_image(im, pic, thumbs_folder):
            return dominant_color, im
        else:
            return None, None
    else:
        return dominant_color, None
