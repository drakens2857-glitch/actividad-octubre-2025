import requests

def buscar_libro_openlibrary(titulo):
    url = f"https://openlibrary.org/search.json?title={titulo}"
    r = requests.get(url)
    return r.json()['docs'][0] if r.status_code == 200 else None
