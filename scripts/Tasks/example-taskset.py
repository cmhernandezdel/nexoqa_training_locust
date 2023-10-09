from locust import TaskSet, constant, task, HttpUser
import random

# hace las tareas de forma aleatoria
class TaskSetExample(TaskSet):

    @task
    def get(self):
        self.client.get("/songs")
        print("Get Songs")

    @task
    def get_random_songs(self):
        songs = [1,2,3,4,5]
        random_url = "/songs/" + str(random.choice(songs))
        res = self.client.get(random_url)
        print("Random songs")


class MyLoadTest(HttpUser):
    host = "http://localhost:8081"
    tasks = [TaskSetExample]
    wait_time = constant(1)