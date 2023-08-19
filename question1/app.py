from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def num_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "numbers" in data and isinstance(data["numbers"], list):
                return data["numbers"]
    except:
        pass
    return None

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    valid_numbers = set()  # Using a set for efficient uniqueness

    for url in urls:
        numbers = num_from_url(url)
        if numbers is not None:
            valid_numbers.update(numbers)
    

    sorted_numbers = sorted(valid_numbers)
    res = {
        "numbers": sorted_numbers
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
