class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

persona1 = Persona("Juan", 25, 1.75)
persona2 = Persona("Ana", 33, 1.68)
persona3 = Persona("Carlos", 21, 1.80)

personas = [persona1, persona2, persona3]

def persona_mas_alta(personas):
    return max(personas, key=lambda persona: persona.altura)

def persona_mayor_edad(personas):
    return max(personas, key=lambda persona: persona.edad)

mas_alta = persona_mas_alta(personas)
mayor_edad = persona_mayor_edad(personas)

print(f"La persona más alta es {mas_alta.nombre} con una altura de {mas_alta.altura} metros.")
print(f"La persona de mayor edad es {mayor_edad.nombre} con {mayor_edad.edad} años.")