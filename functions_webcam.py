import cv2
from PIL import Image
import streamlit as st

#Definição as funções utilizadas para realizar o processamento das imagens

def threshold_webcam(image, frame, value):# Função de Limiarização em imagem de vídeo
    img_in = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    ret, image_bin = cv2.threshold(img_out, value, 255, cv2.THRESH_BINARY)
    img_out = Image.fromarray(image_bin)
    return frame.image([img_in, img_out], width=500)

def brighten_webcam(image, frame, value): #Função de brilho em imagem de vídeo
    img_in = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY) 
    img_out = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_bright = cv2.convertScaleAbs(img_out, alpha=1, beta=value)
    img_out = Image.fromarray(img_bright)
    return frame.image([img_in, img_out], width=500)

def contrast_webcam(image, frame, value): #Função de Contraste em imagem estática
    img_in = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY) 
    cv2image = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_contrast = cv2.convertScaleAbs(cv2image, alpha=value/100, beta=0)
    img_out = Image.fromarray(img_contrast)
    return frame.image([img_in, img_out], width=500)

def sobel_webcam(image, frame, value1, value2):
    img_in = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY) 
    cv2image = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_sobelxy = cv2.Sobel(src=cv2image, ddepth=cv2.CV_64F, dx=value1, dy=value2, ksize=5)
    #img_sobelxy = cv2.addWeighted(img_sobelx, 0.5, img_sobely, 0.5, 0)
    img = Image.fromarray(img_sobelxy)
    img_out = img.convert("L")
    return frame.image([img_in, img_out], width=500)

def canny_webcam(image, frame, value1, value2):
    img_in = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY) 
    cv2image = cv2.cvtColor(image.read()[1], cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(cv2image, value1, value2)
    img_out = Image.fromarray(img_canny)
    return frame.image([img_in, img_out], width=500)