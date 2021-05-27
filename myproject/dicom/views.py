from django.shortcuts import render

# Create your views here.
import base64
import os
import time
import traceback
from io import BytesIO

import imageio
import matplotlib.pyplot as plt
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import redirect, render
from termcolor import colored

from myproject.myproject import settings


# our page
def app_render(request):
    print(settings.BASE_DIR)
    d = {'title': 'DICOM viewer', 'info': 'DICOM SERVER SIDE RENDER'}
    return render(request, "main_template.html", d)


# just to redirect to the web app
def send_to_dcom(request):
    return redirect('medical/app')