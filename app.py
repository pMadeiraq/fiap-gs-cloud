import pandas as pd
from flask import Flask, render_template

# Criar a aplicação Flask
app = Flask(__name__)

# Definir a rota principal (página inicial)
@app.route('/')
def index():
    try:
        # Carregar o CSV usando pandas.
        # O nome do arquivo deve ser exatamente esse.
        df = pd.read_csv('ai_job_trends_dataset.csv')
        
        # Converter o DataFrame do pandas para uma tabela HTML
        # Adiciona classes Bootstrap para deixar a tabela bonita
        data_html = df.to_html(classes='table table-striped table-hover', index=False)
        
        # Renderizar o template 'index.html' e passar a tabela para ele
        return render_template('index.html', table=data_html)
        
    except FileNotFoundError:
        return "Erro: Arquivo 'ai_job_trends_dataset.csv' não encontrado.", 404
    except Exception as e:
        return f"Ocorreu um erro: {e}", 500

# Esta parte é necessária para o Azure Web App saber como iniciar
if __name__ == '__main__':
    app.run()