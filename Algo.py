from Classe import *

def main():
    while True:
        try:

            menu = int(input("Qual valor deseja? > "))

            match menu:
                case 1:
                        cir = Circulo(int(input("Informe o raio > ")))
                        print(cir.calc_area())

                case 2:
                    cir = Circulo(int(input("Informe o raio > ")))
                    print(cir.calc_circo())

                case 3:
                    para = Paralelepipedo(int(input("Informe o Comprimento > ")), int(input("Informe a Largura > ")), int(input("Informe a Altura > ")))
                    print(para.calc_volume())

                case 0:
                    print("Saindo do software")
                    break

                case _:
                    print("Opção Invalida")
                    
        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)