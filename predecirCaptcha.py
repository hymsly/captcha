import cv2 as cv
from os import listdir
from os.path import isfile, join
import numpy as np

folderIN = 'muestra'
folderParticiones = 'muestraBinariaParticionada'
folderPlantillas = 'DICCIONARIO-BINARIO-NORMALIZADO'

images = [f for f in listdir(folderIN) if isfile(join(folderIN, f))]
plantillas = [f for f in listdir(folderPlantillas) if isfile(join(folderPlantillas, f))]


class Predictor:
    numParticiones = 5
    imgParticionesData = []
    caracteresObservados = []
    filenameImage = ""

    caracteres = []
    caracteresData = []

    aciertoMas3 = 0
    aciertoTodo = 0

    statByCaracter = {}
    def __init__(self):
        self.caracteres = []
        self.caracteresData = []
        self.aciertoMas3 = 0
        self.aciertoTodo = 0
        self.aciertosByCaracter = {}
        self.erroresByCaracter = {}
        plantillas = [f for f in listdir(folderPlantillas) if isfile(join(folderPlantillas, f))]
        for plantilla in plantillas:
            caracter = plantilla.split('.')[0]
            self.caracteres.append(caracter)
            im = cv.imread(folderPlantillas + '/' + plantilla,0).astype('float64')
            self.caracteresData.append(im)

    def setParticiones(self):
        self.imgParticionesData = []
        self.caracteresObservados = []
        for i in range(self.numParticiones):
            filenameParticion = folderParticiones + '/' + str(i) + '_'+self.filenameImage
            im = cv.imread(filenameParticion,0).astype('float64')
            self.imgParticionesData.append(im)
            caracterObservada = self.filenameImage[i]
            self.caracteresObservados.append(caracterObservada)

    def setImage(self,filename):
        self.filenameImage = filename
        self.setParticiones()
    
    def predecir(self,cntElements):
        cntCaracteres = len(self.caracteres)
        predicted = True
        cntCaracteresCorrectas = 0
        for i in range(self.numParticiones):
            res = {}
            currentCaracterObservado = self.caracteresObservados[i]
            for j in range(cntCaracteres):
                currentCaracterAnalizado = self.caracteres[j]
                weightDm = cv.filter2D(self.imgParticionesData[i], -1, self.caracteresData[j])
                res[currentCaracterAnalizado] = np.amax(weightDm)
            res = sorted(((value, key) for (key,value) in res.items()),reverse=True)
            prediccion = []
            for i in range(cntElements):
                prediccion.append(res[i][1])
            if(currentCaracterObservado in prediccion):
                if(currentCaracterObservado in self.aciertosByCaracter.keys()):
                    self.aciertosByCaracter[currentCaracterObservado] += 1
                else:
                    self.aciertosByCaracter[currentCaracterObservado] = 1
                cntCaracteresCorrectas+=1
            else:
                predicted = False
                if(currentCaracterObservado in self.erroresByCaracter.keys()):
                    self.erroresByCaracter[currentCaracterObservado] += 1
                else:
                    self.erroresByCaracter[currentCaracterObservado] = 1
        if(cntCaracteresCorrectas>=3):
            self.aciertoMas3+=1
        if(predicted):
            self.aciertoTodo+=1
        return cntCaracteresCorrectas>=3,predicted

    def getResults(self):
        return self.aciertoMas3,self.aciertoTodo,self.aciertosByCaracter,self.erroresByCaracter
