from flask import Flask, render_template, request, session, redirect
from myplace import Myplace
from bs4 import BeautifulSoup
import subprocess
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_mot_reseau", methods=["GET","POST"])
def add_one_mot_reseau():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into mot_reseau (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from mot_reseau')


        return render_template("mot_reseauform.html", mot_reseaus=user, one_user=one_user, the_title="add new mot_reseau")


    user = query_db('select * from mot_reseau')
    one_user = query_db("select * from mot_reseau limit 1", one=True)
    return render_template("mot_reseauform.html", mot_reseaus=user, one_user=one_user, the_title="add new mot_reseau")

@app.route("/add_one_type_donnee", methods=["GET","POST"])
def add_one_type_donnee():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into type_donnee (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from type_donnee')


        return render_template("type_donneeform.html", type_donnees=user, one_user=one_user, the_title="add new type_donnee")


    user = query_db('select * from type_donnee')
    one_user = query_db("select * from type_donnee limit 1", one=True)
    return render_template("type_donneeform.html", type_donnees=user, one_user=one_user, the_title="add new type_donnee")

@app.route("/add_one_programming_language", methods=["GET","POST"])
def add_one_programming_language():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into programming_language (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from programming_language')


        return render_template("programming_languageform.html", programming_languages=user, one_user=one_user, the_title="add new programming_language")


    user = query_db('select * from programming_language')
    one_user = query_db("select * from programming_language limit 1", one=True)
    return render_template("programming_languageform.html", programming_languages=user, one_user=one_user, the_title="add new programming_language")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,password,email,phone,country_id) values (:username,:password,:email,:phone,:country_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from user')


        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','password','email','phone','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','password','email','phone','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','password','email','phone','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from country')


        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_mot_reserve", methods=["GET","POST"])
def add_one_mot_reserve():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramming_language= query_db("select * from programming_language")

        one_user = query_db("insert into mot_reserve (name,programming_language_id) values (:name,:programming_language_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from mot_reserve')


        return render_template("mot_reserveform.html", mot_reserves=user, one_user=one_user, the_title="add new mot_reserve", touslesprogramming_language=touslesprogramming_language)


    touslesprogramming_language= query_db("select * from programming_language")

    user = query_db('select * from mot_reserve')
    one_user = query_db("select * from mot_reserve limit 1", one=True)
    return render_template("mot_reserveform.html", mot_reserves=user, one_user=one_user, the_title="add new mot_reserve", touslesprogramming_language=touslesprogramming_language)

@app.route("/add_one_experience", methods=["GET","POST"])
def add_one_experience():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into experience (script_reseau,user_id,description) values (:script_reseau,:user_id,:description)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from experience')


        return render_template("experienceform.html", experiences=user, one_user=one_user, the_title="add new experience")


    user = query_db('select * from experience')
    one_user = query_db("select * from experience limit 1", one=True)
    return render_template("experienceform.html", experiences=user, one_user=one_user, the_title="add new experience")

@app.route("/add_one_mot_reserve_experience", methods=["GET","POST"])
def add_one_mot_reserve_experience():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmot_reserve= query_db("select * from mot_reserve")

        one_user = query_db("insert into mot_reserve_experience (experience_id,mot_reserve_id) values (:experience_id,:mot_reserve_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from mot_reserve_experience')


        return render_template("mot_reserve_experienceform.html", mot_reserve_experiences=user, one_user=one_user, the_title="add new mot_reserve_experience", touslesmot_reserve=touslesmot_reserve)


    touslesmot_reserve= query_db("select * from mot_reserve")

    user = query_db('select * from mot_reserve_experience')
    one_user = query_db("select * from mot_reserve_experience limit 1", one=True)
    return render_template("mot_reserve_experienceform.html", mot_reserve_experiences=user, one_user=one_user, the_title="add new mot_reserve_experience", touslesmot_reserve=touslesmot_reserve)

@app.route("/add_one_type_donnee_experience", methods=["GET","POST"])
def add_one_type_donnee_experience():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslestype_donnee= query_db("select * from type_donnee")

        one_user = query_db("insert into type_donnee_experience (experience_id,type_donnee_id) values (:experience_id,:type_donnee_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from type_donnee_experience')


        return render_template("type_donnee_experienceform.html", type_donnee_experiences=user, one_user=one_user, the_title="add new type_donnee_experience", touslestype_donnee=touslestype_donnee)


    touslestype_donnee= query_db("select * from type_donnee")

    user = query_db('select * from type_donnee_experience')
    one_user = query_db("select * from type_donnee_experience limit 1", one=True)
    return render_template("type_donnee_experienceform.html", type_donnee_experiences=user, one_user=one_user, the_title="add new type_donnee_experience", touslestype_donnee=touslestype_donnee)

@app.route("/add_one_mot_reseau_experience", methods=["GET","POST"])
def add_one_mot_reseau_experience():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmot_reseau= query_db("select * from mot_reseau")

        one_user = query_db("insert into mot_reseau_experience (experience_id,mot_reseau_id) values (:experience_id,:mot_reseau_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from mot_reseau_experience')


        return render_template("mot_reseau_experienceform.html", mot_reseau_experiences=user, one_user=one_user, the_title="add new mot_reseau_experience", touslesmot_reseau=touslesmot_reseau)


    touslesmot_reseau= query_db("select * from mot_reseau")

    user = query_db('select * from mot_reseau_experience')
    one_user = query_db("select * from mot_reseau_experience limit 1", one=True)
    return render_template("mot_reseau_experienceform.html", mot_reseau_experiences=user, one_user=one_user, the_title="add new mot_reseau_experience", touslesmot_reseau=touslesmot_reseau)

@app.route("/add_one_past_current_village", methods=["GET","POST"])
def add_one_past_current_village():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into past_current_village (experience_id,lat,lon,name) values (:experience_id,:lat,:lon,:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from past_current_village')


        return render_template("past_current_villageform.html", past_current_villages=user, one_user=one_user, the_title="add new past_current_village")


    user = query_db('select * from past_current_village')
    one_user = query_db("select * from past_current_village limit 1", one=True)
    return render_template("past_current_villageform.html", past_current_villages=user, one_user=one_user, the_title="add new past_current_village")



@app.route("/searchjobcity", methods=["POST"])
def trouver_lieu_city():
    leslieu=Myplace(request.form["lieu"]).trouver1()

    return dict({"city":leslieu[0], "code":leslieu[1], "region":leslieu[3], "departement":leslieu[2], "pays":leslieu[2], "latitude":leslieu[4], "longitude":leslieu[5]})
@app.route("/add_one_region_network", methods=["GET","POST"])
def add_one_region_network():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslespast_current_village= query_db("select * from past_current_village")

        one_user = query_db("insert into region_network (past_current_village_id,person_name) values (:past_current_village_id,:person_name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from region_network')


        return render_template("region_networkform.html", region_networks=user, one_user=one_user, the_title="add new region_network", touslespast_current_village=touslespast_current_village)


    touslespast_current_village= query_db("select * from past_current_village")

    user = query_db('select * from region_network')
    one_user = query_db("select * from region_network limit 1", one=True)
    return render_template("region_networkform.html", region_networks=user, one_user=one_user, the_title="add new region_network", touslespast_current_village=touslespast_current_village)

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (country_id,name) values (:country_id,:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from city')


        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_departure_arrival", methods=["GET","POST"])
def add_one_departure_arrival():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        touslescity_arrival= query_db("select * from city_arrival")

        one_user = query_db("insert into departure_arrival (city_id,city_arrival_id,airline_company,timearrival,experience_id) values (:city_id,:city_arrival_id,:airline_company,:timearrival,:experience_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from departure_arrival')


        return render_template("departure_arrivalform.html", departure_arrivals=user, one_user=one_user, the_title="add new departure_arrival", touslescity=touslescity, touslescity_arrival=touslescity_arrival)


    touslescity= query_db("select * from city")

    touslescity_arrival= query_db("select * from city_arrival")

    user = query_db('select * from departure_arrival')
    one_user = query_db("select * from departure_arrival limit 1", one=True)
    return render_template("departure_arrivalform.html", departure_arrivals=user, one_user=one_user, the_title="add new departure_arrival", touslescity=touslescity, touslescity_arrival=touslescity_arrival)

