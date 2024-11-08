class Tamagotchi:
    def __init__(self, nome:str, tipo:str, vida_maxima: int, energia_max:int):
        self.nome = nome
        self.tipo = tipo
        self.vida_maxima = vida_maxima
        self.energia_max = energia_max
        self.vida_atual = vida_maxima
        self.energia_atual = energia_max



    def brincar(self):
        if self.energia_atual > 30:
            self.energia_atual -= 30
            return f"O {self.nome} está brincado!"
        else:
            return f"{self.nome} não tem energia suficiente para brincar"

    def comer(self):
        if self.energia_atual + 20 <= self.energia_max:
            self.energia_atual += 20
            return f"O {self.nome} comeu!"
        else:
            self.energia_atual = self.energia_max
            return f"O {self.nome} já está cheio!"

    def trabalhar(self):
        if self.energia_atual >= 50:
            self.energia_atual -= 50
            return f"O {self.nome} Trabalhou!"
        else:
            return f"O {self.nome} está cansado e não pode trabalhar no momento!"
    
    def dormir(self):
        if self.energia_atual + 50 <= self.energia_max:
            self.energia_atual += 50
            return f"O {self.nome} dormiu!"
        else:
            return f"{self.nome} está com mt enertfia e não pode dormir!"
        
    def lutar(self):
        if self.energia_atual > 20:
            if self.vida_atual > 15:
                self.energia_atual -= 20
                self.vida_atual -= 15
                return f"O {self.nome} lutou."
            else:
                return f"O {self.nome} está com a vida baixa."
        else:
            return f"O {self.nome} está com a energia baixa."

    def irEnfermaria(self):
        self.energia_atual = self.energia_max
        self.vida_atual = self.vida_max
        return f"O {self.nome} está totalmente recuperado."


    
tamagotchi1 = Tamagotchi(nome="CR7", tipo="Macaco", vida_maxima=200, energia_max=150)

while True:
    menu = input(F"""
    Vida: {tamagotchi1.vida_atual}
    Energia: {tamagotchi1.energia_atual}
    Escolha uma opção:
    1 - Comer
    2 - Brincar
    3 - Dormir
    4 - Trabalhar
    5 - Lutar
    6 - Ir na Enfermaria
    0 - Sair
    """)

    match menu:
        case "1":
            print(tamagotchi1.comer())
        case "2":
            print(tamagotchi1.brincar())
        case "3":
            print(tamagotchi1.dormir())
        case "4":
            print(tamagotchi1.trabalhar())
        case "5":
            print(tamagotchi1.lutar())
        case "6":
            print(tamagotchi1.irEnfermaria())
        case "0":
            print("Fim de Jogo")
            break
        case _:
            print("Opção inválida")



