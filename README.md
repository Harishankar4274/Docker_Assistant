# Docker_Assitant

Docker Assistant is a TUI based administrating tool for Docker on RHEL/CentOS platforms.
It installs and manages other components of Docker like Containers, Images and Volumes(under development).
This is the prototype of the program. It manages some functionalities of Containers, Images and Volumes.

It is an **Opensource** tool anyone use it and develop it accordingly.

## Prerequisites:

1.  Currently the program is available only for **RHEL/CentOS**
2.  Python 3
3.  Git
4.  pip
5.  Yum must be configured

## How to use:

It is a simple python program. Just download it and execute it. Follow the below procedure to use the tool:

1.  Get the tool by the command: `# git clone https://github.com/Harishankar4274/Docker_Assistant.git` or you can just download       the file from the link https://github.com/Harishankar4274/Docker_Assistant.git
2.  Go in the Docker_Assistant Directory using the command `# cd /path/to/Docker_Assistant`.
3.  Run the tool by `python3 Docker_Assistant.py`.
4.  First of all the tool will check if you have docker installed or not. The command behind this is `docker --version` If yes then it will take you to the main menu. If not then the program will install it (if the yum is configured). the command behind this is `curl -sSL https://get.docker.com | sh` and `yum -y install docker-ce --nobest`. The latter one runs if earlier one fails. Once the docker is installed, then the tool again checks the status.
5. In the **Main Menu**, currently there are 4 options available:
### Main Menu
  1. Container: for operations related to containers
  2. Image : for operations related to images
  3. Volume : for operations related to volumes
  4. Docker Compose : for operating docker-compose

## Screenshots:

### 1. Starting Docker Assitant:

To start Docker_Assistant first you have to go inside the Docker_Assistant directory by using the command `cd /path/to/Docker_Assistant/` in the terminal. Now you have to start to tool by using `pyhton3 Docker_Assistant.py`. Now the tool checks if the **Docker** is installed or not. Below is the screenshot of the process:
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/1.Docker_Assistant_Start.png">

### 2. Installing Docker(If not installed):
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/2.Docker_installation.png">

### 3. Activating Docker:
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/3.Docker_Service_started.png">

### 4. Main Menu of the tool:
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/4.Main_Menu.png">

### 5. Container Menu:
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/5.Container_menu.png">

### 6. Image Menu:
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/6.Images_menu.png">

### 7. Docker-Compose:
Here as well, the tool checks if the docker-compose is installed or not. If not installed it asks for your permission. If user allow then it installs the docker-compose using the command `pip3 install docker-compose`.
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/7.Docker_Compose_Menu.png">

#### 7.1 Docker-Compose Installation:
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/8.Docker_Compose_Installation.png">

#### 7.2 Docker-Compose Menu:
Once the docker-compose installation process is completed, it again check for the staus and asks for path to docker-compose.yml file. once you enter the path to the file. Then it extracts the information from the file and starts deployment.
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/9.Docker_Compose_Deployment.png">

#### 7.3 Docker-Compose Deplyment Completed:
<img src="https://github.com/Harishankar4274/Docker_Assistant/blob/master/Docker_Assistant_SS/10.Deployment_completed.png">

## Future Plan:

**Want to Add some more functions to it:**

1.  OS Detection.
2.  Installation of Docker according to OS.
3.  Enhance the available features
