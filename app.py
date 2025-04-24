from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    objectif = request.form['objectif']
    niveau = request.form['niveau']
    jours = request.form['jours']
    preferences = request.form['alimentation']

    # Logique de base (à personnaliser ensuite)
    programme_sport = f"Programme {objectif} pour niveau {niveau}, {jours} séances/semaine."
    programme_nutrition = f"Nutrition adaptée à tes préférences : {preferences if preferences else 'aucune préférence'}."

    return render_template(
        'result.html',
        sport=programme_sport,
        nutrition=programme_nutrition
    )
