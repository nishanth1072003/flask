from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get("data", [])
    
    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Find the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets, default=None) if lowercase_alphabets else None
    
    # Construct the response
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with actual user data
        "email": "john@xyz.com",         # Replace with actual user data
        "roll_number": "ABCD123",        # Replace with actual user data
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    
    return jsonify(response), 200

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
