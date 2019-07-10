from os import listdir
from os.path import isfile, join
import cv2 as cv

class Binarizador:
    umbralLow = 50
    umbralHigh = 160
    def setFilename(self,filename):
        self.filename = filename
    def setUmbral(self,umbralLow,umbralHigh):
        self.umbralLow = umbralLow
        self.umbralHigh = umbralHigh
    def readImageColor(self):
        return cv.imread('muestra/'+self.filename)
    def escalaGrises(self,fotoColor):
        return cv.cvtColor(fotoColor, cv.COLOR_BGR2GRAY)
    def rotate(self,foto,grados):
        return foto.rotate(grados,expand=True)
    def binaryImage(self,fotoGris):
        nueva_imagen = cv.adaptiveThreshold(fotoGris,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,2)
        return nueva_imagen
    def saveBinaryImage(self,fotoBinaria):
        cv.imwrite('muestraBinaria/'+self.filename,fotoBinaria)
    def closeImage(self,foto):
        cv.destroyAllWindows()
    def binarizar(self):
        foto = self.readImageColor()
        fotoGris = self.escalaGrises(foto)
        fotoBinaria = self.binaryImage(fotoGris)
        self.saveBinaryImage(fotoBinaria)
        self.closeImage(foto)


