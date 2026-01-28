# ⚠️ LIMITATIONS DU DÉPLOIEMENT

## 🚫 Problème : DeepSeek Local ≠ Production Cloud

**DeepSeek via Ollama fonctionne uniquement en local.** Les services cloud comme Render/Vercel n'ont pas accès à Ollama sur votre PC.

### Solutions Alternatives :

## 🟢 Option 1 : API Cloud (RECOMMANDÉ)

Remplacer Ollama par une API cloud dans `backend/app.py` :

```python
# Au lieu d'Ollama local
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Utiliser Together AI (gratuit)
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")
```

**Avantages :**
- ✅ Fonctionne en production
- ✅ Pas de téléchargement requis
- ✅ Crédits gratuits disponibles

**Inconvénients :**
- ❌ Coûts après les crédits gratuits
- ❌ Dépendance à un service tiers

## 🟡 Option 2 : Backend Local + Frontend Cloud

- **Frontend** : Vercel (gratuit)
- **Backend** : Garde-le tourner sur ton PC
- **Communication** : Frontend contacte `localhost:5000`

**Avantages :**
- ✅ DeepSeek 100% local et gratuit
- ✅ Pas de coûts
- ✅ Contrôle total

**Inconvénients :**
- ❌ Backend doit toujours tourner
- ❌ Pas accessible depuis d'autres appareils

## 🔴 Option 3 : VPS Personnalisé

Louer un VPS (DigitalOcean, Linode) et installer Ollama dessus.

**Avantages :**
- ✅ DeepSeek en "production"
- ✅ Accessible partout

**Inconvénients :**
- 💰 Coûts mensuels (~5-10€)
- 🔧 Configuration serveur requise

---

## 🎯 RECOMMANDATION

Pour ton projet scolaire, utilise **l'Option 1 (API Cloud)** :
1. Crée un compte gratuit sur https://www.together.ai/
2. Obtiens ta clé API
3. Modifie `backend/app.py` pour utiliser Together AI
4. Déploie normalement

**C'est simple, gratuit pour commencer, et fonctionne parfaitement !** 🚀