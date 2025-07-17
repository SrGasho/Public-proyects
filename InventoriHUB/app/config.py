import os

# prefer put all this in a .env file
# and use python-dotenv to load it
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/inventoryhub"
)
