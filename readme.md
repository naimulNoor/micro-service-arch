Decs : Digit Service Arch


test file 

curl -X POST -H "Content-Type: application/json" -d '{"data": "I am roni", "lang": "bn"}' http://translation-service:8082/translate-text


Configure Minikube to Use Local Docker Daemon:

By default, Minikube uses its own Docker daemon to manage container images. To use a local Docker daemon instead (which allows you to use your local Docker images), you can configure Minikube to use the Docker daemon on your host system. Run the following command:

bash

eval $(minikube docker-env)

This command sets up your shell environment to use the Docker daemon inside the Minikube VM.