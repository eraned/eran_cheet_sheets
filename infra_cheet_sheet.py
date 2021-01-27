
# jenkins
brew install jenkins-lts
brew services stop jenkins-lts
brew services start jenkins-lts
brew services restart jenkins-lts
cat /Users/eranedri/.jenkins/secrets/initialAdminPassword
# bash

# flask
export FLASK_APP=web_app
export FLASK_ENV=development
flask run

url : http://127.0.0.1:5000/


# docker

$ docker build -t app:latest /path/to/Dockerfile
$ docker run -d -p 5000:5000 app

docker push eraned/eran_edri_docker_hub:tagname

# kuberntes

# gcp cli


# aws cli

# terraform

# apache airflow
 

