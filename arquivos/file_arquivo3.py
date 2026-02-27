def main():
    print("--- PROGRAMA INICIADO ---")
    print("Digite suas frases. Digite 'sair' para terminar.")

    frases = []

    while True:
        # O input deve estar dentro do while
        entrada = input("> ").strip()

        # O if deve estar EXATAMENTE alinhado abaixo do entrada
        if entrada.lower() == "sair":
            print("Saindo e salvando...")
            break  # Isso quebra o loop while

        frases.append(entrada)

    # Escrita do arquivo
    with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
        for f in frases:
         arquivo.write(f + "\n")

    print("Arquivo salvo. Fim do programa.")


# IMPORTANTE: Sem espaços em "__main__"
if __name__ == "__main__":
    main()
