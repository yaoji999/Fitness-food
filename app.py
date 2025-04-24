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

    return "<br>".join(plan)  # affiche chaque jour sur une nouvelle ligne

# ---------- GÉNÉRATION DE LA NUTRITION ----------
def generer_nutrition(obj, preferences):
    repas = []

    if obj == "perte de poids":
        repas = [
            "Petit-déjeuner : Flocons d’avoine + fruit + yaourt nature",
            "Déjeuner : Poulet grillé + légumes vapeur + riz complet",
            "Dîner : Soupe + tartine avocat + œuf dur",
            "Snack : Amandes ou pomme"
        ]
    elif obj == "prise de masse":
        repas = [
            "Petit-déjeuner : Oeufs + pain complet + banane",
            "Déjeuner : Steak haché + pâtes complètes + légumes",
            "Dîner : Quinoa + saumon + avocat",
            "Collation : Smoothie protéiné"
        ]
    else:  # maintien
        repas = [
            "Petit-déjeuner : Pain complet + fromage blanc + fruit",
            "Déjeuner : Poisson + légumes + pommes de terre",
            "Dîner : Soupe + œufs brouillés + légumes",
            "Snack : Oléagineux ou fruit"
        ]

    if preferences:
        repas.append(f"Préférences : {preferences}")

    return "<br>".join(repas)
