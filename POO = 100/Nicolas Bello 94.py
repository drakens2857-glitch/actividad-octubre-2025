import qrcode

def generar_qr(texto, nombre_archivo='etiqueta_qr.png'):
    img = qrcode.make(texto)
    img.save(nombre_archivo)
    print(f'Código QR guardado como {nombre_archivo}')
