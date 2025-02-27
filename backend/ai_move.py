import random
from flask import Flask, jsonify

app = Flask(__name__)

# Predefined list of attack moves with corresponding video URLs
moves = [
    {"name": "Sea Breath", "video": "https://cloudhost.com/videos/flame_strike.mp4"},
    {"name": "Silver Screen", "video": "https://cloudhost.com/videos/thunder_shock.mp4"},
    {"name": "Fury", "video": "https://cloudhost.com/videos/aqua_wave.mp4"},
    {"name": "Baton Quake", "video": "https://cloudhost.com/videos/rock_smash.mp4"},
]

@app.route('/ai-move', methods=['GET'])
def ai_move():
    ai_choice = random.choice(moves)
    return jsonify({"ai_move": ai_choice})

if __name__ == '__main__':
    app.run(debug=True)
