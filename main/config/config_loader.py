from dotenv import load_dotenv
import os
from pathlib import Path

def load_env_config():
    """
    Loads environment configuration variables from a .env file located
    in the root directory of the project (three levels up from this file).

    Returns:
        dict: A dictionary containing environment variables such as database
              configuration and Flask debug settings.
              
              Keys:
                - 'DB_NAME' (str or None): Database name
                - 'DB_USER' (str or None): Database username
                - 'DB_PASSWORD' (str or None): Database password
                - 'DB_HOST' (str): Database host, defaults to 'localhost'
                - 'DB_PORT' (int): Database port, defaults to 5432
                - 'FLASK_DEBUG' (str): Flask debug flag, defaults to 'True'
    """
    # Path to the .env file in the root directory of the project
    env_path = Path(__file__).resolve().parents[2] / ".env"
    load_dotenv(dotenv_path=env_path)

    return {
        "DB_NAME": os.getenv("DB_NAME"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD"),
        "DB_HOST": os.getenv("DB_HOST", "localhost"),
        "DB_PORT": int(os.getenv("DB_PORT", 5432)),
        "FLASK_DEBUG": os.getenv("FLASK_DEBUG", "True"),
    }
