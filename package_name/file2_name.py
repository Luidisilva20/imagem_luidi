from PIL import Image, ImageDraw
import random

def criar_imagem_cidade(largura=800, altura=600, num_predios=10):
    """
    Cria uma imagem simples de uma cidade com prédios.
    """
    # Cria uma nova imagem com fundo para o céu
    cor_ceu_dia = (135, 206, 235)  
    img = Image.new('RGB', (largura, altura), color = cor_ceu_dia)
    draw = ImageDraw.Draw(img)

    # Cores
    cor_rua = (100, 100, 100)     
    cor_janela = (255, 255, 153)   
    cor_predio_base = (70, 70, 70) 

    # Desenha a rua/chão na parte inferior
    altura_rua = int(altura * 0.25) # 25% da altura para a rua
    draw.rectangle([0, altura - altura_rua, largura, altura], fill=cor_rua)

    # Gera os prédios
    for _ in range(num_predios):
        # Largura aleatória do prédio
        predio_largura = random.randint(largura // 10, largura // 5)
        # Altura aleatória do prédio 
        predio_altura = random.randint(altura // 3, altura - altura_rua - 50)

        # Posição x aleatória do prédio
        predio_x = random.randint(0, largura - predio_largura)
        # Posição y do prédio 
        predio_y = altura - altura_rua - predio_altura

        # Cor aleatória para o prédio 
        r_predio = random.randint(50, 100)
        g_predio = random.randint(50, 100)
        b_predio = random.randint(50, 100)
        cor_predio = (r_predio, g_predio, b_predio)

        # Desenha o corpo do prédio
        draw.rectangle([predio_x, predio_y, predio_x + predio_largura, altura - altura_rua], fill=cor_predio)

        # Adiciona janelas 
        margem_janela = 5
        largura_janela = 15
        altura_janela = 20
        espacamento_janela_x = 25
        espacamento_janela_y = 30

        for y in range(predio_y + margem_janela, altura - altura_rua - altura_janela, espacamento_janela_y):
            for x in range(predio_x + margem_janela, predio_x + predio_largura - largura_janela, espacamento_janela_x):
                # Chance de a janela estar "acesa"
                if random.random() > 0.3: # 70% de chance de luz acesa
                    draw.rectangle([x, y, x + largura_janela, y + altura_janela], fill=cor_janela)
                else: # 30% de chance de janela "apagada" 
                    cor_janela_apagada = (max(0, r_predio-20), max(0, g_predio-20), max(0, b_predio-20))
                    draw.rectangle([x, y, x + largura_janela, y + altura_janela], fill=cor_janela_apagada)


    # Salva a imagem
    nome_arquivo = "cidade_simples.png"
    img.save(nome_arquivo)
    print(f"Imagem '{nome_arquivo}' criada com sucesso!")
    return img

if __name__ == "__main__":
    imagem_cidade = criar_imagem_cidade()
    
