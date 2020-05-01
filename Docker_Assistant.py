import os

# Check if Docker is instaled or not

def docker_status():
    print("\nChecking if docker is installed or not....\n")

    os.system("sleep 3")
    flag = os.system("docker --version")
    if flag != 0:
        print("\ndocker is not installed int this system.\n")
        docker_install()
        status=0
    else:
        print("\nDocker is installed.\n")
        status=1
    return(status)

# Installing Docker

def docker_install():
    ans = str(input("Do you want to install docker (y/n): "))
    if ans == 'y':
        print("Downloading the Docker Engine....")
        os.system("curl -sSL https://get.docker.com | sh")
        os.system("yum -y install docker-ce --nobest")
        os.system("systemctl start docker")
        os.system("systemctl enable docker")
        os.system("systemctl status docker")
        status = docker_status()
        check_in(status)
    elif ans == 'n':
        print("OK then.... Goodbye....")
        exit()
    else:
        print("Invalid Entry. Make a valid entry.")
        ans = str(input("Do you want to install docker (y/n): "))
        if ans == 'y':
            docker_install()
        elif ans == 'n':
            print("OK then.... Good Bye...")
            exit()
        else:
            print("Invalid Option. Please try again. Good Bye...")
            exit()
        
        exit()

# Docker Components

def docker_components():
    
    os.system("sleep 3")
    print("\n\n\t\t\tMAIN MENU\n\n")
    print("""What would you prefer amongst the below options?

    Press 1 for CONTAINERS
    Press 2 for IMAGES
    Press 3 for VOLUMES
    Press 4 for DOCKER COMPOSE
    """)
    ch = str(input("Please choose an option: "))
    return(ch)

# Main Menu

def main_menu(ch):
    if ch == '1':
        container()
    elif ch == '2':
        ch == image()
    elif ch == '3':
        ch == volume()
    elif ch == '4':
        docker_compose()
    elif ch == 'e':
        exit()
    else:
        retry_main_menu()

# Docker Status Check

def check_in(status):

    if status == 1:
        ch = docker_components()
        main_menu(ch)
    else:
        docker_install()

# Container Operations

def container():
        print("\n\n\n\t\t\tCONTAINERS\n\n\n")
        print("""\n\nPlease choose one of the below options:

        Press 1 to CHECK all the available CONTAINERS
        Press 2 to START an available CONTAINER
        Press 3 to ACCESS an available CONTAINER
        Press 4 to REMOVE containers
        Press 5 to CREATE a new CONTAINER
        Press 6 to STOP a CONTAINER
        Press 7 to INSPECT a CONTAINER
        Press 8 to check LOGS of a CONTAINER
        Press b to GO BACK to MAIN MENU
        Press e to EXIT""")
        ch = str(input("Please choose an option: "))

        if ch == '1':
            os.system("docker ps -a")
            retry_container()
        elif ch == '2':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker start {}".format(name))
            retry_container()
        elif ch == '3':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker attach {}".format(name))
            retry_container()
        elif ch == '4':
            print("""Do you want to remove a specific one or all-of-them.
            Please enter the SPECIFIC CONTAINER NAME (Only the SPECIFIC CONTAINER will be removed)
            Please enter 'ALL' to remove all the containers
            (CASE SENSITIVE)""")
            name = str(input("Please enter the name or id of the container: "))
            if name == 'ALL':
                os.system("docker rm -f $(docker ps -a -q)")
            else:
                os.system("docker rm {}".format(name))
            retry_container()
        elif ch == '5':
            name = str(input("Please enter the name of the container: "))
            print("Please enter the name of the enlisted image you want to launch: ")
            os.system("docker images")
            image = str(input("Please enter the image name: "))
            version = str(input("Please enter the image version: "))
            info = str(input("Enter additional info (if any) : "))
            os.system("docker run -dit --name {} {} {}:{}".format(name,info,image,version))
            retry_container()
        elif ch == '6':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker stop {}".format(name))
            retry_container()
        elif ch == '7':
            name = str(input("Please enter the name or id of the container: "))
            ans = str(input("Do you have any specific search request (y/n) : "))
            if ans == 'y':
                request = str(input("""Pleas enter the specific search request 
                (CAUTION: It is CASE SENSITIVE) : """))
                os.system("docker inspect {} | grep {}".format(name,request))
            else:
                os.system("docker inspect {} ".format(name))
            retry_container()
        elif ch == '8':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker logs {}".format(name))
            retry_container()
        elif ch == 'e':
            print("Ok then... Goodbye...")
            exit()
        elif ch == 'b':
            retry_main_menu()
        else :
            print("Invalid option. Please make a valid entry and try again")
            retry_container()

# Images Operation

