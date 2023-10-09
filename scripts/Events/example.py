from locust import HttpUser, task, constant, SequentialTaskSet
from locust import events

import logging


@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    print("Spawned ... ", user_count, " users.")


@events.quitting.add_listener
def sla(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 0.01%")
        environment.process_exit_code = 1
        print(environment.process_exit_code)

    else:
        environment.process_exit_code = 0
        print(environment.process_exit_code)


class LoadTest(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/songs", name="SuccessRequests")
        # self.client.get("/song", name="FailRequests")


class TestScenario(HttpUser):
    host="http://localhost:8081"
    wait_time = constant(1)
    tasks = [LoadTest]