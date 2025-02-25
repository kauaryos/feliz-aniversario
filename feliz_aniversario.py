import time

def exibir_mensagem(nome):
    mensagem = f"""
    🎉🎂 Feliz Aniversário, {nome}! 🎂🎉

    Que seu dia seja repleto de alegria, felicidade e muitas conquistas!
    Aproveite cada momento e celebre com quem você ama. 🥳🎁
    """
    for linha in mensagem.split("\n"):
        print(linha)
        time.sleep(0.5)  # Dá um efeito de digitação lenta

if __name__ == "__main__":
    nome = input("Digite o nome do aniversariante: ")
    exibir_mensagem(nome)
