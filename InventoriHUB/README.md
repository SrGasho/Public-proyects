# InventoryHub

InventoryHub is a RESTful API built with FastAPI, PostgreSQL, and Docker, designed to manage product inventory, categories, and movement logs. It serves as a backend foundation for warehouse and stock control systems.

## Technologies

- Python 3.11+
- FastAPI
- PostgreSQL
- Docker & Docker Compose
- SQLAlchemy (ORM)
- Pydantic v2

## Project Structure

```
inventoryhub/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── config.py            # General configuration
│   ├── database.py          # SQLAlchemy database connection
│   ├── init_db.py           # Table initialization script
│   ├── models/              # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic schemas for data validation
│   ├── crud/                # CRUD logic for each model
│   ├── routes/              # API routes grouped by resource
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/inventoryhub.git
cd inventoryhub
```

### 2. Build and run the application using Docker

```bash
docker-compose up --build
```

This will start:

- FastAPI on http://localhost:8000
- PostgreSQL on port 5432

## API Endpoints

### Products (/products)

- GET /products: Retrieve all products
- GET /products/{id}: Retrieve a single product
- POST /products: Create a new product (category is required)
- PUT /products/{id}: Update a product
- DELETE /products/{id}: Delete a product

A movement record is automatically created when a product is created, updated, or deleted.

### Categories (/categories)

- GET /categories: List all categories
- GET /categories/{id}: Retrieve a category
- POST /categories: Create a new category
- PUT /categories/{id}: Update a category
- DELETE /categories/{id}: Delete a category (only if no products are assigned)

### Inventory Movements (/movements)

- GET /movements: List all inventory movements
- POST /movements: Create a manual movement (under development or internal use only)

## Security

This project does not include authentication or authorization yet. It is intended for development and learning purposes. In future versions, authentication can be integrated using:

- JWT with OAuth2
- User roles and permissions
- Route protection

## License

MIT License © 2025 - [SrGasho](https://github.com/your-username)

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests to improve the project.