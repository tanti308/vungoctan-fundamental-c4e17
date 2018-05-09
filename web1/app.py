from flask import Flask, render_template
app = Flask(__name__)   # tao ra 1 server(app) tao bang flask

@app.route('/')             # tao ra duong dan trang chu
def index():
    posts = [
            {
            "title": "Thơ con cóc",
            "content": "Ahihi",
            "author": "Củ lạc giòn tan",
            'gender': 1

            },
            {
            'title': " Thơ củ lạc",
            'content': '''Lạy chúa trên cao

                            Turn down for what''',
            'author': 'Nhật Minh',
            'gender': 0
            },
            {
            'title':  'Sầm Sơn',
            'content': '''Sầm Sơn sóng đánh dập dồn

                        Chị em phụ nữ hết mình vui chơi''',
            'author': 'Quang Dũng',
            'gender': 1
            }
            ]
    return render_template("index.html", posts=posts)

@app.route('/c4e')          # tao ra duong dan sub-web
def sayhi():
    return "Hi C4E 17"

@app.route('/sayhi/<name>/<age>') # gui 1 parameter=<name>
def sayhinext(name, age):        # route co parameter thi argument cua function cung phai co parameter day
    return "Hi {0}, you are {1} yr olds".format(name, age)

@app.route('/sum/<int:a>/<int:b>')  # dinh dang int a int
def sum_ab(a,b):
    return str(a + b)    # return chi nhan string


if __name__ == '__main__':  # khi chay truc tiep => khoi dong server
  app.run(debug=True)  #    debug = True: server cap nhat theo code minh thay doi
