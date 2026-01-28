@echo off
echo 🔄 Basculement vers API Cloud (Together AI)
echo ===========================================

echo Modification du backend pour utiliser Together AI...
echo.

echo 📝 Instructions :
echo ================
echo 1. Crée un compte gratuit sur https://www.together.ai/
echo 2. Obtiens ta clé API dans Settings → API Keys
echo 3. Modifie backend/.env :
echo    TOGETHER_API_KEY=ta_clé_api_ici
echo.
echo 4. Le backend utilisera automatiquement l'API cloud
echo    au lieu d'Ollama local
echo.
echo ✅ Prêt pour le déploiement sur Render !
echo.
pause