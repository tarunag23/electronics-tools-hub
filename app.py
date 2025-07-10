from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import json
import os
from datetime import datetime
from data_collector import ElectronicsToolsCollector

app = Flask(__name__)
CORS(app)

# Initialize electronics tools collector
collector = ElectronicsToolsCollector()

@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template('index.html')

@app.route('/api/tools')
def get_tools():
    """API endpoint to get all developer tools"""
    try:
        with open('data/tools.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data not found. Please refresh data first."}), 404

@app.route('/api/tools/search')
def search_tools():
    """API endpoint to search electronics tools by keyword"""
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '')
    license_type = request.args.get('license', '')

    try:
        with open('data/tools.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        tools = data.get('tools', [])

        # Filter by search query
        if query:
            tools = [tool for tool in tools if
                    query in tool['name'].lower() or
                    query in tool['description'].lower() or
                    query in tool['category'].lower()]

        # Filter by category
        if category:
            tools = [tool for tool in tools if tool['category'].lower() == category.lower()]

        # Filter by license type
        if license_type:
            tools = [tool for tool in tools if tool.get('license', '').lower() == license_type.lower()]

        return jsonify({
            "tools": tools,
            "count": len(tools),
            "query": query,
            "category": category,
            "license": license_type
        })
    except FileNotFoundError:
        return jsonify({"error": "Data not found. Please refresh data first."}), 404

@app.route('/api/refresh')
def refresh_data():
    """API endpoint to refresh/update data"""
    try:
        result = collector.collect_all_data()
        return jsonify({
            "message": "Data refreshed successfully",
            "timestamp": datetime.now().isoformat(),
            "tools_count": len(result.get('tools', []))
        })
    except Exception as e:
        return jsonify({"error": f"Failed to refresh data: {str(e)}"}), 500

@app.route('/api/categories')
def get_categories():
    """API endpoint to get all available categories"""
    try:
        with open('data/tools.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        categories = list(set(tool['category'] for tool in data.get('tools', [])))
        return jsonify({"categories": sorted(categories)})
    except FileNotFoundError:
        return jsonify({"error": "Data not found. Please refresh data first."}), 404

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # Collect initial data if not exists
    if not os.path.exists('data/tools.json'):
        print("Collecting initial data...")
        collector.collect_all_data()

    # Get port from environment variable for deployment platforms
    port = int(os.environ.get('PORT', 5000))

    app.run(debug=False, host='0.0.0.0', port=port)
