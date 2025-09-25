from PIL import Image, ImageDraw

def criar_imagem_praia(largura = 800, altura = 600):
    """
    Cria uma imagem simples de uma praia com areia e mar.
    """
    # Cria uma nova imagem com fundo branco
    img = Image.new('RGB', (largura, altura), color = 'white')
    draw = ImageDraw.Draw(img)

    # Cores
    cor_areia = (245, 222, 179)  
    cor_agua = (0, 191, 255)     
    cor_ceu = (135, 206, 250)    

    # Desenha o céu 
    draw.rectangle([0, 0, largura, altura // 2], fill=cor_ceu)

    # Desenha o mar
    mar_altura_inicio = altura // 2
    mar_altura_fim = int(altura * 0.75) # 75% da altura total
    draw.rectangle([0, mar_altura_inicio, largura, mar_altura_fim], fill=cor_agua)

    # Desenha a areia
    areia_altura_inicio = int(altura * 0.75) 
    draw.rectangle([0, areia_altura_inicio, largura, altura], fill=cor_areia)

    # Adiciona um sol simples
    cor_sol = (255, 255, 0) 
    raio_sol = min(largura, altura) // 10
    pos_sol_x = largura - raio_sol - 50 
    pos_sol_y = raio_sol + 50
    draw.ellipse([pos_sol_x - raio_sol, pos_sol_y - raio_sol,
                  pos_sol_x + raio_sol, pos_sol_y + raio_sol],
                 fill=cor_sol, outline=cor_sol)

    # Salva a imagem
    nome_arquivo = "praia_simples.png"
    img.save(nome_arquivo)
    print(f"Imagem '{nome_arquivo}' criada com sucesso!")
    return img

if __name__ == "__main__":
    imagem_praia = criar_imagem_praia()
