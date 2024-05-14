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

docker exec -it 79b66025a95f /bin/bash

## update container
```bash
apt-get update -y
```
```bash
apt-get upgrade -y
```

```bash
apt-get install curl -y
apt-get install unzip -y
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

## Since model upload after training and application will download model from s3, hence we need to configure
```bash
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_DEFAULT_REGION=us-east-1
```
## install python      
```bash
apt-get install python3
apt-get install python3.12-venv
apt-get install python3-full -y
```

## install pip      
```bash
apt-get install pip -y
```

```bash
apt-get install libgl1-mesa-glx -y
apt-get install mesa-utils -y
```

## install git
```bash
apt-get install git -y
```

## install nano
```bash
apt-get install nano
```

## install vi
```bash
apt-get install vim
```

## install unzip
```bash
apt-get install unzip
```

## git clone
```bash
git clone https://github.com/mayankchugh-learning/End-to-end-Object-Detection-Project.git
```

## change directory to clonned repository
```bash
cd End-to-end-Object-Detection-Project
```
```bash
python3 -m venv .
python3 -m venv path/to/venv
source path/to/venv/bin/activate
pip install -r requirements.txt
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
docker exec -it c54efff4244e /bin/bash

## execute application
```bash
python3 app.py
```
## Note: you may need to create folder structure inside yolo5 folder - runs/detect/exp and then copy 
```bash
cd yolov5
mkdir runs
cd runs
mkdir detect
cd detect
mkdir exp
cd exp
# inside End-to-end-Object-Detection-Project
cd data
cp inputImage.jpg ../yolov5/runs/detect/exp/ 
```
## to list all containers 
```bash
docker ps -a
```

## to go into docker conatiner 
```bash
docker exec -it <container_id> /bin/bash
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
### Exit Docker Container without Stopping It
- If you want to exit the container's interactive shell session, but do not want to interrupt the processes running in it, press Ctrl+P followed by Ctrl+Q. This operation detaches the container and allows you to return to your system's shell

```bash
docker commit <container_id>
```
docker commit c54efff4244e

```bash
docker image tag <image_id> <dockerhubid>/<name on dockerhub>:latest
```
docker image tag 8a5162116265 mayankchughjob/end-to-end-object-detection:latest

```bash
docker push <image id>
```
docker push mayankchughjob/end-to-end-object-detection:latest

#### Commands to pull image from docker hub and run it locally

```bash
docker pull mayankchughjob/end-to-end-object-detection:latest
```

```bash
docker run -dit -p 8080:8080 mayankchughjob/end-to-end-object-detection /bin/bash
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