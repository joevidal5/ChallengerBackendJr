# ChallengerBackendJr
Challenger Backend Jr - Emprinet

# Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL

# Installation
1. Clone this repository to your local machine.

- git clone https://github.com/joevidal5/ChallengerBackendJr.git

2. Create a virtual environment:

- virtualenv name_evn

3. Activate the virtual environment:

- source env/bin/activate

4. Install the required dependencies:

- pip install -r requirements.txt

5. Create a .env file and set the database URI as DATABASE_URI and an SECRET_KEY:

- DATABASE_URI=postgresql://username:password@localhost/database_name
- SECRET_KEY=secret_key

6. Initialize Flask-Migrate:

- flask db init

7. Create the initial migration:

- flask db migrate

8. Upgrade the database schema:

- flask db upgrade

9. go into the app folder

- cd src

10. Start the application:

- flask run

11. Open the application in your browser at http://localhost:5000.


# Usage
Once the application is running, you can creat and view posts. The following routes are available:

- / - Home page
- /posts - List all posts
- /add - Create a new posts
- /post/<int:post_id> - Show a single posts