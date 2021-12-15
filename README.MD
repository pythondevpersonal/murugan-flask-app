# Flask Employee Crud

`Employee Crud` contains a working example of a Flask project with features:
 
- Employee CRUD options 

### Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/pythondevpersonal/murugan-flask-app.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`cd murugan-flask-app`**
    * **`pip install virtualenv`**
    * **`virtualenv env`**
    * **`env/bin/activate` or `env/Scripts/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**

### Database setup
    open python shell and make sure you are running on enviroment

    Run the following commands respectively:

    * **` set FLASK_APP=run.py`**
    * **` set FLASK_ENV=development`**
    * **` $env:FLASK_APP = "run.py"`**
    * **` flask db upgrade`**
    * On the same file write down the command **`flask run`** 

Open http://127.0.0.1:5000/, customize project files and **have fun**.
