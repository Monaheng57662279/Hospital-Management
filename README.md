# Hospital-Management
Distrubuted Database Project
# Django Project with Docker

This project is a Django web application set up with Docker. It includes a PostgreSQL database, Redis, and other necessary services.

## Prerequisites

- Docker
- Docker Compose

## Project Setup

### Clone the Repository

git clone https://github.com/yourusername/yourproject.git
cd yourproject

##install virtual enviroment
python3 -m virtualenv venv

Create and Activate a Virtual Environment

    Install Virtualenv:

    sh

python3 -m pip install --user virtualenv

Create a Virtual Environment:

sh

python3 -m virtualenv venv

Activate the Virtual Environment:

    On Linux/macOS:

    sh

source venv/bin/activate

On Windows:

sh

        .\venv\Scripts\activate

Install Dependencies

sh

pip install -r requirements.txt

Environment Variables

Create a .env file in the project root and add your environment variables. Example:

dotenv

DEBUG=1
SECRET_KEY=your_secret_key
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=db
DATABASE_PORT=5432
REDIS_URL=redis://redis:6379/0

Docker Setup

Build and run the Docker containers:

sh

docker-compose up --build

Running Migrations

After the containers are up, run the database migrations:

sh

docker-compose exec web python manage.py migrate

Create a Superuser

Create a superuser to access the Django admin:

sh

docker-compose exec web python manage.py createsuperuser

Accessing the Application

The application should now be running at http://localhost:8000.
Stopping the Containers

To stop the containers, run:

sh

docker-compose down

Development

For development, you can run the Django server directly on your local machine:

    Activate the Virtual Environment:

    sh

source venv/bin/activate  # or .\venv\Scripts\activate on Windows

Run the Development Server:

sh

    python manage.py runserver

Testing

To run tests, use the following command:

sh

docker-compose exec web python manage.py test

License

This project is licensed under the MIT License.

mathematica


### Download and Set Up Virtual Environment

1. **Install `virtualenv` if not already installed**:

   ```sh
   python3 -m pip install --user virtualenv

    Create a Virtual Environment:

    sh

python3 -m virtualenv venv

Activate the Virtual Environment:

    On Linux/macOS:

    sh

source venv/bin/activate

On Windows:

sh

    .\venv\Scripts\activate

Install Project Dependencies:

sh

pip install -r requirements.txt
