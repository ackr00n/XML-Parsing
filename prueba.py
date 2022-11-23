"""
print("Prueba Python")
from bs4 import BeautifulSoup
import lxml
with open ("Clientes.xml","r") as f:
    data= f.read()

bs_data = BeautifulSoup(data,"xml")
telefono = bs_data.find_all("telefono")
print (telefono)
print("-------------------------")

bs_cliente = bs_data.find_all("cliente")

print(bs_cliente)
print("-------------------------")

for tag in bs_data.find_all('cliente', {'ID': 'C001' }):
    tag['ciudad'] = "Madrid"

print(bs_data.prettify())


"""

from bs4 import BeautifulSoup

with open ("CatalogoProductos.xml","r") as f:
    data = f.read()

bs_data = BeautifulSoup (data, "xml")

for tag in bs_data.find_all("Descripcion"):
    tag["Descripcion"] = tag("Producto")
for tag in bs_data.find_all("Producto",{"ID" : 100001}):
    tag["Precio"] = "9.95"
print (bs_data.prettify())

