from flask import Flask, render_template, request
#Cria a aplicação Flask
app = Flask(__name__)

@app.route('/calculadora')
def exibir_calculadora():
    return render_template('calculadora.html', resultado="Faça!")

@app.route('/processar', methods=['POST'])
def processar_resultado():


#Esta função recebe os dados das caixas de entrada, processa e retorna o resultado


#Capturar os dados do formulário
#O nome entre parentêses deve ser igual ao nome 'name' no HTML
#request.form pega as informações dos campos das caixas de entrada

    valor1 = float(request.form.get('valor1'))
    valor2 = float(request.form.get('valor2'))
    operacao = request.form.get('operacao')

#Condições das operações

    if operacao == "Soma":
        valor_final = valor1 + valor2
    elif operacao == "Subtração":
        valor_final = valor1 - valor2
    elif operacao == "Multiplicação":
        valor_final = valor1 * valor2
    elif operacao == "Divisão":
        valor_final = valor1 / valor2

    return render_template('calculadora.html', resultado=valor_final)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)