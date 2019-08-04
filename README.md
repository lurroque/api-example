# challenge

![version](https://img.shields.io/badge/challenge-1.0-brightgreen.svg)   ![license](https://img.shields.io/badge/license-MIT-green.svg)

## :house: [Homepage]()
api for register properties and real estates


## Installation
Install project dependencies:
pip install -r requirements/requirements.txt

create .env file at project root with the following environment variables:
FLASK_APP = app.py
FLASK_ENV = development

To run the server:
Flask run

To view introductory endpoint documentation, go to:
http://127.0.0.1:5000/apidocs/

You can create a mysql container with the following command:
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD = api -d -p 3306: 3306 mysql: 5

At this point it is important to model the database:

create database api;

use api;

create table property( id int not null auto_increment, name varchar(120) not null, address varchar(120) not null, description varchar(120) not null, status varchar(120) not null, features varchar(120) not null, type_of varchar(120) not null, purpose varchar(120) not null, real_estate int not null, primary key(id) );

create table real_estate( id int not null auto_increment, name varchar(120) not null, address varchar(120) not null );
    
    
## [License](LICENSE.md)
<details>
    <summary>MIT</summary>
MIT License

Copyright (c) 2019 Luiz Roque

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

</details>

## Author
Learn more about: Luiz Roque

Email: lrvroque@gmail.com

[Github :octocat:](https://github.com/)
[Twitter](https://twitter.com/)
