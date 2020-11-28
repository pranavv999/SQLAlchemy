psql < create.sql
python3 schema.py
python3 main.py
python3 json_generator.py
xdg-open http://localhost:8000