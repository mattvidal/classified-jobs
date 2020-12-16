## Classified Jobs

This project has as main objective to improve my knowledge in API Rest using Django Rest Framework. 

The application aims to store job openings, registration of employers, candidates, in addition to storing a mini resume and eventual job application.


## Requirements

* Python 3.8.6
* Pip 20.2.1
* SQLite3


## Setup process

### Installing dependencies

We use the command below to create our virtual environment `env`:

```bash
python -m venv env
```

And then we use this one to install our dependencies from `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Finally we use the commands listed below to migrate our data to `SQLite3` database:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

This Compose file contains the following environment variables:

* POSTGRES_USER the default value is **postgres**
* POSTGRES_PASSWORD the default value is **changeme**
* PGADMIN_PORT the default value is **5050**
* PGADMIN_DEFAULT_EMAIL the default value is **pgadmin4@pgadmin.org**
* PGADMIN_DEFAULT_PASSWORD the default value is **admin**

You can replace those variables as you wish.

### Access to postgres: 
* `localhost:5432`
* **Username:** postgres (as a default)
* **Password:** changeme (as a default)

### Access to PgAdmin: 
* **URL:** `http://localhost:5050`
* **Username:** pgadmin4@pgadmin.org (as a default)
* **Password:** admin (as a default)

### Add a new server in PgAdmin:
* **Host name/address** `postgres`
* **Port** `5432`
* **Username** as `POSTGRES_USER`, by default: `postgres`
* **Password** as `POSTGRES_PASSWORD`, by default `changeme`

## Licence

MIT License

Copyright (c) 2020 Matheus Vidal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.