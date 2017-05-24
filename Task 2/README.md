## Hello, Docker

The `click` module is used to create a command line application. Open a command line interface and simply type `python <filepath>hello_docker.py`. The program prints "Hello, Docker" to the console. The `click` module also automatically creates a help section which is printed when the `--help` option is used.

## Building Container Using Dockerfile

There is a `.txt` file named `Dockerfile`. The Dockerfile contains all the information required to build an image for the application. We specify a Python runtime, ask it to install any libraries required and finally run the Python script we want. The requirements.txt just lists all the libraries we need. Put all three files (Dockerfile, requirements.txt, <filename>.py) in an empty directory. In a command-line interface, first type `docker build -t hello .` This will build the container. Then type `docker run hello`. It will print "Hello, Docker" to the console.   
