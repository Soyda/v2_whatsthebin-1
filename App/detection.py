import io
from operator import truediv
import os
import json
from unicodedata import name
from PIL import Image
from . import db,app

import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect, Blueprint
from flask_login import login_required, current_user

detection = Blueprint('detection', __name__)

RESULT_FOLDER = os.path.join('static')
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# finds the model inside your directory automatically - works only if there is one model
def find_model():
    for f  in os.listdir():
        if f.endswith(".pt"):
            return f
    print("please place a model file in this directory!")

    
model_name = find_model()
model =torch.hub.load("WongKinYiu/yolov7", 'custom',model_name)

model.eval()

# set threshold to confidence an IoU
model.conf = 0.1  # confidence threshold (0-1)
model.iou = 0.25  # NMS IoU threshold (0-1)  

def get_prediction(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    imgs = [img]  # batched list of images
# Inference
    results = model(imgs, size=640)  # includes NMS
    return results

@detection.route('/detection', methods=['GET', 'POST'])
@login_required
def detect():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return
        
        img_bytes = file.read()
        results = get_prediction(img_bytes)
        results.save(save_dir='App/static')
        filename = 'image0.jpg'

        table_results = results.pandas().xyxy[0].groupby("name").agg("count")
        table_results["count"] = table_results["class"]

        return render_template('result.html',result_image = filename,model_name = model_name, results_table=table_results["count"].to_frame().to_html())

    return render_template('detection.html')


