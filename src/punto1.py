class Persona:
  #Los atributos que estan fuera del constructor se llaman
  # atributos de clase
  postura = 'Bipedos' # Caracteristicas que TODOS tenemos
  # Esto es un metodo "constructor", viene incorporado en python
  def __init__(self, nombre_introducido, edad_introducida): #Los que tienen doble raya al piso son los de python(metodos dunder)
    self.nombre = nombre_introducido # atributos de instancia, son propios de cada objeto
    self.edad = edad_introducida