# Função para cadastrar livro de acordo com seu estilo
def cadastrar_livro():
    print("Bem-vindo à Biblioteca!")
    print("Escolha uma categoria:")
    print("1. Placa de vídeo")
    print("2. Memória RAM")
    print("3. Placa mãe")
    print("4. Monitor")
    
    categoria = input("Digite o número da categoria desejada: ")

    if categoria == "1":
        categoria_nome = "Placa de vídeo"
    elif categoria == "2":
        categoria_nome = "Memória RAM"
    elif categoria == "3":
        categoria_nome = "Placa mãe"
    elif categoria == "4":
        categoria_nome = "Monitor"
    else:
        print("Categoria inválida! Tente novamente.")
        return cadastrar_livro()  # Chama novamente a função se a categoria for inválida

    titulo = input(f"Digite o título do livro de {categoria_nome}: ")
    autor = input(f"Digite o nome do autor do livro de {categoria_nome}: ")
    
    # Exibe a confirmação do cadastro com a categoria, título e autor do livro
    print(f"Livro cadastrado com sucesso! Categoria: {categoria_nome} | Título: {titulo} | Autor: {autor}")

# Função principal que gerencia o sistema
def sistema_biblioteca():
    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Cadastrar livro")
        print("2. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            print("Saindo do sistema da biblioteca...")
            break  # Encerra o programa
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o sistema
sistema_biblioteca()
