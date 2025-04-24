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

    return render_template('result.html', sport=sport, jours_repas=nutrition)

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
    if obj == "perte de poids":
        jours_repas = {
            "Lundi": {
                "petit_dej": "Smoothie banane + flocons d’avoine + graines de chia",
                "dejeuner": "Poulet grillé + patate douce + brocoli vapeur",
                "diner": "Soupe de lentilles + pain complet",
                "snack": "Amandes"
            },
            "Mardi": {
                "petit_dej": "Tartine complète + avocat + œuf au plat",
                "dejeuner": "Saumon + riz complet + courgettes grillées",
                "diner": "Buddha bowl (quinoa, pois chiches, légumes)",
                "snack": "Pomme"
            },
            "Mercredi": {
                "petit_dej": "Yaourt grec + granola + fraises",
                "dejeuner": "Dinde + légumes rôtis + quinoa",
                "diner": "Omelette aux légumes + salade verte",
                "snack": "Barre protéinée maison"
            },
            "Jeudi": {
                "petit_dej": "Pain complet + beurre d’amande + banane",
                "dejeuner": "Bœuf sauté + riz basmati + légumes asiatiques",
                "diner": "Velouté de potimarron + tartine de chèvre",
                "snack": "Noix ou clémentine"
            }
        }
    elif obj == "prise de masse":
        jours_repas = {
            "Lundi": {
                "petit_dej": "Oeufs + pain complet + banane",
                "dejeuner": "Steak haché + pâtes complètes + légumes",
                "diner": "Quinoa + saumon + avocat",
                "snack": "Smoothie protéiné"
            },
            "Mardi": {
                "petit_dej": "Porridge + beurre de cacahuète + miel",
                "dejeuner": "Poulet rôti + riz + haricots verts",
                "diner": "Omelette au fromage + légumes",
                "snack": "Fruit sec"
            },
            "Mercredi": {
                "petit_dej": "Pain complet + œufs brouillés",
                "dejeuner": "Poisson blanc + pommes de terre + salade",
                "diner": "Wok de tofu + riz",
                "snack": "Lait + noix"
            },
            "Jeudi": {
                "petit_dej": "Crêpes protéinées + fruits rouges",
                "dejeuner": "Bœuf + légumes + riz",
                "diner": "Pâtes au thon + légumes",
                "snack": "Barre de céréales"
            }
        }
    else:  # maintien
        jours_repas = {
            "Lundi": {
                "petit_dej": "Pain complet + fromage blanc + fruit",
                "dejeuner": "Poisson + légumes + pommes de terre",
                "diner": "Soupe + œufs brouillés + légumes",
                "snack": "Oléagineux ou fruit"
            },
            "Mardi": {
                "petit_dej": "Yaourt nature + muesli + banane",
                "dejeuner": "Salade composée + œuf dur",
                "diner": "Tartine chèvre-miel + soupe de légumes",
                "snack": "Compote sans sucre"
            },
            "Mercredi": {
                "petit_dej": "Céréales complètes + lait végétal",
                "dejeuner": "Poulet grillé + semoule + légumes rôtis",
                "diner": "Omelette + pain complet",
                "snack": "Fruit frais"
            },
            "Jeudi": {
                "petit_dej": "Tartine beurre + confiture maison",
                "dejeuner": "Filet de poisson + riz + légumes verts",
                "diner": "Soupe + crudités + œufs",
                "snack": "Amandes"
            }
        }

    return jours_repas
