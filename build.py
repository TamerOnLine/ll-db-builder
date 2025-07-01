import os
from main.config import config_loader, db_initializer, settings
from main.extensions import db
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

print("🔧 Initializing the database...")

# Load database configuration
engine = create_engine(settings.Config.SQLALCHEMY_DATABASE_URI)
db_initializer.create_all_tables(engine)

print("✅ All tables created successfully.")