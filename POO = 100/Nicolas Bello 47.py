from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    precio = Column(Integer)

    def __repr__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})"

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

nuevo_producto1 = Producto(nombre='Laptop', precio=1200)
nuevo_producto2 = Producto(nombre='Mouse', precio=25)
session.add(nuevo_producto1)
session.add(nuevo_producto2)
session.commit()

print("Productos en la base de datos:")
for producto in session.query(Producto).all():
    print(producto)

print("\nProductos con precio mayor a 100:")
for producto in session.query(Producto).filter(Producto.precio > 100):
    print(producto)

mouse = session.query(Producto).filter_by(nombre='Mouse').first()
if mouse:
    mouse.precio = 30
    session.commit()
    print(f"\nPrecio del Mouse actualizado: {mouse}")

laptop = session.query(Producto).filter_by(nombre='Laptop').first()
if laptop:
    session.delete(laptop)
    session.commit()
    print(f"\nLaptop eliminada. Productos restantes:")
    for producto in session.query(Producto).all():
        print(producto)

session.close()
print("\nSesión de SQLAlchemy cerrada.")
