from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImagePredictForm
import pickle
import numpy as np  
import pandas as pd
from PIL import Image
# Create your views here.

def make_prediction(image):
    with open("model_digits.pkl", "rb") as freader:
        model = pickle.load(freader)

    pillow_image = Image.open(image)
    grey_image = pillow_image.convert("L")
    np_image = np.array(grey_image)
    image_convert = np.concatenate(np_image)


    return model.predict([image_convert])

def digits_view(request):
    if request.method == "POST":
        # Create form instance with POST data and FILES
        form = ImagePredictForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Get the uploaded image file
            uploaded_image = request.FILES["image"]
            print(f"Uploaded image: {uploaded_image}")

            # Make a prediction
            result = make_prediction(uploaded_image)

            return HttpResponse(f"Raspunsul este {result}")

    
    form = ImagePredictForm()
    context = {"form": form}
    return render(request, "digits.html", context)