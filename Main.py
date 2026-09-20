import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from rubik_solver import utils

app = Flask(__name__)
CORS(app) # Cho phép Front-end gọi API chéo tên miền

@app.route('/solve', methods=['POST'])
def solve_cube():
    try:
        data = request.json
        cube_state = data.get('state', '')
        
        # Thư viện tính toán thuật toán giải
        solution = utils.solve(cube_state, 'Kociemba')
        
        # Chuyển đổi kết quả thành mảng chuỗi các nước đi
        moves = [str(move) for move in solution]
        
        return jsonify({'status': 'success', 'solution': moves})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
  
