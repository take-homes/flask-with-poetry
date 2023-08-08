# Overview

This is a demo problem for a Python backend API server using Flask.

# Installing dependencies with Poetry

First open the **Task Manager** by clicking on the following button:

<img src="https://static.takehomes.com/flask-demo/task_manager.png" width="247" height="323" />

Next, hover your mouse over the **poetry install** task and click on the green **Run Task** button that appears on the right.

<img src="https://static.takehomes.com/flask-demo/poetry_install.png" width="281" height="181" />

When the packages are done installing, you can close the terminal tab.

# Initializing the SQLite database

Hover your mouse over the **run db init** task and click on the green **Run Task** button that appears on the right.

<img src="https://static.takehomes.com/flask-demo/init_db.png" width="286" height="173" />

# Run the Flask server

Hover your mouse over the **run flask app** task and click on the green **Run Task** button that appears on the right.

<img src="https://static.takehomes.com/flask-demo/run_flask_app.png" width="328" height="174" />

A toast message will pop up on the bottom right asking if you want to enable remote connections to the local virtual machine. Click **yes** to continue.

<img src="https://static.takehomes.com/flask-demo/remote_port.png" width="466" height="165" />

Another toast message will pop up confirming that the redirect has occurred and gives you the domain name for the proxy. Click **Open in New Tab** to continue.

<img src="https://static.takehomes.com/flask-demo/redirect.png" width="461" height="143" />

Finally you get a security popup asking you if you want to open to an external website. Click **Open** to continue.

<img src="https://static.takehomes.com/flask-demo/open_tab.png" width="530" height="207" />

A new browser tab will have opened and you will see the backend respond with `[]`.

# Querying the Flask API server

On your local computer, you can use any tool you are comfortable with to interact with the backend including `curl`, [Postman](https://www.postman.com/), or [Insomnia](https://insomnia.rest/).

# Connecting to the SQLite database

Next, hover your mouse over the **sqlite shell** task and click on the green **Run Task** button that appears on the right.

<img src="https://static.takehomes.com/flask-demo/sqlite_shell.png" width="330" height="184" />

You can now issue queries to the SQLite database.
