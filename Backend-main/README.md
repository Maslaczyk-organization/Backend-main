# project-backend

To run the project, follow these steps:

Create an image by typing "docker build . -t image_name" in the terminal.
Once the image is created, run it on port "8000".
For Docker Desktop users, go to the "Images" tab, select the image, and click the "run" button.
Expand the "Optional Settings" menu and enter "8000" in the "Ports" field, than click "Run".
A terminal window will appear and prompt you to select the first option and the application should now be ready for use.

#Testing
To load test our app, we use a tool called Locust. Here are the steps to run Locust:

* Install Locust by running pip install locust in your command prompt or terminal.
* Start the app by running python app.py in your command prompt or terminal.
* Start the Locust master by running locust --host=http://localhost:5000 in your command prompt or terminal.
* Open your web browser and go to http://localhost:8089.
* Set the number of users and spawn rate on the web page, then click "Start Swarming" to start the test.
You can modify the tasks in the locustfile.py file to test different endpoints or simulate different user behavior.
