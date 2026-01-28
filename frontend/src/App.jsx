import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [productName, setProductName] = useState('');
  const [features, setFeatures] = useState('');
  const [tone, setTone] = useState('professionnel');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

  const generateDescription = async () => {
    if (!productName.trim()) {
      setError('Veuillez entrer un nom de produit');
      return;
    }

    if (!features.trim()) {
      setError('Veuillez ajouter au moins une caractéristique du produit');
      return;
    }

    setLoading(true);
    setError('');
    setDescription('');

    try {
      const response = await axios.post(`${API_URL}/generate`, {
        product_name: productName,
        features: features,
        tone: tone
      });

      setDescription(response.data.description);
    } catch (err) {
      console.log('Erreur complète:', err);
      setError(err.response?.data?.error || 'Erreur lors de la génération. Vérifie que le backend tourne sur localhost:5000');
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(description);
    alert('Description copiée !');
  };

  return (
    <div className="app">
      <header className="header">
        <h1>🛍️ Générateur de Descriptions Produits E-commerce</h1>
        <p>Créez des descriptions captivantes en quelques secondes avec l'IA</p>
      </header>

      <div className="container">
        <div className="form-section">
          <h2>📝 Informations du produit</h2>
          
          <div className="input-group">
            <label>Nom du produit *</label>
            <input
              type="text"
              value={productName}
              onChange={(e) => setProductName(e.target.value)}
              placeholder="Ex: Casque Audio Sans Fil Premium"
            />
          </div>

          <div className="input-group">
            <label>Caractéristiques</label>
            <textarea
              value={features}
              onChange={(e) => setFeatures(e.target.value)}
              placeholder="Ex: Réduction de bruit active, autonomie 30h, Bluetooth 5.3, écouteurs pliables"
              rows="3"
            />
          </div>

          <div className="input-group">
            <label>Ton de la description</label>
            <div className="tone-buttons">
              {['professionnel', 'amical', 'enthousiaste', 'luxe', 'technique'].map((t) => (
                <button
                  key={t}
                  onClick={() => setTone(t)}
                  className={tone === t ? 'active' : ''}
                >
                  {t}
                </button>
              ))}
            </div>
          </div>

          <button 
            onClick={generateDescription} 
            disabled={loading || !productName.trim()}
            className="generate-btn"
          >
            {loading ? '⏳ Génération en cours...' : '✨ Générer la description'}
          </button>
        </div>

        {error && (
          <div className="error">
            ⚠️ {error}
          </div>
        )}

        {description && (
          <div className="result-section">
            <div className="result-header">
              <h2>📄 Description générée</h2>
              <button onClick={handleCopy} className="copy-btn">
                📋 Copier
              </button>
            </div>
            
            <div className="description-box">
              {description}
            </div>

            <div className="preview">
              <h3>🎯 Aperçu produit</h3>
              <div className="preview-card">
                <div className="preview-image">
                  [Image du produit]
                </div>
                <div className="preview-content">
                  <h4>{productName}</h4>
                  <p>{description.substring(0, 150)}...</p>
                  <div className="preview-footer">
                    <span className="price">€99.99</span>
                    <button className="cart-btn">🛒 Ajouter au panier</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      <footer>
        <p>🚀 Propulsé par Mistral AI • Backend Flask • Frontend React</p>
        <p className="note">⚠️ Ceci est une démo éducative</p>
      </footer>
    </div>
  );
}

export default App;