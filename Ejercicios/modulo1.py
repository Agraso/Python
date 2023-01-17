class Coche:
    def __init__ (self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
        
    def mostrar_caracteristicas(self):
        print("Este coche es de la marca {} de color {} con tipo de combustible {} y una cilindrada de {}L"
              .format(self.marca,self.color,self.combustible,self.cilindrada))
        
media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3