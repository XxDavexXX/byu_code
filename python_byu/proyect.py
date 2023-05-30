import random

class Escritura:
    def __init__(self, referencia, texto):
        self.referencia = referencia
        self.texto = texto
        self.palabras_ocultas = []

    def ocultar_palabra(self):
        palabras_disponibles = [palabra for palabra in self.texto.split() if palabra not in self.palabras_ocultas]
        if palabras_disponibles:
            palabra_oculta = random.choice(palabras_disponibles)
            self.palabras_ocultas.append(palabra_oculta)

    def esta_completa(self):
        return set(self.texto.split()) == set(self.palabras_ocultas)

    def mostrar_escritura(self):
        texto_oculto = self.texto
        for palabra in self.palabras_ocultas:
            texto_oculto = texto_oculto.replace(palabra, "*" * len(palabra))
        print(f"Referencia: {self.referencia}")
        print(f"Texto: {texto_oculto}")

class Program:
    def __init__(self):
        self.escritura = None

    def guardar_escritura(self, referencia, texto):
        self.escritura = Escritura(referencia, texto)

    def borrar_pantalla(self):
        pass

    def solicitar_input(self):
        return input("Presione Enter para ocultar palabras o escriba 'salir' para terminar: ")

    def run(self):
        self.borrar_pantalla()
        self.escritura.mostrar_escritura()

        while not self.escritura.esta_completa():
            entrada = self.solicitar_input()
            if entrada.lower() == "salir":
                break

            self.escritura.ocultar_palabra()
            self.borrar_pantalla()
            self.escritura.mostrar_escritura()

        print("¡Programa terminado!")

if __name__ == "__main__":
    programa = Program()
    programa.guardar_escritura("Juan 3:16", "Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito")
    programa.run()
