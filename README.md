# About
This project was designed to test out flat credit card scanning with OpenCV and Tesseract. Currently, the short term solution is written in Python. The C++ files and `long-term.py` currently contain some experimentation we were doing with neural networks.

# How the short term solution works (the Python version)
1. The image is read into the program and converted into grayscale.
2. We find regions of interest (ROI), namely regions containing the credit card number and cardholder name on the image.
3. Once we have the ROIs, we perform some image operations (converting it into a black and white image, removing image noise with thresholding, etc.) to prepare it for optical character recognition (OCR) with Tesseract.
4. After the image processing is done, we feed the image into Tesseract.
5. Tesseract returns the text that it was able to extract from the image.
6. We find the card number and cardholder name from the text returned by Tesseract.

# Install
## Python version
1. Run `python -m pip install requirements.txt`
## C++ version
1. Install OpenCV 3.4.3 or greater. [[For Mac](https://www.learnopencv.com/install-opencv3-on-macos/)] [[For Ubuntu 16.04](http://www.codebind.com/cpp-tutorial/install-opencv-ubuntu-cpp/)]
# Run 
## Python version
1. To run the short term solution, do `python main.py <path_to_image>` in the `python/short-term/` directory
2. To run the long term experimental solution, do `python main.py --east frozen_east_text_detection.pb --image <path_to_image> --padding 0.05` in the `python/long-term` directory
# C++ version
1. Run `make` to compile.
2. Then run `./main --model=frozen_east_text_detection.pb --input=<path_to_image>` in the `c++/` directory (this is for the long term solution - currently used for experimental purposes)
