import subprocess
import platform
import random

def limpar_tela():
    sistema = platform.system()
    if sistema =="Windows":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"])
while True:
    limpar_tela()
    print(r'''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Bem-vindo à Ilha do Tesouro.")
    print("Sua missão é encontrar o tesouro.")
    # Aqui definimos as respostas certas de forma aleatória
    caminho_certo = random.choice(["left", "right"])
    acao_certa = random.choice(["swim", "wait"])
    porta_certa = random.choice(["red", "blue", "yellow"])

    escolha1 = ""
    while escolha1 not in ["left", "right"]:
        escolha1 = input("Esquerda (left) ou Direita (right)? ").lower().strip()
        if escolha1 not in ["left", "right"]:
            print("Opção inválida! Digite apenas 'left' or 'right'.")

    if escolha1 == caminho_certo:
        print("Você avançou!")
        escolha2 = ""
        while escolha2 not in ["swim", "wait"]:
            escolha2 = input("Nadar (swim) ou Esperar (wait)? ").lower().strip()
            if escolha2 not in ["swim", "wait"]:
                print("Opção inválida! Digite apenas 'swim' or 'wait'.")

        if escolha2 == acao_certa:
            print("Você chegou na porta!")
            escolha3 = ""
            while escolha3 not in ["red", "blue", "yellow"]:
                escolha3 = input("Qual porta? Red, Blue ou Yellow? ").lower().strip()
                if escolha3 not in ["red", "blue", "yellow"]:
                    print("Opção inválida! Escolha a cor da porta.")

            if escolha3 == porta_certa:
                print("Você achou o tesouro!\n")
                print('''    __________________________
       |OFFo oON                  |
       | .----------------------. |
       | |  .----------------.  | |
       | |  |                |  | |
       | |))|                |  | |
       | |  |                |  | |
       | |  |                |  | |
       | |  |                |  | |
       | |  |                |  | |
       | |  |                |  | |
       | |  '----------------'  | |
       | |__GAME BOY____________/ |
       |          ________        |
       |    .    (Nintendo)       |
       |  _| |_   """"""""   .-.  |
       |-[_   _]-       .-. (   ) |
       |   |_|         (   ) '-'  |
       |    '           '-'   A   |
       |                 B        |
       |          ___   ___       |
       |         (___) (___)  ,., |
       |        select start ;:;: |
       |                    ,;:;' /
    jgs|                   ,:;:'.'
       '-----------------------`
    ''')
            else:
                print("Porta errada. Game Over!")
        else:
            print("Ação errada. Game Over!")
    else:
        print("Caminho errado. Game Over")
    jogar_novamente = input("\nQuer tentar de novo? (S/N): ").lower().strip()
    if jogar_novamente != "s":
        print("Obrigado por jogar!")
        break
