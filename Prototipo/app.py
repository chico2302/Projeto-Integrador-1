from flask import Flask, render_template, request
import data_service

app = Flask(__name__)

@app.route('/')
def index():
    # Filtro dinâmico de período de anos (Padrão: Histórico Total)
    ano_min = int(request.args.get('ano_min', 1980))
    ano_max = int(request.args.get('ano_max', 2023))
    
    # Validação simples para evitar ranges invertidos
    if ano_min > ano_max:
        ano_min, ano_max = ano_max, ano_min
    
    # Processamento dos dados com base no filtro de período
    cards = data_service.obter_dados_cards(ano_min, ano_max)
    graficos = data_service.obter_dados_graficos(ano_min, ano_max)
    tabela = data_service.obter_dados_tabela(ano_min, ano_max)
    
    return render_template(
        'index.html',
        dados_cards=cards,
        graficos=graficos,
        dados_tabela=tabela,
        ano_min=ano_min,
        ano_max=ano_max
    )

if __name__ == '__main__':
    app.run(debug=True)