from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/character', methods=['POST'])
def get_character():
    data = request.get_json()

    if 'character_id' not in data:
        return jsonify({"error": "No 'character_id' provided"}), 400

    character_id = data['character_id']
    url = f"https://rickandmortyapi.com/api/character/{character_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Esto lanza una excepción si hay un error HTTP
        
        character_data = response.json()
        return jsonify({
            "name": character_data['name'],
            "status": character_data['status']
        }), 200

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return jsonify({"error": "Personaje no encontrado"}), 404
        return jsonify({"error": "Error al conseguir la información del personaje", "details": str(err)}), response.status_code

    except Exception as e:
        return jsonify({"error": "Ha ocurrido un error inesperado", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)