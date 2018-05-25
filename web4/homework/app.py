from flask import Flask, render_template
from mongoengine import *
from models.user import User
from models.service import Service

import mlab

app = Flask(__name__)
app.secret_key = "A super secret key"
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username= form['username']
        password = form['password']

        user = User(fullname = fullname,
                    email = email,
                    username = username,
                    password= password )
        user.save()            

        if username in User['username'] or email in User['email']:
            return 'Invalid username or email'

        else:


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method = 'GET':
        return render_template('signup.html')
    elif request.method = 'POST':
        form = request.form
        username = form['username']
        password = form['password']


@app.route('/detail')
def detail():

@app.route('/create')
def create():

@app.route('/search')
def search():

@app.route('/update/<service_id>', methods = ['GET', 'POST'])
def update(service_id):
    if request.method == 'GET':
        service = Service.objects.with_id(service_id)
        return render_template ('update.html', service=service)
    elif request.method == 'POST':
        form = request.form
        image = form['image']
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        email = form['email']
        height = form['height']
        measurements = form['measurements']
        phone = form['phone']
        description = form['description']
        address = form['address']
        job= form['job']
        company = form['company']
        status = form['status']
        service = Service.objects.with_id(service_id)
        service.update(set__name=name,
                       set__yob=yob,
                       set__gender=gender,
                        set__height=height,
                        set__phone=phone,
                        set__email=email,
                        set__address=address,
                        set__job=job,
                        set__company=company,
                        set__status=bool(status),
                        set__description=description,
                        set__measurements=measurements,
                        set__image=image)
        service.reload()
        return redirect(url_for('admin'))

@app.route('/delete/<service_id>')
def delete():
    Service.objects(id= service_id).delete()

@app.route('/deleteall')
def delete_all():
    Service.objects().delete()

if __name__ == '__main__':
  app.run(debug=True)
