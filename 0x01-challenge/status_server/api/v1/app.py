#!/usr/bin/python3
"""Web server
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/api/v1/status', methods=['GET'])
def api_status():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

