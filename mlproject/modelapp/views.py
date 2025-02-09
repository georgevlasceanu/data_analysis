from django.shortcuts import render
from django.http import HttpResponse
import pickle

# Create your views here.
def model_view(request):

    return render(request, "model.html")

def model_result_view(request):
    with open("grid_model.pkl", "rb") as freader:
        model = pickle.load(freader)
    
    x = request.GET["x"]
    y = request.GET["y"]
    x = int(x)
    y = int(y)

    categorie = model.predict([[x, y]])

    return HttpResponse(f"categoria:{categorie}")