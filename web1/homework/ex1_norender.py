from flask import Flask
app = Flask(__name__)

@app.route('/')

@app.route('/bmi/<int:w>/<int:h>')

# bmi_condition = ['Severely underweight','Underweight','Normal','Overweight','Obese']
def bmi_calc(w, h):
    h/=100                          # doi chieu cao cm => m
    bmi_condition = ['Severely underweight','Underweight','Normal','Overweight','Obese']
    bmi= w/(h*h)
    if bmi < 16:
        return "Your BMI: {0:10.1f}. {1}".format(bmi, bmi_condition[0])
    elif 16 <= bmi <= 18.5:
        return "Your BMI: {0:10.1f}. {1}".format(bmi, bmi_condition[1])
    elif 18.5 <= bmi <= 25:
        return "Your BMI: {0:10.1f}. {1}".format(bmi, bmi_condition[2])
    elif 25 <= bmi <= 30:
        return "Your BMI: {0:10.1f}. {1}".format(bmi, bmi_condition[3])
    else:
        return "Your BMI: {0:10.1f}. {1}".format(bmi, bmi_condition[4])

if __name__ == '__main__':
    app.run(debug=True)
