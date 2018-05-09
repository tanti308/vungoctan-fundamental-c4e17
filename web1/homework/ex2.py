from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/user/<username>')

def index(username):
    users = {
            'quy':  {
                    'name': 'Dinh Cong Quy',
                    'age': 20,
                    'gender': 'male',
                    'work': 'teaching assistant'
            },
            'tuananh':{
                    'name': 'Huynh Tuan Anh',
                    'age': 25,
                    'gender': 'male',
                    'work': 'instructor'
            },
            'quan': {
                    'name': 'Nguyen Anh Quan',
                    'age': 22,
                    'gender': 'male',
                    'work': 'teaching assistant'
            }
    }
    if username in users.keys():
        post = users[username]
        return render_template('index2.html', post = post)
    else:
        return 'User not found'

if __name__ == '__main__':
    app.run(debug=True)
