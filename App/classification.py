from flask import Flask, jsonify, url_for, render_template, request, redirect, Blueprint
from flask_login import login_required, current_user
from . import db,app
from PIL import Image
import requests
import os


classification = Blueprint('classification', __name__)

@classification.route('/classification', methods=['GET', 'POST'])
@login_required
def classify():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        file.save(file.filename)
        if not file:
            return
        
        # resize image
        image = Image.open(file.filename)
        image = image.resize((500,500),Image.ANTIALIAS)
        image.save(fp="newimage.jpg")

        file = {'file': ("newimage.jpg", open("newimage.jpg", 'rb'))}
        filename = file["file"][0]
        print(filename)

        # request API to make prediction 
        response = requests.post(
            f"http://localhost:8000/upload_file",
            files=file,
        )
        
        os.system(f"cp {filename} ./App/static/{filename}")

        return render_template('results_classification.html',result_image = f"/{filename}", results_table=response.json())

    return render_template('classification.html')
