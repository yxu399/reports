# Reports Generator Microservice
# main

from flask import Flask, request, jsonify
from reportGeneration import generateReport


app = Flask(__name__)


# arbitrary route for demonstration
@app.route('/')
def index():
    return 'Reports Index Page'


# post request with json data from client app
@app.post('/report')
def report_post():
    """ Receive POST request with json data from client.

    Unpack json data from request.

    Pass data object to generateReport function to generate report.
    """
    # unpack json data from request
    data = request.get_json()

    # check for empty data:
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    
    # validate required fields
    if 'report' not in data or 'data' not in data:
        return jsonify({"error": "Missing 'report' or 'data' field"}), 400
    try:
        # generate report
        report_result = generateReport(data)

        # return report as JSON
        return jsonify(report_result), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
