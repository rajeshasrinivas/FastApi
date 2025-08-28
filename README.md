# FastApi



1. Create the Virtual Environment
~~~
   python -m venv my_evn
~~~
3. Activate the Virtual Environment:

On Windows (PowerShell).

    my_env\Scripts\Activate.ps1

On macOS/Linux (Bash/Zsh)

    source my_env/bin/activate

3. To deactivate the virtual environment, simply type:
   
    deactivate


Install FastApi

    pip install fastapi unicorn pydantic

Run FastAPI

    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
