### Hexlet tests and linter status:
[![Actions Status](https://github.com/Dzigr/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/Dzigr/python-project-83/actions)
[![CI](https://github.com/Dzigr/python-project-83/actions/workflows/CI.yml/badge.svg)](https://github.com/Dzigr/python-project-83/actions/workflows/CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/3848d214bf1f21ace841/maintainability)](https://codeclimate.com/github/Dzigr/python-project-83/maintainability)


### Project description
Page Analyzer is a simple web-application based on the Flask framework, where you can get simple web-site SEO suitability.  

<img src='https://github.com/Dzigr/Lessons/blob/main/Images/page_analyzer.png' width='600'>

[You may try demo here](https://page-analyzer-glto.onrender.com)


**Stack:**
* Python
* Flask
* Bootstrap
* PostgreSQL

### Local deployment
###### Note: Required Python, Poetry & PostgreSQL
1. Clone the repository
```comandline
git clone git@github.com:Dzigr/python-project-83 && cd python-project-83
```
2. Create PostgreSQL database with database.sql
```commandline
# create database
createdb {db name}

# create tables
psql {db name} < database.sql
```
3. Install dependencies
```commandline
poetry install
```
4. Rename `.env.template` file to `.env`  and filling in your data instead of templated.

5. Run application by `make dev` (dev) or `make start` for deploy (gunicorn)
