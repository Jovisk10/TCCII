from matplotlib import pyplot as plt
import streamlit as st
from PIL import Image
import numpy as np
import cv2
#Definição as funções utilizadas para realizar o processamento das imagens

def img_webcam(image, frame, scale):
    if scale == 'gray':
        img_in = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    else:
        img_in = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2RGB)
    return frame.image(img_in, width=550)

def gray_scale(image, frame):
    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    return frame.image(img_out, width=550)

def threshold_webcam(image, frame, value):# Função de Limiarização em imagem de vídeo

    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    ret, image_bin = cv2.threshold(img_out, value, 255, cv2.THRESH_BINARY)
    img_out = Image.fromarray(image_bin)
    return frame.image(img_out, width=550)

def brighten_webcam(image, frame, value): #Função de brilho em imagem de vídeo

    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_bright = cv2.convertScaleAbs(img_out, alpha=1, beta=value)
    img_out = Image.fromarray(img_bright)

    return frame.image(img_out, width=550)

def contrast_webcam(image, frame, value): #Função de Contraste em imagem estática

    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_contrast = cv2.convertScaleAbs(img_out, alpha=value/100, beta=0)
    img_out = Image.fromarray(img_contrast)
    return frame.image(img_out, width=550)

def sobel_webcam(image, frame, value1, value2, component):
    
    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)

    if component == 'xy':
        img_sobelxy = cv2.Sobel(src=img_out, ddepth=cv2.CV_64F, dx=value1, dy=value2, ksize=3)

    elif component == 'x':
        img_sobelxy = cv2.Sobel(src=img_out, ddepth=cv2.CV_64F, dx=value1, dy=0, ksize=3)

    elif component == 'y':
        img_sobelxy = cv2.Sobel(src=img_out, ddepth=cv2.CV_64F, dx=0, dy=value2, ksize=3)

    img = Image.fromarray(img_sobelxy)
    img_out = img.convert("L")
    return frame.image(img_out, width=550)

def canny_webcam(image, frame, value1, value2):

    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(img_out, value1, value2)
    img_out = Image.fromarray(img_canny)
    return frame.image(img_out, width=550)

def channel_rgb_w(image, frame, channel):
    img = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2RGB)
    canalVermelho, canalVerde, canalAzul = cv2.split(img)

    if channel == 'b':
        return frame.image(canalAzul, width=550)
    elif channel == 'g':
        return frame.image(canalVerde, width=550)
    if channel == 'r':
        return frame.image(canalVermelho, width=550)

def channel_ycbcr_w(image, frame, channel):
    img = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2YCrCb)
    canaly, canalcr, canalcb = cv2.split(img)

    if channel == 'y':
        return frame.image(canaly, width=550)
    elif channel == 'cb':
        return frame.image(canalcb, width=550)
    if channel == 'cr':
        return frame.image(canalcr, width=550)
    
def histogram_fn_w(image):
    def myfunc(x):
        return hasattr(x, 'set_color') and not hasattr(x, 'set_facecolor')

    fig = plt.figure(figsize=(3,3), facecolor='#0E1117')
    ax = plt.axes()
    ax.set_facecolor("#0E1117")
    plt.xlabel('Níveis de intensidade dos pixels')
    plt.ylabel('Número de pixels')

    for o in fig.findobj(myfunc):
        o.set_color('white')

    plt.rcParams['xtick.labelsize'] = 5
    plt.rcParams['ytick.labelsize'] = 5
    plt.grid(False)

    plt.hist(image.ravel(), 256, [0,255])
    return st.pyplot(fig, use_container_width=False)