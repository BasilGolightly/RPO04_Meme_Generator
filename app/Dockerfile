# Nalozi sliko / image pythona
FROM python:3.14-slim

# nastavi CWD na /memeGenerator
WORKDIR /memeGenerator

# kopiraj datoteke iz CWD v container
COPY ./memeGenerator .

# nalozi odvisnosti oz. depencencies zapisane v requirements.txt
RUN pip install -r requirements.txt

# odpri vrat 5000 za aplikacijo
EXPOSE 5000

# izvedi "pythom meme.py"
CMD ["python", "meme.py"]




