from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def inedx():
    titulos:str = 'Home'
    return render_template('index.html', titulos=titulos)

if __name__ == '__main__':
    app.run(debug=True)