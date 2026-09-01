
mkdir templates 
python3 scaffold.py mot_reseau name
python3 scaffold.py type_donnee name
python3 scaffold.py programming_language name
python3 scaffold.py user username password email phone country_id:references
python3 scaffold.py country name
python3 scaffold.py mot_reserve name programming_language_id:references
python3 scaffold.py experience script_reseau user_id description
python3 scaffold.py mot_reserve_experience experience_id mot_reserve_id:references
python3 scaffold.py type_donnee_experience experience_id type_donnee_id:references
python3 scaffold.py mot_reseau_experience experience_id mot_reseau_id:references
python3 scaffold.py past_current_village experience_id lat lon name
python3 scaffold.py region_network past_current_village_id:references person_name
python3 scaffold.py city country_id:references name
python3 scaffold.py departure_arrival  city_id:references city_arrival_id:references airline_company timearrival experience_id
