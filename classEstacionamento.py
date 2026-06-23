class Estacionamento ():
    def __init__(self, hora_entrada, placa, modelo, cor, tipo):
        self.hora_entrada = hora_entrada
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
        self.tipo = tipo

    def verificar_placa(placa):
        while True:
            if len(placa) != 7:
                print("A placa está incorreta, digite novamente.")

    def verificar_texto (self):
        if self.modelo == "":
            print("Texto vazio")
        