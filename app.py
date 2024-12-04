from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ourteam')
def our_team():
    return render_template('ourteam.html')

@app.route('/howtouse')
def how_to_use():
    return render_template('how.html')

if __name__ == '__main__':
    app.run(debug=True)
