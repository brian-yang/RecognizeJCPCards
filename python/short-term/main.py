import sys
import cv2
import pytesseract
import utils
import constants

'''
Extracts the card number and cardholder name
from the credit card image.

If the card number is valid, the function returns:
    1. Card number
    2. Card validity (which is going to be true)
    3. Card type
    4. Cardholder name
'''
def get_credit_card_info(img_file):
    img = utils.load_img_as_grayscale(img_file)
    img = utils.verify_card_orientation(img)

    # Resize to standard credit card dimensions
    img = cv2.resize(img, (constants.STANDARD_CARD_WIDTH, constants.STANDARD_CARD_HEIGHT))

    # Get card number region of interest
    card_number_pic = img[430:490, 50:600]
    card_number_pic = utils.prepare_img_for_tesseract(card_number_pic)
    card_number_str = pytesseract.image_to_string(card_number_pic, config=constants.TESSERACT_CONFIG)

    # Validate card number
    card_number_str, card_valid, card_type = utils.validate_card_num(card_number_str)
    if not card_valid:
        return {
            "card_number": card_number_str,
            "card_validity": constants.INVALID
        }

    # Get cardholder name region of interest
    if card_type == constants.PLCC:
        card_holder_pic = img[360:425, 50:800]
    elif card_type == constants.MASTERCARD:
        card_holder_pic = img[290:360, 50:750]
    else:
        card_holder_pic = img

    card_holder_pic = utils.prepare_img_for_tesseract(card_holder_pic)
    card_holder_str = pytesseract.image_to_string(card_holder_pic)

    # Remove invalid characters (the hyphen '-', the space ' ') 
    # in the beginning and end of the name
    while card_holder_str[0] in " -":
        card_holder_str = card_holder_str[1:]
    while card_holder_str[-1] in " -":
        card_holder_str = card_holder_str[:-1]

    return {
        "card_number": card_number_str,
        "card_validity": card_valid,
        "card_type": card_type,
        "card_holder": card_holder_str
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_file = sys.argv[1]
        print(get_credit_card_info(img_file))
