from flask import *
from mongoengine import *
from models.video import Video
from youtube_dl import YoutubeDL
import mlab

app = Flask(__name__)

# session required a secret key
app.secret_key = "A super secret key"
mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos=videos)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        username= form['username']
        password = form['password']

        if username == 'admin' and password =='admin':
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            return 'Pemission denied, go away!!'

@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect(url_for('index'))

@app.route('/admin', methods = ['GET','POST'])
def admin():
    if 'loggedin' in session:
        if request.method == 'GET':
            videos= Video.objects()
            return render_template('admin.html', videos = videos)
        elif request.method == 'POST':
            form = request.form
            link = form['link']
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download=False)
            title = data['title']
            thumbnail = data['thumbnail']
            views = data['view_count']
            youtube_id = data['id']
            video= Video(title = title,
                            thumbnail= thumbnail,
                            views = views,
                            youtube_id=youtube_id,
                            link=link)
            video.save()
    else:
        return redirect(url_for('login'))

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template('detail.html', youtube_id=youtube_id)


if __name__ == '__main__':
  app.run(debug=True)
