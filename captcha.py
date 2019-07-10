from binarizacion import Binarizador
from particionarCaptcha import Cropper
from predecirCaptcha import Predictor
from os.path import isfile, join
from os import listdir

##LEYENDO CAPTCHAS
images = [f for f in listdir('muestra') if isfile(join('muestra', f))]
##INSTANCIANDO OBJETO BINARIZADOR
binarizer = Binarizador()
##INSTANCIANDO OBJETO PARTICIONADOR
cropper = Cropper()
##INSTANCIA MODELO DE RECONOCIMIENTO DEL CAPTCHA
predictor = Predictor()

##BINARIZANDO LOS CAPTCHAS
for image in images:
    #BINARIZANDO
    binarizer.setFilename(image)
    binarizer.binarizar()
    #PARTICIONANDO
    cropper.Crop(image)
    ##CLASIFICANDO
    predictor.setImage(image)
    predictor.predecir(5)##AGARRA LAS 5 PRIMEROS CLASES

##MOSTRANDO RESULTADOS
exitoMinimo3,exitoTodo,acierto,errores = predictor.getResults()
print(len(images),exitoMinimo3,exitoTodo)
print(acierto)
print(errores)
