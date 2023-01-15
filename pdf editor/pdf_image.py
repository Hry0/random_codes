from PyPDF2 import PdfReader
from PIL import Image
import img2pdf
import glob
import os

newpath = r'C:\Users\acer\Documents\Py\pdf editor\invert' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

def Inversion(Imagi):

    import PIL.ImageOps    
    image =Image.open(Imagi)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(Imagi)
#Inverting pages one by one
pd="Lakshya1"
reader = PdfReader(pd+".pdf")
i=1
for page in reader.pages:
    for image in page.images:
        n_m=newpath+"\img'{}'.jpg".format(i)
        with open(n_m, "wb") as fp:
            fp.write(image.data)
            i+=1
        Inversion(n_m)
    print("Done",n_m)

#Creating new pdf
print("/tConverting to pdf:")
files=glob.glob(r'C:\Users\acer\Documents\Py\pdf editor\invert\*.jpg')
with open(newpath+"\\"+pd+"-inverted.pdf","wb") as f:
    f.write(img2pdf.convert(files))

print("DELETING UNNECCESARY FILES")
for i in files:
    print("Deleting",i)
    os.remove(i)