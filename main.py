
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    if (a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit()):
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        d = float(request.form['d'])
        if (a>b):
            result = (a - b)
            stavka = (d / 12)
            konech = format((result * stavka) / ((1 - (1 / (1 + stavka))) * c * 12), '.2f')
            return render_template('result.html', roots=konech)
        else:
            return render_template('result.html', roots ="Введите повторно стоимость и первоначальный взнос" )
    else:
        return render_template('result.html', roots="Ошибка, введите повторно")

if __name__ == "__main__":
    app.run(debug=True)