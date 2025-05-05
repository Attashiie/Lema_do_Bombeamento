from typing import Callable, List, Tuple


def check_pumping_lemma(
    language_func: Callable[[str], bool],
    p: int,
    w: str,
    max_i: int = 3
) -> Tuple[bool, List[Tuple[str, str, str, int]]]:
    """
    Verifica o lema do bombeamento para linguagem L definida por language_func.

    Argumentos:
      language_func: função que retorna True se uma cadeia pertence à L.
      p: valor de bombeamento (int).
      w: cadeia de entrada (|w| ≥ p) que deve pertencer a L.
      max_i: máximo de repetições de y a testar (padrão 3).

    Retorna:
      - is_nonregular: True se **todas** as partições x,y,z violam o lema (L não é regular).
      - failures: lista de tuplas (x, y, z, i) que mostram falha para cada partição.
    """
    n = len(w)
    # Verifica pré-condições do lema: w em L e tamanho suficiente
    if not language_func(w):
        raise ValueError("A cadeia w não pertence à linguagem L.")
    if n < p:
        raise ValueError("Tamanho de w menor que p. Escolha outra cadeia com |w| ≥ p.")

    all_partitions_fail = True
    failure_details: List[Tuple[str, str, str, int]] = []

    # O lema garante que w = x + y + z, com |xy| <= p e |y| >= 1.
    # Vamos gerar todas as possibilidades de x_end e y_end para fatiar w em x, y, z.
    # x_end define o ponto onde x termina: x = w[0:x_end]
    # y_end define o ponto onde y termina: y = w[x_end:y_end]
    # e z é o resto: z = w[y_end:]
    for x_end in range(0, p + 1):      # x pode ter tamanho de 0 até p
        for y_end in range(x_end + 1, p + 1):  # y tem pelo menos 1 símbolo, e x+y até p
            x = w[:x_end]   # parte inicial de comprimento x_end
            y = w[x_end:y_end]  # parte seguinte de comprimento y_end - x_end
            z = w[y_end:]   # resto da cadeia após y

            # Agora testamos repetir y para diferentes valores de i:
            # i=0 (remove y), i=1 (origem), i=2, ... até max_i
            for i in range(0, max_i + 1):
                candidate = x + y * i + z
                # Se ao repetir y a cadeia sai de L, temos uma falha (prova de não regularidade)
                if not language_func(candidate):
                    failure_details.append((x, y, z, i))
                    # Não precisamos testar valores maiores de i para essa partição
                    break
            else:
                # Se nunca houve break, encontramos um i que manteve a cadeia em L
                # Logo, essa partição não prova a não-regularidade
                all_partitions_fail = False

    return all_partitions_fail, failure_details


def main():
    print("=== Verificador do Lema do Bombeamento ===")
    # Exemplo de linguagem L = { a^n b^n | n ≥ 0 }
    def language_func(s: str) -> bool:
        count_a = s.count('a')
        count_b = s.count('b')
        # Verifica se s consiste em 'a'*n seguido de 'b'*n
        return s == 'a'*count_a + 'b'*count_b and count_a == count_b

    try:
        p = int(input("Informe o valor de bombeamento p (inteiro ≥ 1): "))
        w = input("Informe a cadeia w ∈ L com |w| ≥ p: ").strip()
        max_i = int(input("Máximo de repetições i a testar (padrão 3): ") or 3)

        is_nonreg, details = check_pumping_lemma(language_func, p, w, max_i)

        if is_nonreg:
            print(f"\nProvável que L não seja regular (todas as divisões quebraram o lema para p={p}).")
            print("Divisões e valores de i que geraram cadeias fora de L:")
            for x, y, z, i in details:
                print(f"  x='{x}', y='{y}', z='{z}', i={i}")
        else:
            print("\nNão foi possível provar irregularidade de L com os valores informados.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
