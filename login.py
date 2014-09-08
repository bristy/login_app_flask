from flask import Flask, session, render_template, url_for
from flask import request, escape, redirect

app = Flask(__name__)


@app.route('/')
def index():
    print 'username'
    if 'username' in session:
        name = session['username']
        return render_template('welcome.html', name=name)
    return render_template('login.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        session['username'] = name
    return redirect(url_for('index'))

@app.route('/logout/')
def logout():
    #remove user from tag
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=True)
