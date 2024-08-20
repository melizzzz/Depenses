from flask import Flask, render_template

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la page d'un mois spécifique (ex: Janvier)
@app.route('/mois/<mois>')
def mois_detail(mois):
    # Exemple de données que vous pouvez passer au template
    data = {
        "mois": mois.capitalize(),
        "total": "1000,00 €",
        "categories": [
            {"nom": "Essence", "montant": "1525,25 €"},
            {"nom": "Nourriture", "montant": "1525,25 €"},
            {"nom": "Shopping", "montant": "1525,25 €"},
            {"nom": "Frais fixes", "montant": "1525,25 €"}
        ]
    }
    return render_template('mois.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
