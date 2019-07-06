from PIL import Image
from os import listdir
from os.path import isfile, join

class Binarizador:
    umbralLow = 40
    umbralHigh = 160
    def setFilename(self,filename):
        self.filename = filename
    def setUmbral(self,umbralLow,umbralHigh):
        self.umbralLow = umbralLow
        self.umbralHigh = umbralHigh
    def readImageColor(self):
        return Image.open('muestra/'+self.filename)
    def escalaGrises(self,fotoColor):
        return fotoColor.convert('L')
    def rotate(self,foto,grados):
        return foto.rotate(grados,expand=True)
    def binaryImage(self,fotoGris):
        datos = fotoGris.getdata()
        datos_binarios=[]
        total = len(datos)
        cnt = 0
        for x in datos:
        #    #print(x)
            cnt = cnt +1
            curUmbral = self.umbralLow + (cnt*(self.umbralHigh-self.umbralLow))//total
            if x<curUmbral:
                datos_binarios.append(1)
                continue
            datos_binarios.append(0)
        nueva_imagen=Image.new('1',fotoGris.size)
        nueva_imagen.putdata(datos_binarios)
        return nueva_imagen
    def saveBinaryImage(self,fotoBinaria):
        fotoBinaria.save('muestraBinaria/'+self.filename)
    def closeImage(self,foto):
        foto.close()
    def binarizar(self):
        foto = self.readImageColor()
        fotoGris = self.escalaGrises(foto)
        fotoGris = self.rotate(fotoGris,270)
        fotoBinaria = self.binaryImage(fotoGris)
        fotoBinaria = self.rotate(fotoBinaria,90)
        self.saveBinaryImage(fotoBinaria)
        self.closeImage(foto)


images = [f for f in listdir('muestra') if isfile(join('muestra', f))]

binarizer = Binarizador()

for image in images:
    print(image)
    binarizer.setFilename(image)
    binarizer.binarizar()
