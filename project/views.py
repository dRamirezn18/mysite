from django.shortcuts import render

data = [
  {
    "id": "1",
    "title": "My first Django Project", 
    "description": "The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) ",
    "author": "Daniel Ramirez"},
  
  {
    "id": "2",
    "title": "My first Flask Project", 
    "description": "The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) ",
    "author": "Miguel Prado"},

  {
    "id": "3",
    "title": "My first FastAPI Project", 
    "description": "The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) ",
    "author": "Victoria Maxwill"},  
]


# Create your views here.
def index(request, pk):
  projectObject = None
  for i in data:
    if i["id"] == str(pk):
      projectObject = i

  return render(request, 'project/index.html', {"project": projectObject})