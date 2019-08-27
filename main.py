import cv2 as cv

class PencilSketch:
    """ Pencil sketch effect
        A class applies a pencil sketch filter to an image.
    """

    def __init__(self, width, height, bg_gray='canvas.jpg'):
        """Initialize parameters
            :param width: Image width.
            :param height: Image height.
        """
        self.width = width
        self.height = height

        self.canvas = cv.imread(bg_gray, cv.CV_8UC1)
        if self.canvas is not None:
            self.canvas = cv.resize(self.canvas, (self.height, self.width))

    def render(self, img_rgb):
        """Applies pencil sketch effect to an RGB image
            :param self: RGB image to be processed
            :returns: Processed RGB image
        """

        img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)      #convert the color image to greyscale
        img_blur = cv.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)    #reduce noice to smooth the image

        #dividing grayscale value of an pixel image[col, row] by the inverse of the pixel value of mask[col, row]
        #resulting pixel value should be in the range [0,255] and do not divide by zero, cv divide does the trick
        #making the result 0 where 255-mask is zero
        img_blend = cv.divide(img_gray, img_blur, scale=256)

        #belnding the image to be blended with an empty canvas
        if self.canvas is not None:
            img_blend = cv.multiply(img_blend, self.canvas, scale=1 / 256)


        return cv.cvtColor(img_blend, cv.COLOR_GRAY2RGB)

image_name = input("Enter image name for pencil effect: ")
canvas_name = input("Enter image name of canvas: ")

image_rgb = cv.imread(image_name)
image_canvas = cv.imread(canvas_name)

width,height = image_rgb.shape[:2]

image = PencilSketch(width,height).render(image_rgb)
cv.imwrite("convert_img1.png",image)
