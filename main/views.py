from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import plants
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import image, load_img
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
import numpy as np

appleModel = load_model('./models/mdl_wt (2).hdf5')
grapeModel = load_model('./models/grapemdl_wt.hdf5')
maizeModel = load_model('./models/maizemdl_wt.hdf5')
tomatoModel = load_model('./models/tomatomdl_wt.hdf5')
img_height, img_width = 224,224


def news(request):
    return render(request,'main/news.html')
def calendar(request):
     return render(request, 'main/calendar.html')

def calendarMonsoon(request):
     return render(request, 'main/calendarMonsoon.html')

def calendarSpring(request):
     return render(request, 'main/calendarSpring.html')

def calendarWinter(request):
     return render(request, 'main/calendarWinter.html')

def calendarAutumn(request):
     return render(request, 'main/calendarAutumn.html')     

def ourTeam(request):
     return render(request, 'main/ourTeam.html')     


def main(request):
    plantObj = plants.objects.all()
    context = {'plantObj' : plantObj}
    return render(request, 'main/index.html', context)

def upload(request, pk):
    if request.method == 'POST':        
        fs = FileSystemStorage()
        fileObj = request.FILES['imagePath']
        if fileObj == None:
            return HttpResponse("no any file found")
        else:
            filePathName = fs.save(fileObj.name,fileObj) 
            testimage = '.' +'/static/images/' + filePathName
            filePathName = fs.url(filePathName)
            img = load_img(testimage, target_size=(224,224))
            img_tensor = image.img_to_array(img)
            img_tensor1 = np.expand_dims(img_tensor, axis=0)
            img_tensor2 = preprocess_input(img_tensor1)
            plantname = str(plants.objects.get(id = pk)).lower()
            disease = ''
            if plantname == 'apple':
                disease = preAppleDisase(img_tensor2)
            elif plantname == 'maize':
                disease = preMaizeDisease(img_tensor2)
            elif plantname == 'grape':
                disease = preGrapeDisease(img_tensor2)
            elif plantname == 'tomato':
                disease = preTomatoDisease(img_tensor2)
            context = {
                'plantname' : plantname,
                'disease': disease,
                'filePathName' : filePathName,
            }
            return render(request,'main/result.html', context)
            
        
    else:
        plantname = str(plants.objects.get(id = pk)).lower()
        context = {'plantname':plantname}
        return render(request,'main/upload.html',context)

def preAppleDisase(imgTensor):
    class_list = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy'
    ]
    preds = appleModel.predict(imgTensor)
    disease = class_list[np.argmax(preds[0])]
    return disease

def preGrapeDisease(imgTensor):
    class_list = [
        'Grape___healthy',
        'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
        'Grape___Black_rot',
        'Grape___Esca_(Black_Measles)'
        ]
    preds = grapeModel.predict(imgTensor)
    disease = class_list[np.argmax(preds[0])]
    return disease

def preTomatoDisease(imgTensor):
    class_list = [
        'Tomato___Late_blight',
        'Tomato___healthy',
        'Tomato___Early_blight',
        'Tomato___Septoria_leaf_spot',
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
        'Tomato___Bacterial_spot',
        'Tomato___Target_Spot',
        'Tomato___Tomato_mosaic_virus',
        'Tomato___Leaf_Mold',
        'Tomato___Spider_mites Two-spotted_spider_mite'
        ]
    preds = tomatoModel.predict(imgTensor)
    disease = class_list[np.argmax(preds[0])]
    return disease
   
def preMaizeDisease(imgTensor):
    class_list = [
        'Corn_(maize)___Northern_Leaf_Blight',
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
        'Corn_(maize)___Common_rust_',
        'Corn_(maize)___healthy'
        ]
    preds = maizeModel.predict(imgTensor)
    disease = class_list[np.argmax(preds[0])]
    return disease
        
        
      

    
    
"""
def predictImage(request):
    fs = FileSystemStorage()
    fileObj = request.FILES['imagePath']
    filePathName = fs.save(fileObj.name,fileObj) 

    testimage = '.' +'/media/' + filePathName
    filePathName = fs.url(filePathName)
    img = load_img(testimage, target_size=(224,224))
    img_tensor = image.img_to_array(img)
    img_tensor1 = np.expand_dims(img_tensor, axis=0)
    img_tensor2 = preprocess_input(img_tensor1)
    preds = model.predict(img_tensor2)
    print(preds)
    disease = class_list[np.argmax(preds[0])]
    
    context = {'filePathName' : filePathName, 'Disease' : disease }
    return render(request, 'index.html',context)
"""





