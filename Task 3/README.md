### Running web application

Simply open the HTML file, and the web page will start in your default web browser.

### Build a Docker container to run web application

To run the web page in a Docker container copy the html file, jpeg file and Dockerfile into a directory, start your command-line interface and go to the directory where the files are stored.

`cd "path/to/file"`

Next, we need to build the Docker image. Name the image whatever you like. The `:v1` is used to tag the image for easier reference. Notice the `.` at the end. 

`docker build -t some_image_name:v1 . `

Then run the docker container. You can use a port other than 80, like 8080, too. 

`docker run -d -p 80:80 some_image_name:v1`

Finally, to view the web page, check your docker virtual machine ip by doing

`docker-machine ip`

With the ip address you get (for example- 192.168.99.100), open your preferred browser and just go to 'http://192.168.99.100:80/datetime.html'. You can replace '80' with whatever port you have chosen and 'datetime.html' with your preferred file name.
NOTE: Do not try opening the page in any form of Private Browsing. 

### Using a pre-built Docker container to run web application

You can also use a container that has already been built, by loading a .tar file into your docker machine.
Download the tar file provided, which contains the pre-built image. In your docker console, run the following lines:

`docker load -i <path/to/file/dw.tar>`

It will give a result like `Loaded image: django_webapp:v1`. Then do,

`docker run -d -p 80:80 django_webapp:v1` 

Then open your preferred browser and go to 'http://192.168.99.100:80/datetime.html'.
