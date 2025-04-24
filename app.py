from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    objectif = request.form['objectif']
    niveau = request.form['niveau']
    jours = int(request.form['jours'])
    preferences = request.form['alimentation']

    sport = generer_sport(objectif, niveau, jours)
    nutrition = generer_nutrition(objectif, preferences)

    return render_template('result.html', sport=sport, nutrition=nutrition)

# ---------- GÉNÉRATION DU SPORT ----------
def generer_sport(obj, niveau, freq):
    jours_dispo = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    plan = []

    for i in range(freq):
        jour = jours_dispo[i % len(jours_dispo)]
        if obj == "perte de poids":
            if niveau == "débutant":
                séance = "Marche rapide 30 min + gainage 2x30s"
            elif niveau == "intermédiaire":
                séance = "HIIT 20 min + abdos"
            else:
                séance = "Course fractionnée 30 min + muscu légère"
        elif obj == "prise de masse":
            séance = "Musculation haut/bas split 45 min"
        else:
            séance = "Renforcement + mobilité 30 min"

        plan.append(f"{jour} : {séance}")

    return "\n".join(plan)

# ---------- GÉNÉRATION DE LA NUTRITION ----------
def generer_nutrition(obj, pref):
    if obj == "perte de poids":
        petit = "Flocons d’avoine + fruit + yaourt nature"
        dej = "Poulet grillé + légumes vapeur + riz complet"
        diner = "Soupe + tartine avocat + œuf dur"
        snack = "Amandes ou pomme"
    elif obj == "prise de masse":
        petit = "Œufs brouillés + pain complet + smoothie banane"
        dej = "Pâtes + steak haché + haricots verts"
        diner = "Poisson + patates douces + brocoli"
        snack = "Shake protéiné + banane"
    else:
        petit = "Pain complet + beurre d’amande + thé"
        dej = "Quinoa + légumes + œufs"
        diner = "Salade composée + céréales + tofu ou poulet"
        snack = "Fruit ou yaourt nature"

    if pref:
        ajustement = f" (adapté pour : {pref})"
    else:
        ajustement = ""

    return f"""
    Petit-déjeuner : {petit}
    Déjeuner : {dej}
    Dîner : {diner}
    Snack : {snack}
    {ajustement}
    """

if __name__ == '__main__':
    app.run(debug=True)
