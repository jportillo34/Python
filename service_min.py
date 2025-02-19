from flask import Flask, request, jsonify

app = Flask(__name__)

# NOTA: La siguiente linea es un DECORATOR de Flask.
@app.route('/min', methods=['GET'])
def min():
    num1 = request.args.get('num1')  # Get num1 from query parameters
    num2 = request.args.get('num2')  # Get num2 from query parameters

    # Debugging: Print out the values of num1 and num2
    print(f"Received num1: {num1}, num2: {num2}")

    # Check if both parameters are provided
    if num1 is None or num2 is None:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        num1 = float(num1)  # Convert to float for calculation
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide valid numbers.'}), 400

    result = num1 - num2
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Runs on port 5001

