import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
import os
from PIL import Image

def show(img, figsize=(10, 10), title="Image"):
    figure=plt.figure(figsize=figsize)
    
    plt.imshow(img)
    plt.show()


# read graysclae img
def RLE_encoding(img, bits=8,  binary=True, view=True):
    """
    img: Grayscale img.
    bits: what will be the maximum run length? 2^bits       
    """
    image = Image.open(img, 'r')
    if binary:
        ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    if view:
        show(img)

    encoded = []
    shape=img.shape
    count = 0
    prev = None
    fimg = img.flatten()
    th=127
    for pixel in fimg:
        if binary:
            if pixel<th:
                pixel=0
            else:
                pixel=1
        if prev==None:
            prev = pixel
            count+=1
        else:
            if prev!=pixel:
                encoded.append((count, prev))
                prev=pixel
                count=1
            else:
                if count<(2**bits)-1:
                    count+=1
                else:
                    encoded.append((count, prev))
                    prev=pixel
                    count=1
    encoded.append((count, prev))
    
    return np.array(encoded)
fpath="D:\python_hide_information\Hiding_information_using_ML\ste_in_img\decode.png"
img = cv2.imread(fpath, 0)
shape=img.shape
encoded = RLE_encoding(img, bits=8)
encoded
def RLE_decode(encoded, shape):
    decoded=[]
    for rl in encoded:
        r,p = rl[0], rl[1]
        decoded.extend([p]*r)
    dimg = np.array(decoded).reshape(shape)
    return dimg

dimg = RLE_decode(encoded, shape)
show(dimg) 
# save the encoded list into npz array file
earr=np.array(encoded)
# earr=earr.astype(np.uint8)
np.savez("np1.npz", earr)
np.save("np2.npz", earr)
# store that array as image
# the earr has shape of (x, 2) which can work fine as an image.
cv2.imwrite("encoded.tif", earr)
cv2.imwrite("encoded.png", earr)
rencd = cv2.imread("encoded.tif", -1)
show(RLE_decode(rencd, shape))