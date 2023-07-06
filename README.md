# kaggle-bootcamp-data-science-y-python
	Jorge Costa Maciá
	https://github.com/JorgeCostaMacia/
	https://bitbucket.org/jorgecostamacia/

## Introducción
    Proyecto de ML en Kaggle

## Enunciado 
    Esta competición medirá las habilidades de los alumnos del Bootcamp de Verne en Data Science y Python. El dataset es un subconjunto de dato público ofrecido por Microsoft sobre dato real y anonimizado para la detección temprana de virus y malware en general
    Los alumnos deben utilizar Python para entrenar sus modelos. Es obligatorio cumplir el formato de envío de las soluciones (ver la sección de Evaluación)
    ¡Ayúdanos a predecir bajo qué circunstancia el malware ataca más habitualmente para poder evitar infecciones de manera precoz y demuestra a tus compañeros y profesores lo que sabes en el camino!

## Enlace
    https://www.kaggle.com/competitions/bootcamp-data-science-y-python


### Dev
    1- notebooks/setup.ipynb
    2- notebooks/dev.ipynb 

### Pre
    1- notebooks/setup.ipynb
    2- notebooks/eda/train.ipynb 
    3- notebooks/eda/test.ipynb 
    4- notebooks/modeling/traing.ipynb 
    5- notebooks/evaluation/train.ipynb 

### Prod
    1- notebooks/setup.ipynb
    2- notebooks/eda/train.ipynb 
    3- notebooks/eda/test.ipynb 
    4- notebooks/modeling/traing.ipynb 
    5- notebooks/evaluation/test.ipynb 


### Estructura

```
+-- columns/
|   +-- cat_mask_3.pkl
|   +-- cat_mask_4.pkl
|   +-- cat_mask_5.pkl
|   +-- cat_mask_6.pkl
|   +-- cat_onehot_encoder.pkl
|   +-- cat_pro.pkl
|   +-- cat_ctarget_encoder.pkl
|   +-- cat.pkl
|   +-- num_correlacion.pkl
|   +-- num_onehot_encoder.pkl
|   +-- num_pro.pkl
|   +-- num_target_encoder.pkl
|   +-- num.pkl
+-- data/
|   +-- final/
|   |   +-- test.csv
|   |   +-- processed/
|   |   +-- test.csv
|   |   +-- train.csv
|   +-- raw/
|   |   +-- dev.csv
|   |   +-- test.csv
|   |   +-- train.csv
+-- encoders/
|   +-- onehot.pkl
|   +-- target.pkl
+-- imputers/
|   +-- cat_simple.pkl
|   +-- num_simple.pkl
+-- interquartiles/
|   +-- intercuartilico.pkl
+-- models/
|   +-- train.pkl
+-- notebooks/
|   +-- eda/
|   |   +-- test.pkl
|   |   +-- train.pkl
|   +-- evalutaion/
|   |   +-- test.pkl
|   |   +-- train.pkl
|   +-- modeling/
|   |   +-- train.pkl
|   +-- dev.pkl
|   +-- setup.pkl
```
