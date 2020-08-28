# itsTiny

**A simple URL shrinker in Flask and Postgresql**

### [Demo](https://itstiny.herokuapp.com): https://itstiny.herokuapp.com

## Features

* Shortens any valid URL
* Stores the URL and Code pair in database to avoid repeating process
* Displays click count
* Admin panel for editing and adding custom parameters

Made with:

 - Flask
 - PostgreSQL

To run this;
 
  - Clone the repo
  
	`git clone https://github.com/anorebel/itsTiny.git`
 
  - Enter the directory
  
	  `cd itsTiny`
 
  - Create environment and install dependencies
  
	  `pipenv install`

  - Rename `.env.example` to `.env` and add your postgres connection string

  - Initialize database and run:
 	- In development:
	 	`bash
	 	 export FLASK_ENV=development
	 	 export FLASK_APP=app
	 	 flask db upgrade
	 	 flask run`
	 	
	 - In production:
	 	`bash
	 	 export FLASK_APP=app
	 	 flask db upgrade
	 	 flask run`

  - Run create_admin.py and follow prompts to create admin user then visit <address>/admin

  		`python
  		 python3 create_admin.py`
