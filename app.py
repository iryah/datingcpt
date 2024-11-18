from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Veritabanı bağlantısı için URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Profil tablosu modeli
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Veritabanını başlatmak için
with app.app_context():
    db.create_all()

@app.route('/profile', methods=['POST'])
def create_profile():
    data = request.json
    if not data.get("name") or not data.get("age"):
        return jsonify({"error": "Name and age are required!"}), 400
    
    profile = Profile(name=data['name'], age=data['age'])
    db.session.add(profile)
    db.session.commit()
    return jsonify({"message": "Profile created!", "profile": {"id": profile.id, "name": profile.name, "age": profile.age}}), 201

@app.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    profiles_list = [{"id": profile.id, "name": profile.name, "age": profile.age} for profile in profiles]
    return jsonify({"profiles": profiles_list}), 200

if __name__ == '__main__':
    app.run(debug=True)
