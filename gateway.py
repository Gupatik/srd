# ----------------------------
# Flask Gateway
# ----------------------------
# 1. Receives HTTP request from ESP32
# 2. Forwards it to gRPC 
# 3. Returns simple True/False

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/uid', methods=['POST', 'OPTIONS'])  # Add OPTIONS method

def receive_uid():
    if request.method == 'OPTIONS':
        return '', 200  # Handle preflight requests
    
    data = request.get_json()
    if not data or 'uid' not in data:
        return "False", 400

    uid = data['uid']
    print(f"[GATEWAY] UID received: {uid}")

    #
    # La seul partie a changer: DEBUT
    #

    # Appeler les fonction de communication du serveur ici:
    #
    # grpc_response = grpc_stub.authentifier_carte(uid)  # <- comunication avec serveur depuis ici
    # access_granted = grpc_response.is_authorized

    access_granted = uid == "123456"  # Simplified check a changer la valeur par la reponse du serveur

    #
    # La seul partie a changer: FIN
    #

    return str(access_granted), 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
