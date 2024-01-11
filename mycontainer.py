# mycontainer.py

import subprocess
import os

class MyContainer:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def create(self):
        subprocess.run(["docker", "create", "--name", self.name, self.image])

    def start(self):
        subprocess.run(["docker", "start", self.name])

    def stop(self):
        subprocess.run(["docker", "stop", self.name])

if __name__ == "__main__":
    # Example Usage
    container_name = "myapp_container"
    container_image = "nginx:latest"

    my_container = MyContainer(container_name, container_image)

    # Create and start the container
    my_container.create()
    my_container.start()

    # Do some work inside the container...

    # Stop the container
    my_container.stop()
