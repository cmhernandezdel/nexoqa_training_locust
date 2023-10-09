import json
import random
from locust import HttpUser, SequentialTaskSet, constant, task

# ejemplo: registrar y hacer login de usuarios
# son tareas secuenciales, primero una y luego otra
class RegisterAndLogin(SequentialTaskSet):

    # el self es importante ponerlo
    @task
    def register(self):
        self.data='{"email":"visiotech' + str(random.randrange(1,1000)) + '@test.com", "password": "Ab123456"}'
        headers= {"Content-Type":"application/json"}
        obj = json.loads(self.data)
        name=f"{obj['email']}"

        # name para poder identificar las requests
        self.client.post('/register', json=obj, name=name, headers=headers)

    @task
    def login(self):
        headers= {"Content-Type":"application/json"}
        self.client.post('/login', json=json.loads(self.data), headers=headers)

class RegisterHttpUser(HttpUser):
    host="http://localhost:8081"
    wait_time = constant(1)
    tasks = [RegisterAndLogin]