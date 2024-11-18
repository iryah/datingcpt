from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Kullanıcı profili için global bir liste
profiles = []

# Kullanıcı profili oluşturma endpoint'i
@app.route('/profile', methods=['POST'])
def create_profile():
    data = request.json
    profiles.append(data)
    return jsonify({"message": "Profile created!", "profile": data}), 201

# Tüm profilleri listeleme endpoint'i
@app.route('/profiles', methods=['GET'])
def get_profiles():
    return jsonify({"profiles": profiles}), 200

# Flask uygulamasını çalıştırma
if __name__ == '__main__':
    app.run()
