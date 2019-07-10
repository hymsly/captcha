from PIL import Image
from os import listdir
from os.path import isfile, join


folderIN = "DICCIONARIO-BINARIO"
folderOUT = "DICCIONARIO-BINARIO-NORMALIZADO"

class Resizer:
    size = 30,60
    def resize(self,filename):
        im = Image.open(folderIN + '/' + filename)
        im = im.resize(self.size,Image.ANTIALIAS)
        im.save(folderOUT + '/' + filename)


resizer = Resizer()

images = [f for f in listdir(folderIN) if isfile(join(folderIN, f))]

for image in images:
    resizer.resize(image)
