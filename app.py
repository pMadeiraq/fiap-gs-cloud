import pandas as pd
from flask import Flask, render_template
import os  # <--- 1. IMPORTAÇÃO NOVA

# --- 2. LINHAS NOVAS ---
# Pega o caminho absoluto da pasta onde o app.py está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Cria o caminho completo para o arquivo CSV
CSV_PATH = os.path.join(BASE_DIR, 'ai_job_trends_dataset.csv')
# ------------------------

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # --- 3. LINHA MODIFICADA ---
        # Agora ele usa o caminho completo e exato
        df = pd.read_csv(CSV_PATH) 
        
        data_html = df.to_html(classes='table table-striped table-hover', index=False)
        return render_template('index.html', table=data_html)
        
    except FileNotFoundError:
        # Atualizei a mensagem de erro para ser mais clara
        return f"Erro: Arquivo CSV não encontrado no caminho: {CSV_PATH}", 404
    except Exception as e:
        return f"Ocorreu um erro: {e}", 500

if __name__ == '__main__':
    app.run()