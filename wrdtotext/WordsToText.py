import cv2
import pytesseract
import re
import urllib.request
import numpy as np

def url_to_image(url):
    resp = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib.request.urlopen(resp)
    image = np.asarray(bytearray(con.read()), dtype="uint8")
    image2 = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image2

def img2text(URL):
    if re.findall('^http', URL):
        im = url_to_image(URL)
    else:
        im = cv2.imread(URL, cv2.IMREAD_COLOR)
    config = ('-l eng --oem 1 --psm 6')
    text = pytesseract.image_to_string(im, config=config)
    text2 = text.rstrip('\n')
    return (text2)



