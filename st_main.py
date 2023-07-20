import streamlit as st
import numpy as np
from PIL import Image
import cv2
import cv2 as cv
from functions_img import brighten_img, threshold_img, contrast_img, sobel_img, canny_img, histogram_img, histogram_fn
from functions_webcam import threshold_webcam, brighten_webcam, contrast_webcam, sobel_webcam, canny_webcam
from matplotlib import pyplot as plt


st.set_page_config(layout="wide") #Deixando a página no modo wide por default

def main_loop():
    st.title("PDI App")
    st.subheader("This app allows you to play with Image filters!")

    histogram = True
    bar = st.sidebar
    entry_option = bar.selectbox('Selecione o formato da entrada:', ['Upload da Imagem', 'Webcam'])
    option = bar.selectbox('Selecione a técnica desejada:', ['Limiarização', 'Brilho', 'Contraste', 'Sobel', 'Canny'])

    match entry_option:

        case 'Upload da Imagem':
            image = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])

            if not image: 
                return None
        
            else: 
                original_image = Image.open(image)
                original_image = np.array(original_image)

            match option:

                case 'Limiarização':
                    histogram = False
                    threshold_value = bar.slider("Limiarização", min_value=-1, max_value=255, value=-1)
                    processed_image = threshold_img(original_image, threshold_value)

                case 'Brilho':
                    histogram = True
                    brightness_value = bar.slider("Brilho", min_value=-1, max_value=255, value=0)
                    processed_image = brighten_img(original_image, brightness_value)

                case 'Contraste':
                    histogram = True
                    contrast_value = bar.slider("Contraste", min_value=-1, max_value=100, value=0)
                    processed_image = contrast_img(original_image, contrast_value)   

                case 'Sobel':
                    histogram = False
                    sobel_value_1 = bar.slider("Sobel X", min_value=1, max_value=4, value=1)
                    sobel_value_2 = bar.slider("Sobel Y", min_value=1, max_value=4, value=1)
                    processed_image = sobel_img(original_image, sobel_value_1, sobel_value_2)   

                case 'Canny':
                    histogram = False
                    canny_value_1 = bar.slider("Canny dsad", min_value=0, max_value=255, value=0)
                    canny_value_2 = bar.slider("Canny asdas", min_value=0, max_value=255, value=0)
                    processed_image = canny_img(original_image, canny_value_1, canny_value_2)

        case 'Webcam':
            image = ''
            st.text('Imagem de entrada                                                Imagem de saída')
            FRAME_WINDOW  = st.image([])
            camera = cv2.VideoCapture(0)
            col1, col2 = st.columns(2)
            
            match option:

                case 'Limiarização':
                    histogram = False
                    threshold_value = bar.slider("Limiarização", min_value=-1, max_value=255, value=-1)

                    while 'True' == 'True':
                        threshold_webcam(camera, FRAME_WINDOW, threshold_value)

                case 'Brilho':
                    histogram = False
                    brightness_value = bar.slider("Brilho", min_value=0, max_value=255, value=0)
                    
                    while 'True' == 'True':
                        brighten_webcam(camera, FRAME_WINDOW, brightness_value)

                case 'Contraste':
                    histogram = False
                    contrast_value = bar.slider("Contraste", min_value=0, max_value=100, value=0)

                    while 'True' == 'True':
                        contrast_webcam(camera, FRAME_WINDOW, contrast_value)

                case 'Sobel':
                    histogram = False
                    sobel_value_1 = bar.slider("Sobel X", min_value=1, max_value=4, value=1)
                    sobel_value_2 = bar.slider("Sobel Y", min_value=1, max_value=4, value=1)
                    
                    while 'True' == 'True':
                        sobel_webcam(camera, FRAME_WINDOW, sobel_value_1, sobel_value_2)

                case 'Canny':
                    histogram = False
                    canny_value_1 = bar.slider("Canny dsad", min_value=0, max_value=255, value=0)
                    canny_value_2 = bar.slider("Canny asdas", min_value=0, max_value=255, value=0)
                    
                    while 'True' == 'True':
                        canny_webcam(camera, FRAME_WINDOW, canny_value_1, canny_value_2)
    
    #Estrutura da Ferramenta

    # Campo de imagens de entrada e Saída
    col_1, col_2 = st.columns(2)

    match entry_option:

        case 'Upload da Imagem':

            with col_1: # Coluna da img de entrada
                st.text("Imagem de entrada")
                st.image([original_image], width=500)

            with col_2: #Coluna da img de saída
                st.text("Imagem de saída")
                st.image([processed_image], width=500)

    #Campo para Histogramas de entrada e Saída
    st.text("")
    histcol1, histcol2 = st.columns(2)
    fig = plt.figure(figsize=(8,8))

    match option:

        case 'Brilho' | 'Contraste':

            with histcol1: #Coluna hist de entrada
                st.text("Histograma imagem de entrada")
                if histogram == True:
                    histogram_fn(original_image)

            with histcol2: #Coluna hist de saída
                st.text("Histograma imagem de saída")
                if histogram == True:
                    histogram_fn(processed_image)

if __name__ == '__main__':
    main_loop()