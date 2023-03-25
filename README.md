# FlaskDockPy
Web Flask Target for Docker in python

1. install docker in your local machine from https://docs.docker.com/get-docker/
2. your local machine need to have python run [pip install python](https://www.python.org/downloads/)
3. i am using visual code put all 3 files in one directory
4. run -> docker build . -t hworld:latest to create image
5. once step 4 is done then run -> docker run -p 5050:5050 hworld:latest
6. now in browser use the ip shown in docker run to see program output
