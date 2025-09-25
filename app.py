from flask import Flask, render_template, url_for, request, redirect      
import os
import csv


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre_equipe.html')



@app.route('/glossario')
def glossario():
    glossario_de_termos = []
    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossario_de_termos.append(linha)
    return render_template(template_name_or_list='glossario.html', glossario=glossario_de_termos)

@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

@app.route('/excluir_termo/<string:termo>', methods=['POST'])
def excluir_termo(termo):

    linhas_manter = []
    termo_encontrado = False
    try:
        with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')

            #Encontrar e remover o termo pelo ID
            for linha in reader:
                if linha and linha[0] != termo:
                    linhas_manter.append(linha)
                elif linha and linha[0] == termo:
                    termo_encontrado = True

            #Salvar as alterações no arquivo CSV
        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerows(linhas_manter)
        
        if termo_encontrado:
            print(f"Termo '{termo}' excluído com sucesso.")
        else:
            print(f"Termo '{termo}' não encontrado.")    

    except Exception as e:
        print(f"{e} - Arquivo não encontrado")

    return redirect(url_for('glossario'))


app.run()