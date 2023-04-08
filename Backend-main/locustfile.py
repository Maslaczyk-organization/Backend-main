from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_home_page(self):
        self.client.get("/")

    @task(3)  # give more weight to this task
    def load_hello_page(self):
        self.client.get("/hello")

    @task(2)
    def load_greetings_page(self):
        params = {"name": "John Smith"} # change name as needed
        self.client.get("/namesake", params=params)
