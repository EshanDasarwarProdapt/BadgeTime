To create Virtual Environment
python -m venv venv

To activate 
venv\scripts\activate

TO install
pip install -r requirements.txt

To check list
pip list

To deactivate
deactivate 

To start the server of FASTAPI
uvicorn app.main:app --reload