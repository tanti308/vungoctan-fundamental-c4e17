from flask import Flask
app = Flask(__name__)

@app.route('/')

@app.route('/bmi/<int:w>/<int:h>')

# bmi_condition = ['Severely underweight','Underweight','Normal','Overweight','Obese']
def bmi_calc(w, h):
    h/=100                          # doi chieu cao cm => m
    bmi= w/(h*h)
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

    return "Your BMI: {0:10.1f}. {1}".format(bmi, condition)
if __name__ == '__main__':
    app.run(debug=True)
