from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
import os

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'supersecretkey')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Initialize DB
with app.app_context():
    db.create_all()

# Register Endpoint
@app.route('/register', methods=['POST', 'GET', 'HEAD'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201
@app.route("/register", methods=["GET", "POST", "HEAD"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201
else:
    # Serve registration form for GET requests
    return '''
    <html>
    <body>
    <h2>Register</h2>
    <form method='POST'>
    <input type="email" name="email" placeholder="Enter your email" required><br>
    <input type="password" name="password" placeholder="Enter password" required><br>
    <input type="submit" value="Register">
    </form>
    </body>
    </html>
    '''
    #Serve regeistration form for GET requests
    return '''
    <html>
    <body>
    <h2>Register</h2>
    <form method='POST'>
    <input type="email" name="email" placeholder="Enter your email" required><br>
    <input type="password" name="password" placeholder"Enter password" required><br>
    <input type="submit" value="Register">
    </form>
    </body>
    </html>
    ''', 200
    # Login Endpoint
    @app.route('/login', methods=['POST'])
    def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
    access_token = create_access_token(identity=email)
    return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

    if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5003)

    for rule in app.url_map.iter_rules():
    print(f"Route: {rule} - Methods: {rule.methods}")
