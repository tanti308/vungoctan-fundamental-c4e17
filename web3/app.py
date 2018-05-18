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

@app.route('/admin')
def admin():
    all_services = Service.objects()
    return render_template('admin.html', all_services=all_services)

@app.route('/deleteall')
def delete_all():
    Service.objects().delete()
# @app.route('/delete/<service_id>')
# def delete(service_id):
#     service_del=Service.objects.with_id(service_id)
#     if service_del is not None:
#         service_del.delete()
#         return redirect(url_for('admin'))
#     else:
#         return 'Service not found'
# @app.route('/new-service', methods=['GET','POST'])
# def create():
#     if request.method == 'GET':
#         return render_template('new-service.html')
#     elif request.method == 'POST':
#         form = request.form
#         name= form['name']
#         yob= form['yob']
#
#         new_service = Service(name=name, yob=yob)
#         new_service.save()
#         return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
