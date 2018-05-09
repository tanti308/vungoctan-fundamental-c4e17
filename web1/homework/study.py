from flask import Flask, render_template,redirect
app = Flask(__name__)

@app.route('/')

@app.route('/aboutme')
def index():
    user_info = {
                'name': 'Vu Ngoc Tan',
                'age' : 22,
                'gender': 'male',
                'work': 'student',
                'school': 'National Economic University',
                'hobbies': '3G, reading, gaming,...'
                }
    return render_template('index0.html', user_info=user_info)

@app.route('/school')
def return_school():
    return redirect('http://techkids.vn ', code=302)

if __name__ == '__main__':
    app.run(debug=True)
