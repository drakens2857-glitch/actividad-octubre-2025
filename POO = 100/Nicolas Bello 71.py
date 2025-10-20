from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

class GeneradorReportesPDF:
    def __init__(self):
        self.styles = getSampleStyleSheet()

    def generar_reporte_prestamos(self, prestamos, nombre_archivo='reporte_prestamos.pdf'):
        doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
        elementos = []

        titulo = Paragraph("REPORTE DE PRÉSTAMOS<br/>SENA Mosquera - CBA", self.styles['Title'])
        elementos.append(titulo)
        elementos.append(Spacer(1, 0.3 * inch))

        fecha = Paragraph(f"Fecha del reporte: {datetime.now().strftime('%d/%m/%Y %H:%M')}", self.styles['Normal'])
        elementos.append(fecha)
        elementos.append(Spacer(1, 0.3 * inch))

        datos_tabla = [['ID', 'Libro', 'Usuario', 'Fecha', 'Estado']]
        for prestamo in prestamos:
            fila = [
                prestamo['id'],
                prestamo['libro'][:30],
                prestamo['usuario'][:20],
                prestamo['fecha'].strftime('%d/%m/%Y'),
                '✓ Devuelto' if prestamo['devuelto'] else '✗ Pendiente'
            ]
            datos_tabla.append(fila)

        tabla = Table(datos_tabla, colWidths=[0.8*inch, 2.5*inch, 2*inch, 1.5*inch, 1.2*inch])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
        ]))

        elementos.append(tabla)
        doc.build(elementos)
        return f"Reporte generado en {nombre_archivo}"
