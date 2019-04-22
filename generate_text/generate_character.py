import cv2
from random import randint
import numpy as np
from PIL import ImageFont, ImageDraw, Image, ImageFilter

def main():
    fontPath = "./ARIALUNI.ttf"

    img = drawChar(u"\u262f", 12, fontPath)
    cv2.namedWindow("Character Display")  # Create a window for display.
    cv2.imshow("Character Display", img)  # Show our image inside it.
    cv2.waitKey(0)                      # Wait for a keystroke in the window
    return 0



def build_28x28_white_image():
    img = np.zeros((28, 28, 3), np.uint8)
    img[:] = tuple(reversed((255, 255, 255)))
    return img


#
def randomize_location(font_obj, chars, out_of_bounds_threshold=0, x_range=28, y_range=28):
    width = font_obj.getsize(chars)[0]
    height = font_obj.getsize(chars)[1]
    print("Text width: " + str(width) + "\nText height: " + str(height))

    x_max = (x_range + out_of_bounds_threshold) - width
    y_max = (y_range + out_of_bounds_threshold) - height
    x_start = 0 - out_of_bounds_threshold
    y_start = 0 - out_of_bounds_threshold

    rand_x_coord = randint(x_start, x_max)
    rand_y_coord = randint(y_start, y_max)

    return rand_x_coord, rand_y_coord



def drawChar(chars, font_size, font_path, openCV=False, color=(0, 0, 0), base_image=build_28x28_white_image()):
    font = ImageFont.truetype(font_path, font_size)

    random_location_x, random_locaiton_y = randomize_location(font, chars)


    print("Random location of x: " + str(random_location_x) + "\nRandom location of Y: " + str(random_locaiton_y))
    img_PIL = Image.fromarray(base_image)
    draw_PIL = ImageDraw.Draw(img_PIL)
    coordinates = (random_location_x,random_locaiton_y) # Top-left of character
    draw_PIL.text(coordinates, chars, font=font, fill=color)
    base_image = np.array(img_PIL)

    return base_image

main()
