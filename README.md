## OSSCAMEROON PHARMACIES
This project is an [osscameroon](https://osscameroon.com) initiative. Using appropriate technologies, we provide all the 
pharmacies on the Cameroon national territory.
## Features
* [Open Source](https://osscameroon.com/osscameroon/osscameroon.html)
* Promotes health and well-being of the Cameroonian citizens by providing the nearest pharmacies and health care services.

## Description
The **OSSCAMEROON PHARMACIES** is a web application that provides the nearest pharmacies and health care services in Cameroon.
Using [scraping](https://en.wikipedia.org/wiki/Web_scraping) techniques, we collect the data from the [Google Maps](https://www.google.com/maps) website.
- The backend being a [Python](https://www.python.org/) web application, we use [Flask](https://flask.palletsprojects.com/) to create the web application.
- A [sqlite3](https://docs.python.org/3/library/sqlite3.html) database is used to store the data.
- In addition to that a
frontend built with [React](https://reactjs.org/) and [TypeScript](https://www.typescriptlang.org/) is used to display the data.


To contribute, some bunch of steps has to be included. Follow me in this small tutorial.

## Contribution

- [Fork](https://github.com/osscameroon/pharmacies/fork) the project from [here](https://github.com/osscameroon/pharmacies/fork).
- Clone the repository as follows:
    
    ```bash
    git clone https://github.com/<username>/pharmacies.git
    ```
- [Create a new branch](https://help.github.com/articles/creating-a-new-branch/) for different or several PRs.

    ```bash
    git checkout -b <branch-name>
    ```
  
- [Commit and push](https://help.github.com/articles/using-git-commands/) your changes.


- Running backend server
    ```bash
    cd backend
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python server.py
    ```
- Running the frontend
    ```bash
    yarn install
    yarn start
    ```
- Running scraper
    ```bash
    cd scraper
    python scraper.py
    ```
  Results will be available in the scraper folder in the file called `./backend/scraper/pharmacies.csv`.

## Contributors

- [Boris Mbarga](https://github.com/elhmn)
- [Steve Yonkeu](https://github.com/yokwejuste) 

This project is opensource under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
