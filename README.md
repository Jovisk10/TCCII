# PDI App

## 1. Descrição do projeto

O PDI APP é uma ferramenta que visa exemplificar diversas formatos e técnicas aplicadas a imagens que são estudadas na disciplina de Processamento digital de imagens, assim pretendendo facilitar o entendimento de como processamento de imagens ocorre de forma prática.

## 2. Funcionalidades do projeto

O PDI App contem as seguindes funcionalidades:

#### Aquisição de imagens

- Estáticas (realizando o upload da imagem desejada)
- Dinâmicas (realizando a leitura de video da webcam)

#### Visualização nos fomatos:

- Escala de cinza
- RGB
- YCbCr

#### Técnicas estudadas:

- Limiarização
- Brilho e Contraste (Com visualização do histograma para imagens estáticas)
- Detecção de bordas pelos operadores de Canny e Sobel

## 3. Tecnologias utilizadas

Para o desenvolvimento dessa ferramenta foram utilziadas as seguintes tecnologias:

#### Interface Web 

- Streamlit

#### Processamento das imagens

- OpenCV
- Pillow

#### Visualização do histograma

- Matplotlib
- Numpy

## 4. Inicialização

A ferramenta pode ser inicializada de 3 formas diferentes:

### Clonando o projeto no github  (Deve-se ter o git instalado)

Via cmd windowns

```git clone https://github.com/Jovisk10/TCCII.git ``` 

Dentro da pasta pdi_tool

```pip install -r requirements.txt```  


```streamlit run pdi_app.py``` 

### Acesse através do link 

 -- Deixar o link disponivel aqui --

### Instale a través do aquivo .bat 

-- Tentar gerar esse arquivo .bat

## 5. Colaboradores

Ferramenta desenvolvida por João Vitor da Silva Campos como trabalho de conclusão de curso de Engenharia Elétrica sob orientação do professor Jozias Parente na Universidade do Estado do Amazonas

## 7. Status do projeto

Projeto em andamento.