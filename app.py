from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    objectif = request.form['objectif']
    niveau = request.form['niveau']
    jours = request.form['jours']
    alimentation = request.form['alimentation']

    # Exemple simple de réponse (tu peux améliorer avec IA ensuite)
    programme = f"Programme pour {objectif}, niveau {niveau}, {jours} jours/semaine."
    nutrition = f"Plan nutrition adapté à une alimentation {alimentation}."

    return render_template('result.html', programme=programme, nutrition=nutrition)

if __name__ == '__main__':
    app.run(debug=True)
