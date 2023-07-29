from functions_img import brighten_img, threshold_img, contrast_img, sobel_img, canny_img, histogram_img, histogram_fn, channel_rgb, channel_ycbcr
from functions_webcam import threshold_webcam, brighten_webcam, contrast_webcam, sobel_webcam, canny_webcam, channel_rgb_w, channel_ycbcr_w, gray_scale, img_webcam
import streamlit as st
from PIL import Image
import numpy as np
import cv2 as cv


st.set_page_config(layout="wide") #Deixando a página no modo wide por default

def main_loop():
    st.title("PDI App")
    st.subheader("This app allows you to play with Image filters!")

    histogram = True
    bar = st.sidebar
    entry_option = bar.selectbox('Selecione o formato da entrada:', ['Upload da Imagem', 'Webcam'])
    option = bar.selectbox('Selecione a técnica desejada:', ['Limiarização', 'Brilho', 'Contraste', 'Sobel', 'Canny', 'Visualizar'])
    #scale = bar.radio('Selecione a escala:', ['Escala de Cinza', 'Escala de Cor'])

    bar.markdown(''' ### Opções: ''')
    vis = img2 = img3 = img4 = text_frame3 = text_frame4 = ''

    match entry_option:

        case 'Upload da Imagem':
            image = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg','tif'])

            if not image: 
                return None
        
            else: 
                original_image = Image.open(image)
                original_image = np.array(original_image)
                img = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

            match option:

                case 'Limiarização':
                    threshold_value = bar.slider("Limiarização", min_value=-1, max_value=255, value=-1)
                    text_frame2 = 'Imagem binarizada'
                    img2 = threshold_img(img, threshold_value)

                case 'Brilho':
                    brightness_value = bar.slider("Brilho", min_value=-1, max_value=255, value=0)
                    text_frame2 = 'Imagem de saída'
                    text_frame3 = 'Histograma da imagem de entrada'
                    text_frame4 = 'Histograma da imagem de saída'
                    img2 = brighten_img(img, brightness_value)

                case 'Contraste':
                    contrast_value = bar.slider("Contraste", min_value=0.0, max_value=2.0, value=0.0)
                    text_frame2 = 'Imagem de saída'
                    text_frame3 = 'Histograma da imagem de entrada'
                    text_frame4 = 'Histograma da imagem de saída'
                    img2 = contrast_img(img, contrast_value)

                case 'Sobel':
                    sobel_value_1 = bar.slider("Sobel X", min_value=1, max_value=4, value=1)
                    sobel_value_2 = bar.slider("Sobel Y", min_value=1, max_value=4, value=1)
                    text_frame2 = 'Imagem de saída'
                    img2 = sobel_img(img, sobel_value_1, sobel_value_2)   

                case 'Canny':
                    canny_value_1 = bar.slider("Limiar mínimo", min_value=0, max_value=255, value=0)
                    canny_value_2 = bar.slider("Limiar máximo", min_value=0, max_value=255, value=0)
                    text_frame2 = 'Imagem de saída'
                    img2 = canny_img(img, canny_value_1, canny_value_2)

                case 'Visualizar':

                    vis = bar.selectbox('Selecione o formato da conversão:', ['Escala de Cinza','RGB', 'YCBCR'])
                    img = original_image

                    match vis:

                        case 'Escala de Cinza':
                            text_frame2 = 'Imagem em escala de cinza' 
                            img2 = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

                        case 'RGB':
                            text_frame2 = "Componente Vermelha (R)"
                            img2 = channel_rgb(original_image, 'r')
                            text_frame3 = "Componente Verde (G)"
                            img3 = channel_rgb(original_image, 'g')
                            text_frame4 = "Componente Verde (B)"
                            img4 = channel_rgb(original_image, 'b')

                        case 'YCBCR':
                            text_frame2 = "Componente Y"
                            img2 = channel_ycbcr(original_image, 'y')
                            text_frame3 = "Componente Cb"
                            img3 = channel_ycbcr(original_image, 'cb')
                            text_frame4 = "Componente Cr"
                            img4 = channel_ycbcr(original_image, 'cr')

            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            with col1: # Coluna da img de entrada
                st.text("Imagem de entrada")
                st.image([img], width=550)

            with col2: # Coluna da img de entrada
                st.text(f'{text_frame2}')
                st.image([img2], width=550)

            with col3: # Coluna da img de entrada
                st.text(f'{text_frame3}')

                match option:

                    case 'Brilho' | 'Contraste':
                        histogram_fn(img)

                match vis:
                    
                    case 'RGB' | 'YCBCR':
                        st.image([img3], width=550)
                    

            with col4: # Coluna da img de entrada
                
                st.text(f'{text_frame4}')

                match option:

                    case 'Brilho' | 'Contraste':
                        histogram_fn(img2)

                match vis:
                    
                    case 'RGB' | 'YCBCR':
                        st.image([img4], width=550)

        case 'Webcam':

            image = vis = None
            camera = cv.VideoCapture(0)

            text_frame2 = text_frame3 = text_frame4 = ''

            #Estrutura da imagem dinâmica
            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            with col1:
                st.text("Imagem de entrada")
                frame = st.image([])
            with col2:
                text_frame2 = st.text("")
                frame2 = st.image([])
            with col3:
                text_frame3 = st.text("")
                frame3 = st.image([])
            with col4:
                text_frame4 = st.text("")
                frame4 = st.image([])

            match option:

                case 'Limiarização':
                    histogram = False
                    threshold_value = bar.slider("Limiarização", min_value=-1, max_value=255, value=-1)
                    while 'True' == 'True':
                        img_webcam(camera, frame, 'gray')
                        text_frame2.text("Imagem binarizada")
                        threshold_webcam(camera, frame2, threshold_value)

                case 'Brilho':
                    histogram = False
                    brightness_value = bar.slider("Brilho", min_value=0, max_value=255, value=0)
                    
                    while 'True' == 'True':
                        img_webcam(camera, frame, 'gray')
                        text_frame2.text("Imagem Saída")
                        brighten_webcam(camera, frame2, brightness_value)

                case 'Contraste':
                    histogram = False
                    contrast_value = bar.slider("Contraste", min_value=0, max_value=200, value=0)

                    while 'True' == 'True':
                        img_webcam(camera, frame, 'gray')
                        text_frame2.text("Imagem Saída")
                        contrast_webcam(camera, frame2, contrast_value)

                case 'Sobel':
                    histogram = False
                    sobel_value_1 = bar.slider("Sobel X", min_value=1, max_value=4, value=1)
                    sobel_value_2 = bar.slider("Sobel Y", min_value=1, max_value=4, value=1)
                    
                    while 'True' == 'True':
                        img_webcam(camera, frame, 'gray')
                        text_frame2.text("Imagem Saída")
                        sobel_webcam(camera, frame2, sobel_value_1, sobel_value_2)

                case 'Canny':
                    histogram = False
                    canny_value_1 = bar.slider("Limiar mínimo", min_value=0, max_value=255, value=0)
                    canny_value_2 = bar.slider("Limiar máximo", min_value=0, max_value=255, value=0)
                    
                    while 'True' == 'True':
                        img_webcam(camera, frame, 'gray')
                        text_frame2.text("Imagem Saída")
                        canny_webcam(camera, frame2, canny_value_1, canny_value_2)

                case 'Visualizar':
                    histogram = processed_image = None
                    vis = bar.selectbox('Selecione o formato de visualização:', ['Escala de Cinza','RGB', 'YCBCR'])

                    match vis:

                        case 'Escala de Cinza':
                            while 'True' == 'True':
                                img_webcam(camera, frame, 'color')
                                text_frame2.text("Imagem em escala de cinza")
                                gray_scale(camera, frame2)

                        case 'RGB':
                            while 'True' == 'True':
                                img_webcam(camera, frame, 'color')
                                text_frame2.text("Componente Vermelha (R)")
                                channel_rgb_w(camera, frame2, 'r')
                                text_frame3.text("Componente Verde (G)")
                                channel_rgb_w(camera, frame3, 'g')
                                text_frame4.text("Componente Verde (B)")
                                channel_rgb_w(camera, frame4, 'b')

                        case 'YCBCR':
                            while 'True' == 'True':
                                img_webcam(camera, frame, 'color')
                                text_frame2.text("Componente Y")
                                channel_ycbcr_w(camera, frame2, 'y')
                                text_frame3.text("Componente Cb")
                                channel_ycbcr_w(camera, frame3, 'cb')
                                text_frame4.text("Componente Cr")
                                channel_ycbcr_w(camera, frame4, 'cr')

if __name__ == '__main__':
    main_loop()