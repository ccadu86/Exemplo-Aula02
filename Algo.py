from Classe import *

def main():
    while True:
        try:
            menu = int(input("Qual valor deseja? > "))

            if menu == 1:
                    cir = Circulo(int(input("Informe o raio > ")))
                    print(cir.calc_area())

            elif menu == 2:
                cir = Circulo(int(input("Informe o raio > ")))
                print(cir.calc_circo())

            elif menu == 3:
                para = Paralelepipedo(int(input("Informe o Comprimento > ")), int(input("Informe a Largura > ")), int(input("Informe a Altura > ")))
                print(para.calc_volume())

            elif menu == 0:
                print("Saindo do software")
                break
                    
        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)