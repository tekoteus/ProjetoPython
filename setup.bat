@echo off
echo === Criando ambiente virtual ===
python -m venv env

echo === Ativando ambiente virtual ===
call env\Scripts\activate

echo === Instalando dependências ===
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo === Ambiente configurado com sucesso! ===
pause
