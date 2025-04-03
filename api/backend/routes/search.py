from flask import Blueprint, request, jsonify
import unicodedata
from utils.csv_loader import load_csv_data

data = load_csv_data()

search_bp = Blueprint('search_bp', __name__)

def normalize_text(text):
    # Remove acentos e converte o texto para minúsculas
    text = unicodedata.normalize('NFKD', str(text)).encode('ASCII', 'ignore').decode('ASCII')
    return text.lower()

@search_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify([]) 

   
    query = normalize_text(query)

    
    filtered_data = data[data.apply(
        lambda row: row.astype(str).apply(normalize_text).str.contains(query).any(), axis=1
    )]

    
    results = filtered_data.to_dict(orient='records')
    return jsonify(results)
