from locust import SequentialTaskSet, constant, task, HttpUser
import random


# hace las tareas en orden secuencial
class SequentialTaskSetExample(SequentialTaskSet):

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
    tasks = [SequentialTaskSetExample]
    wait_time = constant(1)