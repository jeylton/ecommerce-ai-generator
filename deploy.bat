@echo off
echo 🚀 Déploiement E-commerce AI Generator
echo ======================================

echo 📦 Étape 1 : Vérification des prérequis...
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Git n'est pas installé. Installe Git depuis https://git-scm.com/
    pause
    exit /b 1
)

echo ✅ Git trouvé

echo.
echo 🔧 Étape 2 : Initialisation du repo Git...
if not exist .git (
    git init
    git add .
    git commit -m "Initial commit: E-commerce AI generator with DeepSeek"
    echo ✅ Repository Git initialisé
) else (
    echo ✅ Repository Git déjà initialisé
)

echo.
echo 🌐 Étape 3 : Déploiement Frontend sur Vercel...
cd frontend
call npm install
call npm run build

echo Installation de Vercel CLI...
call npm install -g vercel

echo Déploiement sur Vercel...
call vercel --prod --yes

echo.
echo 🔙 Retour au dossier principal...
cd ..

echo.
echo 🎯 Prochaines étapes manuelles :
echo ================================
echo 1. Backend Render :
echo    - Aller sur https://render.com
echo    - Connecter ce repo GitHub
echo    - Déployer le dossier 'backend'
echo    - Noter l'URL générée
echo.
echo 2. Configuration Vercel :
echo    - Dans Vercel dashboard, ajouter variable :
echo      VITE_API_URL=https://votre-backend.onrender.com
echo.
echo 3. ⚠️ LIMITATION IMPORTANTE :
echo    DeepSeek (Ollama) ne fonctionne que LOCALEMENT
echo    Pour production, utiliser API cloud alternative
echo.
echo ✅ Déploiement terminé !
pause