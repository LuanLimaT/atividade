from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.mundo  # Nome do banco de dados

# Coleções com o banco
paises_collection = db.paises
cidades_collection = db.cidades
rios_collection = db.rios

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_pais', methods=['POST'])
def adicionar_pais():
    pais_data = {
        'nome': request.form['pais_nome'],
        'continente': request.form['pais_continente'],
        'populacao': request.form['pais_populacao'],
        'pib': request.form['pais_pib'],
        'expectativa': request.form['pais_expec'],
    }
    paises_collection.insert_one(pais_data)
    return redirect(url_for('listar_paises'))

@app.route('/adicionar_cidade', methods=['POST'])
def adicionar_cidade():
    cidade_data = {
        'nome': request.form['cidade_nome'],
        'pais': request.form['cidade_pais'],
        'populacao': request.form['cidade_populacao'],
        'capital': request.form['cidade_capital'] == 'Sim'
    }
    cidades_collection.insert_one(cidade_data)
    return redirect(url_for('listar_cidades'))

@app.route('/adicionar_rio', methods=['POST'])
def adicionar_rio():
    rio_data = {
        'nome': request.form['rio_nome'],
        'nascente': request.form['rio_nascente'],
        'pais': request.form['rio_pais'],
        'continente': request.form['rio_continente']
    }
    rios_collection.insert_one(rio_data)
    return redirect(url_for('listar_rios'))

@app.route('/listar_paises')
def listar_paises():
    paises = paises_collection.find()
    return render_template('listagem_paises.html', paises=paises)

@app.route('/listar_cidades')
def listar_cidades():
    cidades = cidades_collection.find()
    return render_template('listagem_cidades.html', cidades=cidades)

@app.route('/listar_rios')
def listar_rios():
    rios = rios_collection.find()
    return render_template('listagem_rios.html', rios=rios)

if __name__ == '__main__':
    app.run()
