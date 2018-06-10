# A Quick Template for Flask Apps

This is my personal template for creating flask applications that require user authentication.  It draws heavily from Miguel Greenberg's incredible [Flask Mega Tutorial](https://learn.miguelgrinberg.com/) and uses [Bootstrap.js](https://getbootstrap.com/docs/3.3/getting-started/#template) for a nice responsive design.

This template is available for you to use, but comes with no guarantee or warranty.  Use at your own risk.

# Getting up and Running

    virtualenv env
    source ./env/bin/activate
    pip install -r requirements.txt
    export FLASK_APP=apprunner.py
    flask db init
    flask db migrate -m "Initial database build"
    flask db upgrade
    flask run

# Deploying to Azure

* Follow these deploy to [Azure for Python](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-python) instructions through your first push to Azure.
  * Create an App Service Plan, Service, and Resource Group to hold the services.
  * Create a deployment user.
  * Add azure as a remote repository.
* Configure the [App Service for Python](https://docs.microsoft.com/en-us/visualstudio/python/managing-python-on-azure-app-service)
  * Add the Python 3.6 extension.
  * Ensure that the web.config file reflects the location of your installed extension.
  * On the kudu console, cd into the folder containing the python installed by the extension.
  * python -m pip install -r requirements.txt while in that folder.
* OPTIONAL: Create an Azure SQL DB Server and Database
  * [Quick Start](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-get-started-portal)
  * Create an [application user](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-2017) and grant them [permissions](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/getting-started-with-database-engine-permissions?view=sql-server-2017#permission-hierarchy).
* MISCELLANEOUS Checklist
  * Add the environment variables to web.config.
  * Create any additional folders on the kudu console.

# Working with VS Code and Flask Apps

* Setting an environment variable.
  * Powershell: $(env:MyVariable)=SomeValue
  * CMD: set MyVariable=SomeValue
  * Linux: export MyVariable=SomeValue
* Viewing an environment variable
  * Powershell:  Get-ChildItem Env:MyVariable
  * CMD: echo %MyVariable%
  * Linux: echo $MyVariable