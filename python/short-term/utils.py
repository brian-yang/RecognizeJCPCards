import matplotlib.pyplot as plt
import cv2
import numpy as np
import constants

'''
Validate the card number based on:
1. the Luhn algorithm for Mastercards
2. the special formatting rules for PLCC cards
'''
def validate_card_num(card_num):
    # Replace all spaces to avoid inconsistency
    card_num = card_num.replace(" ", "")

    # Checks if the card number satisfies the conditions for each credit card type
    found_mastercard = len(card_num) == 16 and is_mastercard_num(card_num)
    found_plcc = len(card_num) == 11 and is_plcc_num(card_num)

    if found_mastercard:
        return card_num, True, constants.MASTERCARD
    elif found_plcc:
        return card_num, True, constants.PLCC
    else:
        return card_num, False, constants.INVALID

'''
Runs the Luhn algorithm on the card number
to see if the credit card is a Mastercard.
'''
def is_mastercard_num(card_num):
    try:
        digits = list(map(int, card_num))
    except:
        return False

    evens = sum(digit for digit in digits[-1::-2])
    odds = sum(constants.LUHN_ODD_LOOKUP[digit] for digit in digits[-2::-2])

    return (evens + odds) % 10 == 0

'''
Checks the special formatting rules for the PLCC
to see if the credit card is a PLCC.

(For now, this is just checking if all the characters in the
input string are digits)
'''
def is_plcc_num(card_num):
    try:
        s = list(map(int, card_num))
    except:
        return False

    return True

'''
Apply OpenCV image operations to prepare the credit card image
to be fed into Google Tesseract.
'''
def prepare_img_for_tesseract(img):
    # Apply Otsu binary thresholding to create a black-white img.
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

    # Now the card text is white on a black background.
    # Invert the image so that the text is black on a white background.
    img = 255 - img

    # Apply Gaussian filtering to remove image noise.
    kernel_size = 3
    kernel = np.ones((kernel_size, kernel_size), np.float32) / \
        kernel_size/kernel_size
    img = cv2.filter2D(img, -1, kernel)

    return img

'''
Loads an image based on the given image filename
as a grayscale image.
'''
def load_img_as_grayscale(img_file):
    return cv2.imread(img_file, 0)

'''
Verifies that the credit card is oriented correctly (ie. not rotated sideways). 
If not, rotate the image so that the credit card number
is upright. (see images in the images folder for examples of rotated card images)
'''
def verify_card_orientation(img):
    rows, cols = img.shape[0:2]
    if rows > cols:
        return np.rot90(img)
    else:
        return img

'''
Draws the image so that as the credit card image is processed,
you can see how it looks in each step.
'''
def draw(img):
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    plt.imshow(img)
    plt.show()