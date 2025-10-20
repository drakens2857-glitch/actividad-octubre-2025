import requests

class IntegradorAPIs:
    def __init__(self):
        self.base_url_google_books = "https://www.googleapis.com/books/v1/volumes"

    def buscar_info_libro(self, isbn):
        try:
            url = f"{self.base_url_google_books}?q=isbn:{isbn}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get('totalItems', 0) > 0:
                    libro = data['items'][0]['volumeInfo']
                    return {
                        'titulo': libro.get('title'),
                        'autores': libro.get('authors', []),
                        'editorial': libro.get('publisher'),
                        'año': libro.get('publishedDate'),
                        'descripcion': libro.get('description'),
                        'paginas': libro.get('pageCount'),
                        'categoria': libro.get('categories', []),
                        'portada': libro.get('imageLinks', {}).get('thumbnail')
                    }
            return None
        except Exception as e:
            return {'error': str(e)}

    def obtener_recomendaciones(self, genero, max_resultados=5):
        try:
            url = f"{self.base_url_google_books}?q=subject:{genero}&maxResults={max_resultados}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                recomendaciones = []
                for item in data.get('items', []):
                    info = item['volumeInfo']
                    recomendaciones.append({
                        'titulo': info.get('title'),
                        'autores': ', '.join(info.get('authors', ['Desconocido'])),
                        'descripcion': info.get('description', 'Sin descripción')[:200]
                    })
                return recomendaciones
            return []
        except Exception as e:
            return {'error': str(e)}


class SistemaRecomendaciones:
    def __init__(self):
        self.api_integrador = IntegradorAPIs()
        self.historial_usuario = {}

    def registrar_lectura(self, usuario_id, genero):
        if usuario_id not in self.historial_usuario:
            self.historial_usuario[usuario_id] = []
        self.historial_usuario[usuario_id].append(genero)

    def recomendar_para_usuario(self, usuario_id):
        if usuario_id not in self.historial_usuario:
            return []
        generos = self.historial_usuario[usuario_id]
        genero_favorito = max(set(generos), key=generos.count)
        return self.api_integrador.obtener_recomendaciones(genero_favorito)
