import Image

DEFAULT_RESIZE_MODE = Image.ANTIALIAS

def resize(image, l, dimension='w', resize_mode=DEFAULT_RESIZE_MODE):
    """Resize the image.
    Parameters:
        * image
        * length
        * dimension to resize ('w' or 'h')
    """
    
    if dimension == 'w':
        new_width = l
        new_height = int(round(image.size[1]*l/float(image.size[0])))
    else:
        new_height = l
        new_width = int(round(image.size[0]*l/float(image.size[1])))
    
    return image.resize((new_width, new_height), resample=resize_mode)