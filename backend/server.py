from flask import Flask, request, jsonify
from flask_cors import CORS
from darkpattern import gemini, gemini_textmani
from TextManipulation import txtmani

# Create a Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Define a route that accepts POST requests
@app.route('/process_link', methods=['POST'])
def process_link():
    try:
        if request.is_json:
            json_data = request.json
            if 'link' in json_data:
                link = json_data['link']
                # Assuming gemini function returns a string, modify as needed
                res = gemini(link)
                txtmani(link)
                res2 = gemini_textmani()
                return jsonify({"text manipulation" : res2,"message": res, "link": link}), 200
            else:
                return jsonify({"error": "JSON object should contain 'link' key"}), 400
        else:
            return jsonify({"error": "Request body should be in JSON format"}), 400
    except Exception as e:
        # Handle any unexpected exceptions gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the app with host set to 0.0.0.0
    app.run(debug=True, host='0.0.0.0')
