from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>il va falloir te mettre à jour sur des mots ou ce que tu veux. Tu vas pouvoir realiser ce que tu veux, ou peu importe quoi, mais avant il faut reviser des mots, ou se mettre a jour cest comme on veut. <a href=\"/motsreseaux\">les mots de reseau</a> pas que les mots reseaux</p>"
@app.route("/motsreseaux")
def hello_world():
    return "<p>router ca te parle</p>"
