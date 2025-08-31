Installation
1. Create ``.venv`` in root project

    ```python -m venv .venv```
2. Install Requirement Library

    ``` pip install -r requirements.txt ```

3. Create Database In MongoDB and config dbname in slider/settings.py in line ``18``

    ``mongoengine.connect(db="db_python", alias='default')``