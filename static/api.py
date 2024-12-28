from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Replace with your Firebase credentials (service account key JSON)
cred = credentials.Certificate("database_credentials.json") #replace with your credentials file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aether-c4b42-default-rtdb.europe-west1.firebasedatabase.app/' # Replace with your firebase project URL
})

@app.route('/message', methods=['POST'])
def receive_message_from_aether():
    try:
        data = request.get_json()
        print(f"Received Data: {data}")
        return jsonify({"status":"ok","message":"data received"})
    except Exception as e:
        return jsonify({"status":"error","message":str(e)})

@app.route('/new_bid', methods=['POST'])
def receive_new_bid():
  try:
    bid_data = request.get_json()
    print(f"Received bid: {bid_data}")
    ref = db.reference('bids', app=firebase_admin.get_app())
    ref.push(bid_data)
    return jsonify({"status":"ok","message":"bid stored"})
  except Exception as e:
     print(f"Error creating database entry {e}")
     return jsonify({"status":"error","message":str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)