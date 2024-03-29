def psnr(img1, img2):
    import numpy as np
    import math
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    pixel_max = 255.0

    return 20 * math.log10(pixel_max / math.sqrt(pixel_max))
