# Standard credit card size: 85.6mm * 53.9mm
# In pixels: 856px * 540px
STANDARD_CARD_WIDTH = 856
STANDARD_CARD_HEIGHT = 540

# Configures Google Tesseract to look for digits
TESSERACT_CONFIG = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'

# For the Luhn algorithm
LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)

# String constants
MASTERCARD = "Mastercard"
PLCC = "Private Card"
INVALID = "Invalid"