from flask import Flask, jsonify, url_for, render_template, request, redirect, Blueprint
from flask_login import login_required, current_user
from . import db,app
from PIL import Image
import requests
import os


classification = Blueprint('classification', __name__)

def plastic_advice():
    return "Les pots de yaourt ne sont, pour l'instant, pas recyclables dans toutes les communes francaises, de même pour les sacs plastiques."

def organic_advice():
    return "Les déchets issus des végétaux sont compostables. Veuillez les mettre dans un composteur, un lombricomposteur ou un bokashi par exemple."
     
def cardboard_advice():
    return "A déchirer et à mettre dans les bacs de recyclage dédiés ou en entier en décheterie ( Attention, le carton souillé ne se recycle pas ! )"
    
def paper_advice():
    return "Poubelle à papier"
    
def glass_advice():
    return "Pensez à enlever le bouchon des bouteilles en verre"
     
def battery_advice():
    return "Attention, les batteries sont à déposer en décheterie ou dans les bacs dédiés en magasin"
     
def clothes_advice():
    return "Si en bon état, à vendre, à donner ou à déposer dans les bennes de collectes : <a href = https://refashion.fr/citoyen/fr/point-dapport>Points de collectes</a>"
    
def metal_advice():
    return "S'il s'agit de conserves veuillez les mettres dans la poubelle des recyclables, s'il s'agit d'un gros objet la déchèterie sera plus adaptée."
 

def pred_message(response):

    classes_to_fr = {'clothes':'Vêtement', 
                 'battery':'Pile ou batterie', 
                 'biological':'Déchet organique', 
                 'cardboard':'Carton', 
                 'glass':'Verre', 
                 'metal':'Métal', 
                 'paper':'Papier', 
                 'plastic':'Plastique', 
                 'trash':'Déchet non recyclable'}

    recyclable_lille = ["plastic","glass","metal","paper","cardboard"]

    pred = "Prédiction: "+classes_to_fr[response.json()["label"]]
    conf = "Confiance: "+response.json()["confidence"]+" %"

    if response.json()["label"] in recyclable_lille:
                
        if response.json()["label"] == 'plastic':
            advice = plastic_advice()

        elif response.json()["label"] == 'cardboard':
            advice = cardboard_advice()
        
        elif response.json()["label"] == 'paper':
            advice = paper_advice()

        elif response.json()["label"] == 'metal':
            advice = metal_advice()
        
        elif response.json()["label"] == 'battery':
            advice = battery_advice()

        elif response.json()["label"] == 'glass':
            advice = glass_advice()
    else:

        if response.json()["label"] == 'biological':
            advice = organic_advice()

        elif response.json()["label"] == 'clothes':
            advice = clothes_advice()

    return {"pred": pred, "conf":conf, "advice": "Conseil: "+advice}


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
        
        pred_dict = pred_message(response)

        message = f"""<p>{pred_dict["pred"]}</p>
                      <p>{pred_dict["conf"]}</p>
                      <br>
                      <p>{pred_dict["advice"]}</p>"""

        os.system(f"cp {filename} ./App/static/{filename}")

        return render_template('results_classification.html',result_image = f"/{filename}", results_table=message)

    return render_template('classification.html')
