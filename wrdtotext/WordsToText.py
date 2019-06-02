import cv2
import pytesseract
import re
import urllib.request
import numpy as np
import os
import pandas as pd

def url_to_image(url):
    resp = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib.request.urlopen(resp)
    image = np.asarray(bytearray(con.read()), dtype="uint8")
    image2 = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    return image2

def img2text(URL):
    if re.findall('^http', URL):
        im = url_to_image(URL)
    else:
        img = cv2.imread(URL)
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    config = ('-l eng --oem 1 --psm 6')
    text = pytesseract.image_to_string(im, config=config)
    text2 = text.rstrip('\n')
    return (text2)

def img2textdir(dirpath):
    files = []
    for file in os.listdir(dirpath):
        if file.endswith('.jpg') or file.endswith('.png'):
            files.append(os.path.join(dirpath, file))
    texts=[]
    names=[]
    for i in files:
        text=img2text(i)
        texts.append(text)
        names.append(i)
    translation={'Image':names, 'Text':texts}
    df=pd.DataFrame(data=translation)
    return df

