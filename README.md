# 🛍️ Générateur de Descriptions E-commerce avec DeepSeek AI

Application web pour générer automatiquement des descriptions de produits e-commerce optimisées pour la vente, utilisant l'IA DeepSeek-R1.

## 🚀 Fonctionnalités

- **Interface intuitive** : Formulaire simple pour saisir nom du produit et caractéristiques
- **IA DeepSeek** : Génération de descriptions vendeuses et persuasives
- **Choix de ton** : Professionnel, créatif, ou décontracté
- **Copie facile** : Bouton pour copier la description générée

## 🛠️ Technologies

- **Frontend** : React + Vite
- **Backend** : Flask (Python)
- **IA** : DeepSeek-R1 via Ollama (local) ou API cloud

## 📦 Installation & Développement Local

### Prérequis
- Node.js 20.19+ ou 22.12+
- Python 3.9+
- Ollama installé

### Installation

1. **Cloner le repo**
```bash
git clone <url-du-repo>
cd ecommerce-ai-generator
```

2. **Backend**
```bash
cd backend
pip install -r requirements.txt
```

3. **Frontend**
```bash
cd frontend
npm install
```

4. **IA (DeepSeek)**
```bash
# Télécharger et installer Ollama : https://ollama.ai
ollama pull deepseek-r1:1.5b
ollama serve
```

5. **Lancer l'application**
```bash
# Terminal 1 - Backend
cd backend && python app.py

# Terminal 2 - Frontend
cd frontend && npm run dev
```

6. **Accéder** : http://localhost:5173

## 🚀 Déploiement

### Frontend (Vercel - GRATUIT)

1. **Installer Vercel CLI**
```bash
npm install -g vercel
```

2. **Déployer**
```bash
cd frontend
vercel --prod
```

3. **Configuration** : Ajouter variable d'environnement `VITE_API_URL` avec l'URL du backend Render

### Backend (Render - GRATUIT)

⚠️ **Limitation** : DeepSeek via Ollama ne fonctionne que localement. Pour la production, utiliser une API cloud alternative.

1. **Créer un compte** sur https://render.com
2. **Connecter GitHub** et déployer depuis ce repo
3. **Configuration** :
   - Runtime : Python 3
   - Build Command : `pip install -r requirements.txt`
   - Start Command : `gunicorn app:app`

## 🔧 Configuration

### Variables d'environnement (.env)

**Backend :**
```
# Pour développement local avec Ollama
# (rien à configurer)

# Pour production avec API cloud (optionnel)
TOGETHER_API_KEY=votre_clé_api
```

**Frontend :**
```
VITE_API_URL=https://votre-backend-render.onrender.com
```

## 📝 Utilisation

1. Saisir le nom du produit
2. Ajouter les caractéristiques principales
3. Choisir le ton souhaité
4. Cliquer sur "Générer la description"
5. Copier et utiliser dans votre boutique e-commerce

## 🤝 Contribution

N'hésitez pas à contribuer en ouvrant des issues ou des pull requests !

## 📄 Licence

MIT License - voir le fichier LICENSE pour plus de détails.