### Running web application

In terminal, navigate to the project root folder, in this case, '.../mysite'. Then run the following command:

`python manage.py runserver`

Start a browser on the host machine and go to 'http://localhost:8000/dnt/', where 'dnt' is the app name and 8000 is the default port.

### Using Docker to Run the Web Application

To do this you need to have [Compose installed](https://docs.docker.com/compose/install/). To check if you already have it, run `docker-compose --version`. 

Open terminal and go to the project root directory, i.e - the directory containing the `Dockerfile`. 

Run the command `docker-compose up`. It will take some time to build, but after it's done, the app should run at the port 8000. If you do not know the ip of the docker machine, use the `docker-machine ip` command to get it.
