@echo off
echo === Iniciando ambient virtual===
call env\Scripts\activate

streamlit run main.py

echo === Abrindo main.py ===
pause