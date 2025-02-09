from django.urls import path
from .views import *

urlpatterns = [
    path("", model_view),
    path("result", model_result_view, name="result_url"),
]
