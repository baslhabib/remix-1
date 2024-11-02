from flask import Flask, jsonify
from genetic_algorithm import run_genetic_algorithm

app = Flask(__name__)

@app.route('/run-genetic-algorithm', methods=['GET'])
def run_algorithm():
    final_population = run_genetic_algorithm()
    return jsonify(final_population)

if __name__ == '__main__':
    app.run(debug=True)
