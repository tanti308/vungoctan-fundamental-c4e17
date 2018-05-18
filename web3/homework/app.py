from flask import *#Flask, render_template, redirect, url_for
from mongoengine import *
from models.service import Service
import mlab

app = Flask(__name__)

# Connect database
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g,yob__lte=2000, address__contains='Hà Nội')
    return render_template('search.html', all_service=all_service)

@app.route('/service')
def service():
    all_services = Service.objects()
    return render_template('service.html', all_services=all_services)


@app.route('/detail/<service_id>')
def detail_id(service_id):
    service = Service.objects.with_id(service_id)
    return render_template('detail.html', service = service )

@app.route('/admin')
def admin():
    all_services = Service.objects()
    return render_template('admin.html', all_services = all_services)

@app.route('/new-service', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name= form['name']
        yob= form['yob']

        new_service = Service(name=name, yob=yob)
        new_service.save()
        return redirect(url_for('admin'))


@app.route('/update/<service_id>', methods = ['GET', 'POST'])
def update(service_id):
    if request.method == 'GET':
        service = Service.objects.with_id(service_id)
        return render_template ('update.html', service=service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        status = form['status']
        description = form['description']
        measurements = form['measurements']
        image = form['image']
        service = Service.objects.with_id(service_id)
        service.update(set__name=name,
                       set__yob=yob,
                       set__gender=gender,
                        set__height=height,
                        set__phone=phone,
                        set__address=address,
                        set__status=bool(status),
                        set__description=description,
                        set__measurements=measurements,
                        set__image=image)
        service.reload()
        return redirect(url_for('admin'))

@app.route("/delete/<service_id>")
def delete(service_id):
    id_del=Service.objects.with_id(service_id)
    if id_del is not None:
        id_del.delete()
    return redirect(url_for('admin'))


if __name__ == '__main__':
  app.run(debug=True)
