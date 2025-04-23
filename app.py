from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        objectif = request.form.get("objectif")
        niveau = request.form.get("niveau")
        alimentation = request.form.get("alimentation")
        # Exemple simple : répondre avec un plan selon les infos
        programme = f"Programme personnalisé pour {objectif}, niveau {niveau}, alimentation {alimentation}"
        return render_template("index.html", programme=programme)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
