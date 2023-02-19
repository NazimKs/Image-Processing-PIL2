# -*- coding: utf-8 -*-
"""! This file contains the main procedure to execute the methods used in this activity.
@author KESKES Nazim
@version 1.0.0
@since October 7, 2022
"""
# Initialization
from PIL.Image import *

def photobooth(image):
    """! Function allowing the photobooth transformation of an image.
         @param image.
         @return photobooth image
    """
    # Get the width and height of the image
    (l, h) = image.size
    # Create a new image called new_image of size (l,h) all black.
    new_image = new('RGB', (l, h))
    for x in range(l):
        for y in range(h):
            # Get the color value of the pixel located on line y and column x of the image
            c = Image.getpixel(image, (x, y))
            # If x and y are even
            if x % 2 == 0 and y % 2 == 0:
                Image.putpixel(new_image, (x // 2, y // 2), c)
            # If x is odd and y is even
            elif x % 2 == 1 and y % 2 == 0:
                Image.putpixel(new_image, (x // 2 + l // 2, y // 2), c)
            # If x is even and y is odd
            elif x % 2 == 0 and y % 2 == 1:
                Image.putpixel(new_image, (x // 2, y // 2 + h // 2), c)
            # If x and y are odd
            else:
                Image.putpixel(new_image, (x // 2 + l // 2, y // 2 + h // 2), c)
    # Return the resulting image
    return new_image

def stretching(image):
    """! Function allowing the stretching of an image.
        @param image.
        @return stretched image
    """
    # Get the width and height of the image
    (l, h) = image.size
    # Create a new image called new_image of size (2l,h/2) all black.
    new_image = new('RGB', (2 * l, h // 2))
    for x in range(l):
        for y in range(h):
            # Get the color value of the pixel located on line y and column x of the image
            c = Image.getpixel(image, (x, y))
            # If y is even
            if y % 2 == 0:
                Image.putpixel(new_image, (2 * x, y // 2), c)
            # If y is odd
            else:
                Image.putpixel(new_image, (2 * x + 1, y // 2), c)
    # Return the stretched image
    return new_image

def folding(image):
    """! Function that folds an image.
        @param image.
        @return folded image
    """
    # Get the width and height of the image
    (l, h) = image.size
    # Create a new image named new_image of size (l/2,2h) that is all black.
    new_image = new('RGB', (l // 2, 2 * h))
    for x in range(l):
        for y in range(h):
            # Get the color value of the pixel located in row y and column x of the image
            c = Image.getpixel(image, (x, y))
            # If x is less than l//2
            if x < l // 2:
                Image.putpixel(new_image, (x, y), c)
            # If x is greater than or equal to l//2
            else:
                Image.putpixel(new_image, (l - x - 1, 2 * h - 1 - y), c)
    # Return the folded image
    return new_image


def baker(image):
    """! Function that creates a baker's transform of an image.
        @param image.
        @return baker's transformed image
    """
    # To transform an image using the baker's transform, first stretch the image and then fold it
    return folding(stretching(image))


def main() -> None:
    """Function allowing the execution of the sequence of operations of this activity."""
    # Open the image
    image = open("assets/joconde.png","r")
    # Show the initial image
    Image.show(image)
    # Show the image transformed into photobooth
    image_photobooth = photobooth(image)
    Image.show(image_photobooth)
    # Show the image transformed into baker
    image_baker = baker(image)
    Image.show(image_baker)
    # Apply the baker transformation to the initial image 19 times
    for i in range(19):
        image = baker(image)
        Image.show(image)
        # Note: the result after the 17th iteration gives us the original image, which is impressive.
    # Close the image
    image.close()

    # Test with another image
    image2 = open("assets/lena.png", "r")
    # Show the initial image
    Image.show(image2)
    # Apply the baker transformation to the other image 19 times
    for i in range(19):
        image2 = baker(image2)
        Image.show(image2)
    # Close image 2
    image2.close()

if __name__ == "__main__":
    main()
