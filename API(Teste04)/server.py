from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Carregando o arquivo CSV e convertendo para string
df = pd.read_csv('ArquivosTeste03/Relatorio_cadop.csv', encoding='utf-8', sep=';')
df = df.astype(str)  # Convertendo todas as colunas para string

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()  # Convertendo query para minúsculas
    field = request.args.get('field', 'all')
    
    if not query:
        return jsonify([])
    
    try:
        # Realizando a busca
        if field == 'all':
            # Busca em todas as colunas
            mask = df.apply(lambda x: x.str.lower().str.contains(query, na=False)).any(axis=1)
            results = df[mask]
        else:
            # Busca em campo específico
            if field in df.columns:
                mask = df[field].str.lower().str.contains(query, na=False)
                results = df[mask]
            else:
                return jsonify([])
        
        # Limitando a 100 resultados para melhor performance
        results = results.head(100)
        
        # Convertendo para formato JSON
        return jsonify(results.to_dict(orient='records'))
    except Exception as e:
        print(f"Erro na busca: {str(e)}")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True) 