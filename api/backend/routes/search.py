
from flask import Blueprint, request, jsonify
from utils.csv_loader import load_csv_data

data = load_csv_data()

search_bp = Blueprint('search_bp', __name__)

@search_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])  

    filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    results = filtered_data.to_dict(orient='records')
    return jsonify(results)
