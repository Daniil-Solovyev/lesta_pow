from flask import Flask, request, jsonify
from models import Challenge, Algorithm
from pow_solver import LestaPowSolver
import requests

app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve_pow():
    data = request.json

    pow_challenge = Challenge(
        algorithm=Algorithm(**data['algorithm']),
        complexity=data['complexity'],
        random_string=data['random_string'],
        timestamp=data['timestamp'],
        type=data['type']
    )

    solver = LestaPowSolver(pow_challenge)
    nonce = solver.solve_challenge()

    return jsonify({'nonce': nonce})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)