# school-project

## Development Setop

### Prerquisites

1. `Git` - Follow instructions on https://git-scm.com/downloads to download it.
2. `Docker` and `Docker compose` - To install on windows follow instructions on https://hub.docker.com/editions/community/docker-ce-desktop-windows/.
3. `Python` - Go to https://www.python.org/downloads/ to intall python. Install version **`3.8`** as `3.9` still has many bugs.
4. `virtualenv` - Once python is installed run `pip3 install virtualenv` to install it.
5. A text editor, preferably VS Code

### Setup project

Navigate to your Documents folder, and clone this repository. To do this, follow the commands below:

```shell
# Navigate to the Documents folder
$ cd ~\Documents

# Clone this repository into your documents folder. Git will prompt you for credentials. Enter your github username and password
$ git clone https://github.com/shreyas44/school-project

# Navigate to the school-project folder
$ cd school-project

# Create a virtual environment for the project
$ virtualenv .

# Activate the virtual environemt
$ source bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Start PostgreSQL database and run it in the background
$ docker-compose up -d

# Start Django development server
$ python manage.py runserver
```

You should now have a folder named school-project in your Documents folder. Open the folder in VS Code, make changes and watch the changes appear in the browser!

To view the running application, go to https://localhost:8000

