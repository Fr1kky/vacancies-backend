from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/get_rate', methods=['GET'])
def get_rate_route():
    response = {"rate": 100}
    return jsonify(response)


@app.route('/get_vacancy', methods=['GET'])
def get_vacancy():
    response = {
        "title": "Computer Vision Engineer",
        "company": "Google",
        "salary": "300$",
        "location": "New York",
        "job_type": 1,
        "description": "Some comments",
        "experience": "0-1"
    }
    return jsonify(response)


@app.route('/get_rank', methods=['POST'])
def get_rank_route():
    request_dict = request.json
    salary_starts_from = request_dict.get('salary_starts_from')

    if not salary_starts_from:
        return jsonify({'error': 'salary_starts_from field is required'})

    if salary_starts_from <= 0:
        return jsonify({'error': 'salary_starts_from must be greater than 0'})

    if 0 < salary_starts_from < 1000:
        return jsonify({'rank': 'junior'})
    elif 1000 < salary_starts_from < 3000:
        return jsonify({'rank': 'middle'})
    elif 3000 < salary_starts_from < 5000:
        return jsonify({'rank': 'senior'})
    elif salary_starts_from > 5000:
        return jsonify({'rank': 'god'})


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
