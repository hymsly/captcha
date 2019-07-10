import cv2 as cv
from os import listdir
from os.path import isfile, join


folderIN = 'muestraBinaria'
folderOut = 'muestraBinariaParticionada'

images = [f for f in listdir(folderIN) if isfile(join(folderIN, f))]

class Cropper:
    px = 10
    step = 30
    numCrops = 5
    def Crop(self,filename):
        im = cv.imread(folderIN + '/' + filename,0)
        ims = []
        pxCurrent = self.px
        for _ in range(self.numCrops):
            crop_img = im[0:60, pxCurrent:pxCurrent+self.step]
            pxCurrent += self.step
            ims.append(crop_img)
        for i in range(self.numCrops):
            cv.imwrite(folderOut+'/'+str(i)+'_'+filename,ims[i])

