# Meme Generator, Mark Sadnik, RIT 2 UN
A simple meme generator made with flask for a school assignment.
The emphasis is on using docker to create a lightweight container for running the app.

It works by inputting two strings of text (top and bottom text) via an HTML form and uploading an image (.jpg, .png, .gif or .webp). 
The inputted text then gets drawn onto the top and bottom of the uploaded image respectively.
If the generation failed, a simple error message will be shown.

## Purpose
The main goal is to demonstrate the usage of Docker for educational purposes (RPO - Razvoj Programske Opreme course at FERI, 2nd year) 

## How to run it

### Docker 
**REQUIREMENT:** Docker desktop

Navigate to the /app folder, where there is a prepared Dockerfile and all the necessary files for the app.

```powershell
# build the container
docker build -t meme-generator -f Dockerfile .

# run the container
docker run -p 5000:5000 meme-generator

# check the status via command line
# alternative: check on docker desktop
docker ps
```

### Python without container
**REQUIREMENTS:** 
    - Latest version of Python 3

    - Virtual environment venv

    - Flask

    - Pillow (PIL)

To create a virtual environment and activate it:

```powershell
# create a virtual environment in the /app folder
python -m venv .venv

# activate it
.venv\Scripts\activate
```

Install dependencies:

```powershell
# install pip 
python -m pip install --upgrade pip

# check version
py -m pip --version

# create dependency file
pip freeze > requirements.txt

# install requirements via requirements file
pip install -r memeGenerator/requirements.txt
```

## Final message 
Have fun and try to create the funniest meme in existence.

Your truly,

Mark Sadnik, RIT 2 UN