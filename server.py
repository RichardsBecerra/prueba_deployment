from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= 'clave'


@app.route('/')
def index():
    if 'count' not in session:
        session ['count'] = 0
    else:
        session ['count'] +=1

    return render_template('index.html')

@app.route('/dobleclick')
def dobleclick():
    if 'count' not in session:
        session ['count']= 0
    else:
        session ['count'] += 2

    return render_template('index.html')

#cuenta las veces que se visito la pagina
@app.route('/formulario', methods=['POST'])
def formulario():
    cantidad = request.form.get('cantidad')
    
    if request.method == 'POST':
        if 'count_dos' not in session:
            session ['count_dos'] = int(cantidad)
        else:
            session ['count_dos'] += int(cantidad)

        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
