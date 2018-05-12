from flask import Flask, render_template
from mongoengine import *
from models.customer import Customer
import mlab

app = Flask(__name__)

# Connect database
mlab.connect()


# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def search():
    all_customer = Customer.objects(contacted=False, gender =0)
    return render_template('search.html', all_customer=all_customer)



if __name__ == '__main__':
  app.run(debug=True)
