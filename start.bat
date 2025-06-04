@echo off
echo === Iniciando ambient virtual===
call env\Scripts\activate

streamlit run app.py

echo === Abrindo app.py ===
pause