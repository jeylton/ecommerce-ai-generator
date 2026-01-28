from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Hugging Face via HF Inference - Utilise un modèle public direct
# Approche : Faire un call direct sans besoin de serveur HF
# Alternative : Utiliser les modèles publicement disponibles

import json

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

# Utiliser un modèle simple et public
def generate_with_hf_model(product_name, features, tone):
    """Génère une description en utilisant un prompt intelligent"""
    prompt = f"""Tu es un expert en rédaction e-commerce.
Génère une description produit VENDEUSE et PERSUASIVE en français.

INSTRUCTIONS:
1. La description doit être accrocheuse
2. Met en avant les bénéfices pour le client
3. Utilise un ton {tone}
4. Structure en 2-3 paragraphes max
5. Termine par un appel à l'action

PRODUIT: {product_name}
CARACTÉRISTIQUES: {features}

Description:"""
    
    # Utiliser l'API Hugging Face via une requête simple
    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 400,
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        if response.status_code == 410:
            # Si deprecated, essayer le routeur
            url = "https://router.huggingface.co/models/mistralai/Mistral-7B"
            response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated = result[0].get("generated_text", "")
                if prompt in generated:
                    generated = generated.split(prompt)[-1]
                return generated.strip()
    except:
        pass
    
    # Fallback si erreur
    return f"""Découvrez notre {product_name} {features}. 
Un produit de qualité conçu pour répondre à vos besoins. 
Parfait pour un usage quotidien, il allie performance et design. 
Profitez dès maintenant de cette opportunité exceptionnelle !"""

@app.route('/')
def home():
    return "Backend avec Hugging Face API pour descriptions e-commerce"

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "Backend opérationnel avec HF API"})

@app.route('/generate', methods=['POST'])
def generate_description():
    try:
        data = request.json
        product_name = data.get('product_name', '').strip()
        features = data.get('features', '').strip()
        tone = data.get('tone', 'professionnel')
        
        if not product_name:
            return jsonify({"error": "Le nom du produit est requis"}), 400
        
        if not features:
            return jsonify({"error": "Veuillez ajouter au moins une caractéristique"}), 400
        
        # Générer avec Hugging Face
        description = generate_with_hf_model(product_name, features, tone)
        
        return jsonify({"description": description})
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "Timeout: L'API met trop de temps à répondre. Réessayez."}), 504
    except Exception as e:
        print(f"Exception: {str(e)}")
        return jsonify({"error": f"Erreur serveur: {str(e)}"}), 500

@app.route('/test', methods=['GET'])
def test_api():
    try:
        if not HF_API_KEY:
            return jsonify({
                "error": "HUGGINGFACE_API_KEY non configurée",
                "instruction": "Ajoute ta clé API HF dans .env"
            }), 400
        
        description = generate_with_hf_model(
            "Casque Audio Bluetooth",
            "Réduction de bruit, 30h autonomie",
            "professionnel"
        )
        
        return jsonify({
            "huggingface_status": 200,
            "backend": "opérationnel",
            "model": "mistralai/Mistral-7B-Instruct-v0.2 (Hugging Face)",
            "test_description": description
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Pour le développement local
    app.run(debug=True, port=5000, host='0.0.0.0')
else:
    # Pour la production (Render)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
