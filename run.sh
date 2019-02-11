python3 -m venv venv
. venv/bin/activate
pip3 install Flask
export FLASK_APP=.
export FLASK_ENV=development
flask init-db
flask run