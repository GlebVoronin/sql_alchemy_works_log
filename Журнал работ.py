from flask import Flask
from flask import render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/astronauts.sqlite")
session = db_session.create_session()
jobs = session.query(Jobs).all()
@app.route('/')
def jobs_list():
    return render_template('jobs.html', jobs=jobs)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')