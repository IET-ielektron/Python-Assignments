Note:
1. The project gives flexibility to work with custom and ORM
2. Single project structure.(CUSTOM)
3. Details is in separate folders
4. Project is deployed to heroku environment 
5. database use is postgresql(heroku deployed) for custom
6. find the software versions in requirements.txt file
7. find the python version in runtime.txt file
8. IDE use is pycharm

Steps to setup project in local:
1. find mainsource.zip file inside the Source code folder
2. Unzip to a new folder ex: "interview"
3. run some commands after that
  cd interview
4. create an environment and name it as int-env
  py -m venv int-env
5. activate the environment
  .\int-env\Scripts\activate
6. cd mainsource\emp_mgr
7. run requirements.txt file to install the libraries and packages
  pip install -r requirements.txt
8. use postman to test the links

Postman links:
1. open postman
2. import collection
3. click on send 
4. verify the output for json