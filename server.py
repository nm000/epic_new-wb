from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./static/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/news", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("news.html", {"request": request})

@app.get("/funding", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("funding.html", {"request": request})

@app.get("/news", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("news.html", {"request": request})

@app.get("/faqs", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("faqs.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/learn", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("learn.html", {"request": request})

@app.get("/publications", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("publications.html", {"request": request})

@app.get("/framework", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("framework.html", {"request": request})

@app.get("/experiences", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("exp.html", {"request": request})

# Crear nueva página
#En la función de arriba se envía texto desde la funciíon hasta el html (podría usarse)
@app.get("/about", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def read_task1(request: Request): #El nombre de la función no importa

    Name1 = ["Extract key information from a map"]
    Functional1 = ["Ask and give directions, Describe locations", "Prepositions of place \n There is/There are, \n Yes/No questions"]
    Vocabulary1 = ["Mangrove forests, Swamps, Roads, Cities, Natural Park, Towns, Farms, and Beaches"]
    Reading1 = ["Read google maps locations"]
    Listening1 = ["Listen for information"]
    Pronunciation1 = ["Rising intonation in yes/no questions"]

    Name2 = ["Introducing animals from Salamanca Island"]
    Functional2 = ["Introducing self and other people, Exchanging personal info, Asking for and giving spelling", "Subject pronouns, Present tense be, Contractions, Wh-questions, A/An"]
    Vocabulary2 = ["Osprey, Hummingbird, Sea Bass, Alligator, Lizard, Fox, Otter, Seagull, Heron, Duck, Monkey, Manatee, Ocelot"]
    Reading2 = ["Salamanca Island Poster"]
    Listening2 = ["Animal sounds in the wild"]
    Pronunciation2 = ["Rising and falling intonation"]

    Name3 = ["Filling out a profile"]
    Functional3 = ["Talking about abilities, Asking for confirmation, Answering profile questions podcast", "Yes/No questions, Frequency adverbs, Can/Can't"]
    Vocabulary3 = ["Animals' body parts: fur, feathers, wings, claws, teeth, tail, fin, peak","Animals' abilities: fly, swim, run, attract, reach, protect, pull, hide, walk"]
    Reading3 = ["Read for details"]
    Listening3 = ["Listen for abilities"]
    Pronunciation3 = ["Word stress"]

    Name4 = ["Give directions from one place to another"]
    Functional4 = ["Correct given information, Ask someone to repeat", "Clauses: before, after, then. Prepositions of place, Wh Questions"]
    Vocabulary4 = ["Types of landscape: Sea, Mangrove, Swamp, Forest, Coast, Village"]
    Reading4 = ["Read travel signs"]
    Listening4 = ["Listen to recorded messages"]
    Pronunciation4 = ["Word stress"]

    Name5 = ["Compare animals' differences and similarities"]
    Functional5 = ["Asking and telling the time, Asking for information", "Adjectives to describe animals: Tiny, Small, Big, Clever, Furry, Cute, Fast, Slow. Present simple"]
    Vocabulary5 = ["Weather: warm, hot, windy, wet, rainy, dry"]
    Reading5 = ["Read weather map"]
    Listening5 = ["Listen to recorded messages"]
    Pronunciation5 = ["Vowel sounds"]

    return templates.TemplateResponse("about.html", {"request": request, "name1": Name1, "funct1": Functional1, "voc1": Vocabulary1, "read1": Reading1, "listen1": Listening1, "pron1": Pronunciation1, "name2": Name2, "funct2": Functional2, "voc2": Vocabulary2, "read2": Reading2, "listen2": Listening2, "pron2": Pronunciation2, "name3": Name3, "funct3": Functional3, "voc3": Vocabulary3, "read3": Reading3, "listen3": Listening3, "pron3": Pronunciation3, "name4": Name4, "funct4": Functional4, "voc4": Vocabulary4, "read4": Reading4, "listen4": Listening4, "pron4": Pronunciation4, "name5": Name5, "funct5": Functional5, "voc5": Vocabulary5, "read5": Reading5, "listen5": Listening5, "pron5": Pronunciation5}) # Renderizar la plantilla html correspodiente dentro de Templates

@app.get("/sal-isl", response_class=HTMLResponse) # Ruta que va a tener la nueva página
def salamanca(request: Request): #El nombre de la función no importa
    return templates.TemplateResponse("salamancaHome.html", {"request": request}) # Renderizar la plantilla html correspodiente dentro de Templates
#En la función de arriba se envía texto desde la funciíon hasta el html (podría usarse)
