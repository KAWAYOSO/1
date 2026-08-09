from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Страница "Храбрость"
@app.route('/bravery')
def bravery():
    return render_template('quality.html')

# Страница "Мудрость"
@app.route('/wisdom')
def wisdom():
    return render_template('skill.html')

# Страница "Сила"
@app.route('/strength')
def strength():
    return render_template('last.html')

if __name__ == '__main__':
    app.run(debug=True)