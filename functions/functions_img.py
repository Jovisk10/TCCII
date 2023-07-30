from PIL import Image
import streamlit as st
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Definição as funções utilizadas para realizar o processamento das imagens

def brighten_img(image, value): #Função de brilho em imagem estática
    img_bright = cv.convertScaleAbs(image, beta=value, alpha=1)
    return img_bright

def threshold_img(image, value):# Função de Limiarização em imagem estática
    ret, img_out = cv.threshold(image, value, 255, cv.THRESH_BINARY)
    img = Image.fromarray(img_out)
    return img

def contrast_img(image, value): #Função de Contraste em imagem estática
    img_contrast = cv.convertScaleAbs(image, alpha=value)
    return img_contrast

def sobel_img(image, value1, value2, component):

    if component == 'x':
        img_sobel = cv.Sobel(src=image, ddepth=cv.CV_64F, dx=value1, dy=0, ksize=3) 

    elif component == 'y':
        img_sobel = cv.Sobel(src=image, ddepth=cv.CV_64F, dx=0, dy=value2, ksize=3) 

    elif component == 'xy':
        img_sobel = cv.Sobel(src=image, ddepth=cv.CV_64F, dx=value1, dy=value2, ksize=3)

    img = Image.fromarray(img_sobel)
    img = img.convert("L")
    return img

def canny_img(image, value1, value2):
    img_canny = cv.Canny(image, value1, value2)
    img = Image.fromarray(img_canny)
    return img

def channel_rgb(image, channel):
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    canalAzul, canalVerde, canalVermelho = cv.split(image)

    if channel == 'b':
        return canalAzul
    
    elif channel == 'g':
        return canalVerde
    
    elif channel == 'r':
        return canalVermelho

def channel_ycbcr(image, channel):
    image = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    canaly, canalcb, canalcr = cv.split(image)

    if channel == 'y':
        return canaly
    
    elif channel == 'cb':
        return canalcb
    
    elif channel == 'cr':
        return canalcr

def histogram_img(img):
    return plt.hist(img.ravel(), 256, [0,255])

def histogram_fn(image):
    def myfunc(x):
        return hasattr(x, 'set_color') and not hasattr(x, 'set_facecolor')

    fig = plt.figure(figsize=(3,3), facecolor='#0E1117')
    ax = plt.axes()
    ax.set_facecolor("#0E1117")
    plt.xlabel('Níveis de intensidade dos pixels', fontsize = 5)
    plt.ylabel('Número de pixels', fontsize = 5)

    for o in fig.findobj(myfunc):
        o.set_color('white')

    plt.rcParams['xtick.labelsize'] = 5
    plt.rcParams['ytick.labelsize'] = 5
    plt.grid(False)

    #gray =  cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    plt.hist(image.ravel(), 256, [0,255])
    return st.pyplot(fig, use_container_width=False)