from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vista2')
def MuseoFrida():
    return render_template('vista2.html')

@app.route('/MuseoFrida')
def vista3():
    return render_template('MuseoFrida.html')

@app.route('/PinturasAbstractas')
def PinturasAbstractas():
  return render_template('PinturasAbstractas.html')

if __name__ == "__main__":
    app.run(debug=True, port=3800)
