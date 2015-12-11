from flask import make_response, jsonify, render_template
from app.app import app

@app.route("/")
def main():
	return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error':'not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
        return make_response(jsonify({'error':'bad request'}), 400)