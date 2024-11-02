from flask import Flask, jsonify
from genetic_algorithm import run_genetic_algorithm

app = Flask(__name__)

@app.route('/run-genetic-algorithm', methods=['GET'])
def run_genetic_algorithm():
    best_individual, best_fitness = genetic_algorithm()
    return jsonify({"best_individual": best_individual, "fitness": best_fitness})


if __name__ == '__main__':
    app.run(debug=True)
