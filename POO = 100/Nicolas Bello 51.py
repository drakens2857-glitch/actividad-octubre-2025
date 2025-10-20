from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 75}
]

@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos)

@app.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto_encontrado = next((p for p in productos if p['id'] == producto_id), None)
    if producto_encontrado:
        return jsonify(producto_encontrado)
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@app.route('/productos', methods=['POST'])
def add_producto():
    nuevo_producto = request.get_json()
    if not nuevo_producto or 'nombre' not in nuevo_producto or 'precio' not in nuevo_producto:
        return jsonify({"mensaje": "Datos de producto incompletos"}), 400
    nuevo_producto['id'] = len(productos) + 1
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

if __name__ == '__main__':
    app.run(debug=True)
