# Criando um catalogo telefonico

catalogo_telefonico = {}

def incluir_contato(catalogo, nome, telefone):
    catalogo[nome] = telefone
    print(f"Contato {nome} com telefone {telefone} incluído com sucesso.")
    
def excluir_contato(catalogo, nome):
    if nome in catalogo:
        del catalogo[nome]
        return f"Contato {nome} excluído com sucesso."
    else:
        return f"Erro: Contato {nome} Não está no catalogo."
    
def pesquisar_contato(catalogo, nome):
    if nome in catalogo:
        return f"O telefone de{nome} e: {catalogo[nome]}"
    else:
        return f"Contatp {nome} não encontrado no catalogo."
    
def imprimir_catalogo(catalogo):
    print("\n--- Catalogo telefônico atual ---")
    if not catalogo:
        print("O catalogo está vazio.")
    else:
        for nome, telefone in catalogo.items():
                print(f"Nome: {nome}, telefone: {telefone}")
    print("-------------------------------\n")
    
print("--- Inicializando o Catálogo ---")
imprimir_catalogo(catalogo_telefonico)

# Incluindo contatos
incluir_contato(catalogo_telefonico, "Alice", "11987654321")
incluir_contato(catalogo_telefonico, "Bob", "21991234567")
incluir_contato(catalogo_telefonico, "Charlie", "31988776655")
imprimir_catalogo(catalogo_telefonico)

# Pesquisando contatos
print(pesquisar_contato(catalogo_telefonico, "Alice"))
print(pesquisar_contato(catalogo_telefonico, "Bob"))
print(pesquisar_contato(catalogo_telefonico, "David")) # Contato que não existe

# Excluindo contatos
print(excluir_contato(catalogo_telefonico, "Bob"))
print(excluir_contato(catalogo_telefonico, "Eva")) # Contato que não existe
imprimir_catalogo(catalogo_telefonico)

# Incluindo mais um para ver o catálogo novamente
incluir_contato(catalogo_telefonico, "Fernanda", "41977778888")
imprimir_catalogo(catalogo_telefonico)

print("--- Fim da Demonstração ---")