from urllib.request import urlretrieve
import os

class getCaptcha:
    URL = 'https://apps2.mef.gob.pe/consulta-vfp-webapp/Captcha.jpg'
    def downloadCaptcha(self,id):
        filename = 'images/'+str(id)+'.jpg'
        try:
            urlretrieve(self.URL,filename)
        except Exception as error:
            print(id,error)
    def download(self,n=1000):#por defecto descargo 1000 imagenes
        if not os.path.exists('images'):
            os.makedirs('images')
        for i in range(n):
            self.downloadCaptcha(i)

captchas = getCaptcha()
captchas.download(2000)

