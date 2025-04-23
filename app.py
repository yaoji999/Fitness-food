
from flask import Flask, request, render_template
import os

app = Flask(__name__)

def generer_plan(age, poids, objectif, contexte):
    objectif = objectif.lower()
    contexte = contexte.lower()

    # Détection du niveau
    if "débutant" in contexte or "jamais" in contexte:
        niveau = "débutant"
    elif "intermédiaire" in contexte or "régulier" in contexte:
        niveau = "intermédiaire"
    else:
        niveau = "standard"

    # Détection du type de plan
    perte_poids = "perdre" in objectif or "maigrir" in objectif
    prise_masse = "prendre" in objectif or "muscle" in objectif

    # Plan sport
    if niveau == "débutant":
        sport = "- Lundi : 30 min marche rapide + gainage\n- Mercredi : Circuit full body à la maison\n- Vendredi : Étirements + gainage + squat poids de corps"
    elif niveau == "intermédiaire":
        sport = "- Lundi : Séance full body\n- Mercredi : Cardio 30 min + abdos\n- Vendredi : Muscu ciblée haut du corps"
    else:
        sport = "- Lundi : HIIT 30 min\n- Mardi : Renforcement bas du corps\n- Jeudi : Yoga/étirements\n- Samedi : Cardio long (footing/vélo)"

    # Plan nutrition
    if perte_poids:
        nutrition = "Petit-déj : yaourt grec + flocons + fruit\nDéj : riz complet + légumes + poulet\nDîner : soupe + œuf dur + tartine avocat"
    elif prise_masse:
        nutrition = "Petit-déj : porridge avoine + banane + beurre de cacahuète\nDéj : pâtes + viande + légumes\nDîner : omelette 3 œufs + riz"
    else:
        nutrition = "Petit-déj : pain complet + fromage blanc + fruit\nDéj : quinoa + légumes + dinde\nDîner : salade + œufs + patate douce"

    return f"Objectif : {objectif}\nNiveau : {niveau}\n\nProgramme Sport :\n{sport}\n\nPlan Nutrition :\n{nutrition}"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        age = request.form["age"]
        poids = request.form["poids"]
        objectif = request.form["objectif"]
        contexte = request.form["contexte"]
        response = generer_plan(age, poids, objectif, contexte)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
