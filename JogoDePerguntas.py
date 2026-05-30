import random

pontos: int = 0

perguntas: int = random.randrange(1,10)

usuarioCadastrado: str = "Nickolas"
senhaCadastrada: str = "trote"


def IniciarJogo():

    contador: int = 5

    global pontos

    respotasIncorretas: int = 0

    print("\n--- JOGO DO CONHECIMENTO ---\n")


    while contador > 0:

        perguntas: int = random.randrange(1,10)
        
        respotasIncorretas = respotasIncorretas
            
        match perguntas:
                  
                case 1:
            
                    pergunta = str(input('''O que é um algoritmo em programação?\n
                    \na) Um erro que impede o programa de rodar.
                    \nb) Uma sequência de passos lógicos e finitos para resolver um problema.
                    \nc) Um aparelho eletrônico usado para armazenar dados.
                    \nd) Uma linguagem de programação exclusiva para jogos.
                    \n --> DIGITE AQUI: ''')).upper()
            
                    if pergunta != "B":

                        print("\nResposta Errada !!\n")
                        respotasIncorretas = respotasIncorretas + 1
                        
                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:
                            pontos = pontos - 10
                            
                    
            
                    else:

                        print("\nResposta Correta\n")
                        pontos = pontos + 50
                    
                case 2:
                    
                    pergunta = str(input('''Qual é o principal objetivo de uma "variável" em um código?\n
                    \na) Armazenar temporariamente dados ou valores na memória do computador. 
                    \nb) Deixar o código mais longo e difícil de ler.
                    \nc) Conectar o computador à internet.
                    \nd) Excluir arquivos do sistema operacional.
                    \n --> DIGITE AQUI: ''')).upper()

                    if pergunta != "A":
                    
                        print("\nResposta Errada !!\n")
                        respotasIncorretas = respotasIncorretas + 1
                        
                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:
                            pontos = pontos - 10
                            
                    
                    else:
                    
                        print("\nResposta Correta !!\n")
                        pontos = pontos + 50



                case 3:

                    pergunta = str(input('''Em linguagens de programação, qual operador matemático é geralmente usado para multiplicar dois números?\n
                    \na) X
                    \nb) *
                    \nc) %
                    \nd) / 
                    \n --> DIGITE AQUI: ''')).upper()

                    if pergunta != "B":
                    
                        print("\nResposta Errada !!\n")
                        respotasIncorretas = respotasIncorretas + 1
                        
                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:
                            pontos = pontos - 10
                            
                        
                    
                    else:
                    
                        print("\nResposta Correta !!\n")
                        pontos += 50
                
                case 4:

                    pergunta = str(input('''Quando queremos que o nosso programa tome uma decisão (ex: "Se a senha estiver correta, entre; senão, dê um aviso"), qual estrutura devemos usar?\n
                    \na) Laço de Repetição (Loop).
                    \nb) Variável de Texto.
                    \nc) Estrutura Condicional (Se/Então).
                    \nd) Comentário.
                    \n --> DIGITE AQUI: ''')).upper()

                    if pergunta != "C":

                        print("\nResposta Errada !!\n")
                        respotasIncorretas = respotasIncorretas + 1

                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:

                            pontos = pontos - 10
                            
                    
                    else:

                        print("\nResposta Correta !!\n")

                        pontos += 50
                
                case 5:

                    pergunta = str(input('''Se você precisar que um personagem do seu jogo ande 10 passos para frente, repetindo essa ação 5 vezes, qual estrutura de programação é a mais indicada?\n
                    \na) Estrutura condicional.
                    \nb) Laço de repetição (Loop). 
                    \nc) Declaração de variável.
                    \nd) Biblioteca de áudio.
                    \n --> DIGITE AQUI: ''')).upper()
                
                    if pergunta != "B":

                        print("\nResposta Errada !!\n")

                        respotasIncorretas = respotasIncorretas + 1

                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:

                            pontos = pontos - 10
                            
                    
                    else:

                        print("\nResposta Correta !!\n")

                        pontos += 50
                
                case 6:

                    pergunta = str(input('''O que é um "Bug" no mundo da programação?\n
                    \na) Um animal de estimação do programador.
                    \nb) Uma parte muito importante da tela do jogo.
                    \nc) Um erro ou falha no código que faz o programa se comportar de forma inesperada.
                    \nd) O ato de salvar o seu jogo
                    \n --> DIGITE AQUI: ''')).upper()

                    if pergunta != "C":

                        print("\nResposta Errada !!\n")

                        respotasIncorretas = respotasIncorretas + 1

                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:

                            pontos = pontos - 10
                            
                    
                    else:

                        print("\nResposta Correta !!\n")

                        pontos += 50
                
                case 7:

                    pergunta = str(input('''Em programação, o que é um "Comentário"?\n
                    \na) Uma parte do código que é ignorada pelo computador e serve para os humanos lerem e entenderem o código.
                    \nb) Uma mensagem de erro que aparece na tela.
                    \nc) Um comando que desliga o computador.
                    \nd) Um código malicioso que rouba dados.
                    \n --> DIGITE AQUI: ''')).upper()

                    if  pergunta != "A":

                        respotasIncorretas = respotasIncorretas + 1

                        print("\nResposta Errada !!\n")
                        if pontos <= 0:
                            pontos = 0
                            
                        
                        else:
                            pontos = pontos - 10
                            
                    
                    else:
                        print("\nResposta Correta !!\n")

                        pontos += 50
                case 8:
                    
                    pergunta = str(input('''Qual das alternativas representa um "Dado do tipo Inteiro" (Integer)?\n
                    \na) "Olá, Mundo!"
                    \nb) 3.14
                    \nc) 42
                    \nd) Verdadeiro / Falso
                    \n --> DIGITE AQUI: ''')).upper()

                    if pergunta != "C":

                        respotasIncorretas = respotasIncorretas + 1

                        print("\nResposta Errada !!\n")
                        if pontos <= 0:
                            pontos = 0
                            
                        
                        else:
                            pontos = pontos - 10
                            
                    
                    else:

                        print("\nResposta Correta !!\n")

                        pontos += 50
                                        
                
                case 9:
                    
                    pergunta = str(input('''Para que serve o sinal de (igual) na maioria das linguagens de programação?\n
                    \na) Para comparar se dois valores são idênticos.
                    \nb) Para encerrar o programa.
                    \nc) Para atribuir um valor a uma variável.
                    \nd) Para somar dois valores
                    \n --> DIGITE AQUI: ''')).upper()

                    if pergunta != "C":

                        print("\nResposta Errada !!\n")

                        respotasIncorretas = respotasIncorretas + 1

                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:

                            pontos = pontos - 10
                            
                    
                    else:

                        print("\nResposta Correta !!\n")

                        pontos += 50

                
                case 10: 

                    pergunta = str(input('''Qual destas opções NÃO é uma linguagem de programação?\n
                    \na) Python
                    \nb) JavaScript
                    \nc) HTML (Nota: HTML é uma linguagem de marcação, não de programação)
                    \nd) C++
                    \n --> DIGITE AQUI: ''')).upper()

                    if pergunta != "C":

                        print("\nResposta Errada !!\n")

                        respotasIncorretas = respotasIncorretas + 1

                        if pontos <= 0:

                            pontos = 0
                            
                        
                        else:

                            pontos = pontos - 10
                            
                    
                    else:

                        print("\nResposta Correta !!\n")

                        pontos += 50
            
        contador = contador - 1

    print(f"Total De Erros {respotasIncorretas}")

def VerPontuacao():

    print(f"Pontuação Atual {pontos}")

def Menu():

    while True:

        opcao = str(input('''Selecione a opção desejada
                            A - Iniciar Jogo
                            B - Ver Pontuação
                            X - Encerrar
                            --> ''')).upper()
        
        match opcao:
            case "A":
                IniciarJogo()
            
            case "B":

                VerPontuacao()
            
            case "X":

                print("ENCERRANDO...")
                break
            
            case _:

                print("Opção Inválida...")

def Login():

    global usuarioCadastrado
    global senhaCadastrada

    contador: int = 3

    while contador > 0:

        usuario = str(input("Informe O seu Usuario: "))
        senha = str(input("Informe Sua Senha: "))

        if usuario == usuarioCadastrado and senha == senhaCadastrada:

            Menu()
            break
        
        elif (usuario != usuarioCadastrado or senha != senhaCadastrada) and (contador == 1):
            
            print("Tentativas Excedidas")
            print("ENCERRANDO...")

        else:
            print("Usuario Ou Senha Incorretos")
         
            print("Tente Novamente...")
    
        contador = contador - 1


Login()
