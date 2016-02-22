from os.path import basename
import image_utils


def to_gray_and_save_pic(uri, elaborated_folder):
    image = image_utils.open_image(uri, "RGB")
    if not image:
        return False
    else:
        if image.format == "PNG":
            image = image.convert('LA')
        else:
            image = image.convert('L')
        image_utils.save_image(image, basename(uri), elaborated_folder)
        return True


def resize_and_save_pic(uri, width, height, elaborated_folder):
    image = image_utils.open_image(uri, "RGB")
    image = image_utils.resize_image(image, (width,height))
    image_utils.save_image(image, basename(uri), elaborated_folder)
    return True


def make_linear_ramp():
    ramp = []
    for i in range(int(255)):
        outputRed = int((i * .393) + (i *.769) + (i * .189))
        if outputRed > 255:
            outputRed =255
        outputGreen = int((i * .349) + (i *.686) + (i * .168))
        if outputGreen > 255:
            outputGreen =255
        outputBlue = int((i * .272) + (i *.534) + (i * .131))
        if outputBlue > 255:
            outputBlue = 255
        ramp.extend((int(outputRed), int(outputGreen), int(outputBlue)))
    return ramp



def to_sepia_and_save_pic(uri, elaborated_folder):
    """
    Convert before in grayscale and then in sepia
    """
    img = image_utils.open_image(uri, "RGB")
    if img:
        orig_mode = img.mode
        if orig_mode != "L":
            img = img.convert("L")
        sepia = make_linear_ramp()
        img.putpalette(sepia)
        img = img.convert(orig_mode)
        image_utils.save_image(img, basename(uri), elaborated_folder)
        return True
    else:
        return False