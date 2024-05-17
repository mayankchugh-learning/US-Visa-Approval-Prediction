# steps-to-deploy-locally-on-docker

## https://hub.docker.com/_/ubuntu


## install docker

```bash
	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

    docker --version
```

## download image

```bash
docker pull ubuntu
```

## Create and start docker container interactive and detach with code mapping for ubuntu image
```bash
docker run -dit -p 8080:8080 ubuntu /bin/bash
```

## to list all containers 
```bash
docker ps -a
```

## to go into docker conatiner 
```bash
docker exec -it <container_id> /bin/bash
```

docker exec -it 46faaa72e730 /bin/bash

## update container
```bash
apt-get update -y
```
```bash
apt-get upgrade -y
```

```bash
apt-get install curl unzip -y
```

## install aws cli 

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip -u awscliv2.zip
./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
which aws
ls -l /usr/local/bin/aws
```

```bash
aws --version
```

# choose you region and country when prompt
## configure aws configuration
```bash
aws configure
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=/9fmfoI3U
AWS_DEFAULT_REGION=us-east-1

## Since model upload after training and application will download model from s3, hence we need to configure
```bash
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_DEFAULT_REGION=us-east-1
```
```bash
export MONGODB_URL="mongodb+srv://mayankchughlearning:z4E32JwhsC12LQTK@cluster0.oa9kol7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```
```bash
export AWS_ACCESS_KEY_ID=""

export AWS_SECRET_ACCESS_KEY=""

export AWS_DEFAULT_REGION="us-east-1"

## install python      
```bash
apt-get install python3-full -y
```

## install pip      
```bash
apt-get install pip -y
```

```bash
apt-get install mesa-utils -y
```

## install git nano vim
```bash
apt-get install git -y
apt-get install nano -y
apt-get install vim -y
```

## git clone
```bash
git clone https://github.com/mayankchugh-learning/US-Visa-Approval-Prediction.git
```

## change directory to clonned repository
```bash
cd US-Visa-Approval-Prediction
```
```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate
```
## install all requirement - Note: you may need to comment line with notebook  
```bash
pip install -r requirements.txt
```

## to check if aws cli is installed
```bash
aws --version
```

## exist from docker and then go into docker conatiner 
```bash
docker ps -a
docker exec -it <container_id> /bin/bash
```
docker exec -it 46faaa72e730 /bin/bash

## execute application
```bash
python3 app.py
```

## to list all containers 
```bash
docker ps -a
```

## to go into docker conatiner - Skip this step
```bash
docker exec -it <container_id> /bin/bash
```

### Exit Docker Container without Stopping It
- If you want to exit the container's interactive shell session, but do not want to interrupt the processes running in it, press Ctrl+P followed by Ctrl+Q. This operation detaches the container and allows you to return to your system's shell

```bash
docker commit <container_id>
```
docker commit 46faaa72e730 mayankchughjob/end-to-end-usvisa-prediction-mlmodel

```bash
docker image tag <image_id> <dockerhubid>/<name on dockerhub>:latest
```
docker image tag 8a5162116265 mayankchughjob/end-to-end-object-detection:latest

```bash
docker push <image id>
```
docker push mayankchughjob/end-to-end-usvisa-prediction-mlmodel 

#### Commands to pull image from docker hub and run it locally

```bash
docker pull mayankchughjob/end-to-end-usvisa-prediction-mlmodel:latest
```

```bash
docker run -dit -p 8080:8080 mayankchughjob/end-to-end-usvisa-prediction-mlmodel /bin/bash
```

## to list all containers 
```bash
docker ps -a
```

## to go into docker conatiner 
```bash
docker exec -it <container_id> /bin/bash
```
docker exec -it 582ca9056a26 /bin/bash
```bash
cd End-to-end-Object-Detection-Project/
```
```bash 
source path/to/venv/bin/activate
```
```bash 
python3 app.py
```

# docker image

https://docs.docker.com/engine/reference/commandline/image/#examples


## to list all images
```bash
docker image ls
```

# docker command line interface (cli)

```bash
https://docs.docker.com/engine/reference/commandline/


 AWS_ACCESS_KEY_ID=
 AWS_SECRET_ACCESS_KEY=
 AWS_DEFAULT_REGION=
```

## to stop all running container (reference only)
```bash
docker stop $(docker ps -a -q)
```

## to remove all stopped container (reference only)
```bash
docker rm $(docker ps -a -q)
```

## to remove all images
```bash
docker rmi $(docker images -a -q)
```

## to list all containers (reference only)
```bash
docker ps -a
```

## to list all images (reference only)
```bash
docker image ls
```

# docker-compose

https://docs.docker.com/compose/


# dockerfile

```bash
https://docs.docker.com/engine/reference/builder/#run
```
```bash
docker ps -a
```
```bash
docker restart <container_id>  #8f1a99a79b3d
```
```bash
docker exec -it <container_id> /bin/bash
# docker exec -it 8f1a99a79b3d /bin/bash
```
```bash 
source path/to/venv/bin/activate
```
```bash 
python3 app.py
```
