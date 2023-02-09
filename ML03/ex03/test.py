from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("../resources/elon_canaGAN.png")
print(arr)
#imp.display(arr)
cf = ColorFilter()
#imp.display(cf.invert(arr))
#imp.display(cf.to_green(arr))
#imp.display(cf.to_red(arr))
#imp.display(cf.to_blue(arr))
#imp.display(cf.to_celluloid(arr))
#imp.display(cf.to_grayscale(arr, 'm'))
#imp.display(cf.to_grayscale(arr, 'weight', weights=[0.2, 0.3, 0.5]))
