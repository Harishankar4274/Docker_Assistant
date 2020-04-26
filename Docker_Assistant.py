import os

# Check if Docker is instaled or not

def docker_status():
    print("Checking if docker is installed or not....")

    os.system("sleep 3")
    flag = os.system("docker --version")
    if flag != 0:
        print(flag)
        print("docker is not installed int this system.")
        docker_install()
        flag=0
    else:
        print("Docker is installed.\n")
        flag=1
    return(flag)

# Installing Docker

def docker_install():
    ans = str(input("Do you want to install docker (y/n): "))
    if ans == y:
        print("Downloading the Docker Engine....")
        os.system("sudo curl -sSL https://get.docker.com | sh")
    elif ans == n:
        print("OK then.... Goodbye....")
        exit()
    else:
        i=0
        while i < 3:
            print("Invalid Entry. Make a valid entry.")
            docker_install()
            i += 1
        exit()

# Docker Components

def docker_components():
    
    os.system("sleep 3")
    print("\n\n\t\t\tMAIN MENU\n\n")
    print("""What would you prefer amongst the below options?

    Press 1 for CONTAINERS
    Press 2 for IMAGES
    Press 3 for VOLUMES""")
    ch = str(input("Please choose an option: "))
    return(ch)

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
        Press b to GO BACK to MAIN MENU
        Press e to EXIT""")
        ch = str(input("Please choose an option: "))

        if ch == '1':
            os.system("docker ps -a")
        elif ch == '2':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker start {}".format(name))
        elif ch == '3':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker attach {}".format(name))
        elif ch == '4':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker rm {}".format(name))
        elif ch == '5':
            name = str(input("Please enter the name of the container: "))
            image = str(input("Please enter the image name: "))
            version = str(input("Please enter the image version (press enter for latest version): "))
            os.system("docker run -dit --name {} {}:{}".format(name,image,version))
        elif ch == '6':
            name = str(input("Please enter the name or id of the container: "))
            os.system("docker stop {}".format(name))
        elif ch == 'e':
            print("Ok then... Goodbye...")
            exit()
        elif ch == 'b':
            docker_components()
        else :
            print("Invalid option. Please make a valid entry and try again")
            ans = str(input("Do you wanrt to continue (y/n): "))
            if ans == 'y':
                container()
            elif ans == 'n':
                print("Bye...")
            else:
                print("Invalid Entry... Terminating...")
                exit()

# Images Operation

# Volume Operations

print("""\n\n\n\t\t\tWELCOME TO DOCKER ADMIN\n\n
This is a python program that will assist you while using dockers""")
status = docker_status()

if status == 1:
    ch = docker_components()
else:
    docker_install()

if ch == 'e':
    exit()
elif ch == '1':
    container()
