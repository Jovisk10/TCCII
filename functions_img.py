from PIL import Image
import streamlit as st
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Definição as funções utilizadas para realizar o processamento das imagens

def brighten_img(image, value): #Função de brilho em imagem estática
    img_bright = cv.convertScaleAbs(image, beta=value)
    return img_bright

def threshold_img(image, value):# Função de Limiarização em imagem estática
    cv2image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, img_out = cv.threshold(cv2image, value, 255, cv.THRESH_BINARY)
    img = Image.fromarray(img_out)
    return img

def contrast_img(image, value): #Função de Contraste em imagem estática
    cv2image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    img_contrast = cv.convertScaleAbs(cv2image, alpha=value/100, beta=0)
    img = Image.fromarray(img_contrast)
    return img

def sobel_img(image, value1, value2):
    cv2image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img_sobelxy = cv.Sobel(src=cv2image, ddepth=cv.CV_64F, dx=value1, dy=value2, ksize=5)
    #img_sobelxy = cv2.addWeighted(img_sobelx, 0.5, img_sobely, 0.5, 0)
    img = Image.fromarray(img_sobelxy)
    img = img.convert("L")
    return img

def canny_img(image, value1, value2):
    cv2image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img_canny = cv.Canny(cv2image, value1, value2)
    img = Image.fromarray(img_canny)
    return img

def histogram_img(img):
    return plt.hist(img.ravel(), 256, [0,255])

def histogram_fn(image):
    def myfunc(x):
        return hasattr(x, 'set_color') and not hasattr(x, 'set_facecolor')

    fig = plt.figure(figsize=(5,5), facecolor='#0E1117')
    ax = plt.axes()
    ax.set_facecolor("#0E1117")
    plt.xlabel('Níveis de intensidade dos pixels')
    plt.ylabel('Número de pixels')

    for o in fig.findobj(myfunc):
        o.set_color('white')

    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.grid(False)

    gray =  cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    plt.hist(gray.ravel(), 256, [0,255])
    return st.pyplot(fig)