def image():
        print("\n\n\n\t\t\tIMAGES\n\n\n")
        print("""\n\nPlease choose one of the below options:

        Press 1 to CHECK available IMAGES
        Press 2 to INSPECT an IMAGE
        Press 3 to SEARCH IMAGES
        Press 4 to PULL an IMAGE
        Press 5 to BUILD an IMAGE (under development)
        Press 6 to PUSH an IMAGE (under development)
        Press 7 to REMOVE IMAGE
        Press 8 to HISTORY
        Press b to GO TO MAIN MENU
        Press e to EXIT""")
        ch = str(input("Please choose an option: "))

        if ch == '1':
            os.system("docker images")
            retry_image()
        elif ch == '2':
            os.system("docker images")
            name = str(input("Please enter the IMAGE NAME: "))
            ver = str(input("Please enter the IMAGE VERSION: "))
            ans = str(input("Do you have any SPECIFIC INSPECT REQUEST (y/n) : "))
            if ans == 'y':
                request = str(input("""Pleas enter the SPECIFIC INSPECT REQUEST 
                (CAUTION: It is CASE SENSITIVE) : """))
                os.system("docker image inspect {} | grep {}".format(name,request))
            else:
                os.system("docker image inspect {} ".format(name))
            retry_image()
        elif ch == '3':
            name = str(input("Please enter the IMAGE NAME : "))
            os.system("docker search {}".format(name))
            retry_image()
        elif ch == '4':
            name = str(input("Please enter the IMAGE NAME you want to PULL: "))
            os.system("docker pull {}".format(name))
            retry_image()
        elif ch == '5':
            print("Comming Soon... ")
            retry_image()
        elif ch == '6':
            print("Comming Soon... ")
            retry_image()
        elif ch == '7':
            name = str(input("Please enter the IMAGE NAME: "))
            ver = str(input("Please enter the VERSION"))
            os.system("docker image rm {}:{}".format(name,ver))
            retry_image()
        elif ch == '8':
            name = str(input("Please enter the IMAGE NAME: "))
            ver = str(input("Please enter the VERSION"))
            os.system("docker image history {}:{}".format(name,ver))
            retry_image()
        elif ch == 'e':
            print("Ok then... Goodbye...")
            exit()
        elif ch == 'b':
            retry_main_menu()
        else :
            print("Invalid option. Please make a valid entry and try again")
            retry_image()

# Volume Operations

def volume():
        print("\n\n\n\t\t\IMAGES\n\n\n")
        print("Coming Soon... ")
        retry_main_menu()

# Docker Compose

def docker_compose():
    print("\n\n\n\t\t\tDOCKER COMPOSE\n\n\n")
    status = compose_status()
    if status == 1:
        path = str(input("Enter path to docker compose file: "))
        os.system("cd {}".format(path))
        os.system("docker-compose up -d")
    else:
        compose_install()

# Docker Compose Status

def compose_status():
    flag = os.system("docker-compose -v")
    if flag == 0:
        print("docker-compose is installed")
        flag = 1
    else:
        compose_install()
        flag = 0
    return(flag)

# Docker Compose installation

def compose_install():
    ans = str(input("Do you want to install docker-compose (y/n) : "))
    if ans == 'y':
        print("Installing docker-compose...")
        os.system("pip3 install docker-compose")
        compose_status()
    elif ans == 'n':
        print("Returning to MAIN MENU...")
        retry_main_menu()
    else:
        ans = str(input("Invalid Entry. Do you want to try again (y/n) : "))
        if ans == 'y':
            compose_install()
        else:
            print("Returning to MAIN MENU...")
            docker_components()

# For retrying MAIN MENU

def retry_main_menu():
    ans = str(input("Do you want to go to MAIN MENU (y/n): "))
    if ans == 'y':
        ch = docker_components()
        main_menu(ch)
    elif ans == 'n':
        print("OK then.... Good Bye...")
        exit()
    else:
        print("Invalid Option. Please try again. Good Bye...")
        exit()

# For retrying CONTAINER MENU

def retry_container():
    ans = str(input("Do you want to CONTINUE (y/n): "))
    if ans == 'y':
        container()
    elif ans == 'n':
        print("OK then.... Good Bye...")
        exit()
    else:
        print("Invalid Option. Please try again. Good Bye...")
        retry_container()

# For retrying IMAGES MENU

def retry_image():
    ans = str(input("Do you want to CONTINUE (y/n): "))
    if ans == 'y':
        image()
    elif ans == 'n':
        print("OK then.... Good Bye...")
        exit()
    else:
        print("Invalid Option. Please try again. Good Bye...")
        retry_image()

# For retrying VOLUME MENU

def retry_volume():
    ans = str(input("Do you want to CONTINUE (y/n): "))
    if ans == 'y':
        volume()
    elif ans == 'n':
        print("OK then.... Good Bye...")
        exit()
    else:
        print("Invalid Option. Please try again. Good Bye...")
        retry_volume()

print("""\n\n\n\t\t\tWELCOME TO DOCKER ADMIN\n\n
This is a python program that will assist you while using dockers""")
status = docker_status()
check_in(status)
