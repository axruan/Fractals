# Alex Ruan
# CS550
# On my honor, I have neither given nor recieved unauthorized aid.
# Sources: Class code from 10/19 and YouTube video explaining the Julia set and the algorithm
# python3.codes/fractal-tree/ for the rainbow-y part
# colorsys documentation for implementing the colorsys module
# http://www.comfsm.fm/~dleeling/cis/hsl_rainbow.html to help me understand how hsl/hsv worked
# I did the Mandelbrot and Julia sets. I chose the Julia set because I had a lot of difficulty with fractals, so I wanted to build off some pre-existing code/math. This also gave me some more time to mess around with the colors and how to zoom correctly.

from PIL import Image
import colorsys

# Creates image width and height
imgx, imgy = 512, 512

# Defines the max iterations
maxIter = 256

# Initializes each image
m1 = Image.new("RGB", (imgx, imgy))
m2 = Image.new("RGB", (imgx, imgy))
j = Image.new("RGB", (imgx, imgy))

# Mandelbrot function that accepts the bounds for the image and the image name
def mandelbrot(xmin, xmax, ymin, ymax, image, name):

    # The Mandelbrot set math
    for y in range(imgy):
        cy = y * (ymax - ymin)/(imgy - 1) + ymin
        for x in range(imgx):
            cx = x * (xmax - xmin)/(imgx - 1) + xmin
            c = complex(cx, cy)
            z = 0
            for i in range(maxIter):
                if abs(z) > 2.0:
                    break
                z = z**2 + c

            # Creates the "peppermint" effect
            h = int(i*3.6)
            s = i
            v = i
            colorsys.hsv_to_rgb(h, s, v)
            image.putpixel((x, y), (h, s, v))

    # Creates the image
    image.save(name, "JPEG")

# Julia function that accepts bounds for the image
def julia(xmin, xmax, ymin, ymax):
    # The Julia set math
    for y in range(imgy):
        cy = y * (ymax - ymin)/(imgy - 1) + ymin
        for x in range(imgx):
            cx = x * (xmax - xmin)/(imgx - 1) + xmin
            c = complex(cx, cy)
            z = c
            for i in range(maxIter):
                if abs(z) > 2.0:
                    break
                z = z**2 + complex(-0.1, 0.651)

            # Creates the color effect
            h = int(i%3.6)
            s = i
            v = 50
            colorsys.hsv_to_rgb(h, s, v)
            j.putpixel((x, y), (h, s, v))

    # Creates the image
    j.save("julia.png", "PNG")


# Calls the fractal functions
mandelbrot(-0.55, -0.5, -0.7, -0.65, m1, "m1.png")
mandelbrot(0.37, 0.38, 0.29, 0.3, m2, "m2.png")
julia(-0.6, 0.6, -0.6, 0.6)
