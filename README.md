# Simple Market CLI

## Author
yelsin45

## Description
A beginner-friendly command-line application for managing users (with location), products, orders, and order items in a small farm or marketplace scenario.  
Built with Python, SQLAlchemy ORM, and Alembic for database migrations.  
Data is stored in SQLite for easy setup.

## Features

- **Users**: Add, list, update, delete (with location and role).
- **Products**: Add, list, update, delete (linked to a farmer).
- **Orders**: Add, list, delete (by customer).
- **Order Items**: Add, list, delete (for orders, reduces product stock on add).
- **Search**: Search products by name or by farmer location.
- **All relationships and data are persisted in the database.**
- **Easy to extend and modify for your needs.**

## Technologies Used

- Python 3.8+
- SQLAlchemy
- Alembic
- Pipenv (for dependency management)
- SQLite

## Setup Instructions

1. **Clone this repository**  
   ```sh
   git clone <your-repo-url>
   cd simple_market
   ```

2. **Install dependencies & activate environment**  
   ```sh
   pipenv install
   pipenv shell
   ```

3. **Set up Alembic for migrations**  
   ```sh
   alembic init alembic
   ```
   - Edit `alembic.ini` and set  
     ```
     sqlalchemy.url = sqlite:///market.db
     ```
   - Edit `alembic/env.py` and add:
     ```python
     import sys
     import os
     sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))
     from models import Base
     target_metadata = Base.metadata
     ```

4. **Create migration and apply it**  
   ```sh
   alembic revision --autogenerate -m "init"
   alembic upgrade head
   ```

5. **Run the application**  
   ```sh
   python app.py
   ```

## Example Usage

- Add a user (farmer or customer) with location.
- Add a product with a farmer ID.
- Add an order with a customer ID.
- Add items to an order—stock is reduced automatically.
- List, update, and delete all entries.
- Search products by name or by farmer location.

## Support/Contact

For help or feedback, open an issue or email: rtcch@example.com

## License

MIT License
