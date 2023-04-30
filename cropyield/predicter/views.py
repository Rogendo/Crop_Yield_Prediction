from django.shortcuts import render
import pickle

# Create your views here.
# loading the pre-trained model
pickle_in = open('predicter/Crop_Yield_Prediction/RandomForest.pkl', 'rb')
model = pickle.load(pickle_in)


def index(request):
    return render(request, 'predicter/index.html')


def predicter(request):
    return render(request, 'predicter/main.html')

def Forminfo(request):
    nitrogen= request.GET['nitrogen']
    phosphorus=request.GET['phosphorus']
    potassium=request.GET['potassium']
    teperature=request.GET['temperature']
    humidity=request.GET['humidity']
    ph=request.GET['ph']
    rainfall=request.GET['rainfall']
    y_pred=model.predict([[nitrogen,phosphorus,potassium,teperature,humidity,ph,rainfall]])
    if y_pred == 0:
        y_pred = "apple"
    elif y_pred==1:
        y_pred='banana'
    elif y_pred == 2:
        y_pred = "blackgram"
    elif y_pred == 3:
        y_pred = "chickpea"
    elif y_pred == 4:
        y_pred = "coconut"
    elif y_pred == 5:
        y_pred = "coffee"
    elif y_pred == 6:
        y_pred = "cotton"

    elif y_pred == 7:
        y_pred = "grapes"
    elif y_pred == 8:
        y_pred = "jute"
    elif y_pred == 9:
        y_pred = "kidneybeans"
    elif y_pred == 10:
        y_pred = "lentil"
    elif y_pred == 11:
        y_pred = "maize"
    elif y_pred == 12:
        y_pred = "mango"
    elif y_pred == 13:
        y_pred = "mothbeans"
    elif y_pred == 14:
        y_pred = "mungbean"
    elif y_pred == 15:
        y_pred = "muskmelon"
    elif y_pred == 16:
        y_pred = "orange"
    elif y_pred == 17:
        y_pred = "papaya"
    elif y_pred == 18:
        y_pred = "pigeonpeas"
    elif y_pred == 19:
        y_pred = "pomegranate"
    elif y_pred == 20:
        y_pred = "rice"
    elif y_pred == 21:
        y_pred = "watermelon"
    else:
        y_pred='failed to predict'
    
    print(y_pred)

    return render(request, 'predicter/result.html',{'result':y_pred})