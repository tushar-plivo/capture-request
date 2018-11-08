from flask import request, url_for, send_file, jsonify
from flask_api import FlaskAPI, status, exceptions
import json
import sys


app = FlaskAPI(__name__)
requests_header_record = []
request_params_record = []

@app.route("/play/trumpet.mp3/requests", methods=['GET', 'POST'])
def requests_header_list():
    """
    List or create notes.
    """
    is_header = request.args.get('inspect')
    if is_header=='headers':
        app.logger.info(requests_header_record)
        return requests_header_record
    return []

@app.route("/play/trumpet.mp3", methods=['GET', 'POST'])
def host_file():
    """
    Play the record file.
    """
    try:
        app.logger.info('adding the request to the request history')
        header_data = request.headers
        header_data_dict = {}
        for item in header_data:
            header_data_dict[item[0]] = item[1] 
        app.logger.info(header_data_dict)
        requests_header_record.insert(0, header_data_dict)
        return send_file('/Users/tusharabhishek/Downloads/Trumpet.mp3', attachment_filename='trumpet.mp3')
        
    except Exception as e:
        return str(e)

@app.route("/play/trumpet.mp3/clear", methods=['GET', 'POST'])
def clear_record():
    """
    clears the requests record.
    """
    requests_header_record[:] = []
    return "request record cleared"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
