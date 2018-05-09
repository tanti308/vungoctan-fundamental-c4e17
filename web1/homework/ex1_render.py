from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')

@app.route('/bmi/<int:w>/<int:h>')

# bmi_condition = ['Severely underweight','Underweight','Normal','Overweight','Obese']
def index(w,h):
    h/=100                          # doi chieu cao cm => m
    bmi= (w/(h*h))
    bmi = float("{0:.1f}".format(bmi))
    if bmi < 16:
        condition = 'Severe underweight'
    elif 16 <= bmi <= 18.5:
        condition = 'Underweight'
    elif 18.5 <= bmi <= 25:
        condition = 'Normal'
    elif 25 <= bmi <= 30:
        condition = 'Overweight'
    else:
        condition = 'Obese'
    post = [bmi, condition]

    return render_template('index1.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
