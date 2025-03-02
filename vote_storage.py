from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///votes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Vote Model
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    selected_move = db.Column(db.String(50), nullable=False)
    ai_move = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Initialize DB
with app.app_context():
    db.create_all()

# Submit Vote Endpoint
@app.route('/submit-vote', methods=['POST'])
def submit_vote():
    data = request.get_json()
    user_email = data.get('email')
    selected_move = data.get('selected_move')
    ai_move = data.get('ai_move')

    if not user_email or not selected_move or not ai_move:
        return jsonify({'message': 'Missing data'}), 400

    new_vote = Vote(user_email=user_email, selected_move=selected_move, ai_move=ai_move)
    db.session.add(new_vote)
    db.session.commit()

    return jsonify({'message': 'Vote submitted successfully'}), 201

# Get Results Endpoint
@app.route('/get-results', methods=['GET'])
def get_results():
    last_24_hours = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
    votes = Vote.query.filter(Vote.timestamp >= last_24_hours).all()

    results = {}
    for vote in votes:
        results[vote.selected_move] = results.get(vote.selected_move, 0) + 1
    
    return jsonify({'results': results, 'total_votes': len(votes)})

if __name__ == '__main__':
    app.run(debug=True)
