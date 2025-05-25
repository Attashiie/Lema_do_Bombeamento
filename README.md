# Verificador do Lema do Bombeamento

Este projeto implementa um verificador do Lema do Bombeamento para linguagens regulares. Ele permite testar se uma linguagem, definida por uma função Python, pode ser provada como não regular ao tentar violar as condições do lema do bombeamento.

## Funcionalidades

* **Verificação do Lema do Bombeamento**: A função principal `check_pumping_lemma` verifica se uma dada cadeia `w` de uma linguagem `L` (definida por `language_func`) viola o Lema do Bombeamento para um valor `p` específico.
* **Geração de Partições**: O código gera todas as possíveis partições `x`, `y`, `z` da cadeia `w` que satisfazem as condições do lema (`|xy| <= p` e `|y| >= 1`).
* **Teste de Repetição de `y`**: Para cada partição, o código testa a repetição de `y` (`x y^i z`) para diferentes valores de `i` (de 0 até `max_i`).
* **Identificação de Falhas**: Se qualquer uma das cadeias geradas (`x y^i z`) não pertencer à linguagem `L`, uma falha é registrada, indicando uma possível prova de não-regularidade.
* **Interface de Linha de Comando**: O script fornece uma interface simples de linha de comando para que o usuário insira o valor de `p`, a cadeia `w` e o número máximo de repetições `i` a serem testadas.
* **Exemplo Integrado**: Inclui um exemplo da linguagem `L = { a^n b^n | n ≥ 0 }` para demonstração.

## Tecnologias Utilizadas

* **Python 3**: A linguagem de programação principal.
* **`typing`**: Para anotações de tipo.

## Primeiros Passos

### Pré-requisitos

* Python 3.x instalado em seu sistema.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <url_do_repositorio>
    cd <nome_do_repositorio>
    ```
2.  **Certifique-se de que o arquivo Python fornecido (`bombeamento.py`) está no diretório.**

### Executando o Aplicativo

1.  **Execute o script:**
    Abra um terminal ou prompt de comando e execute o script:
    ```bash
    python bombeamento.py
    ```
2.  **Siga as instruções**: O programa solicitará que você insira o valor de bombeamento `p`, a cadeia `w` (que deve pertencer à linguagem e ter comprimento `>= p`), e o número máximo de repetições `i` a serem testadas.

    Exemplo de uso com a linguagem `L = { a^n b^n | n ≥ 0 }`:
    * Informe o valor de bombeamento `p`: `2`
    * Informe a cadeia `w` ∈ `L` com `|w| ≥ p`: `aabb`
    * Máximo de repetições `i` a testar (padrão 3): `3`

    O resultado indicará se a linguagem é "provável que L não seja regular" ou se "não foi possível provar irregularidade" com os valores fornecidos.

## Como Funciona

1.  **Definição da Linguagem**: O usuário define a linguagem `L` através da função `language_func(s: str) -> bool`, que retorna `True` se a cadeia `s` pertence a `L` e `False` caso contrário.
2.  **Verificação de Pré-condições**: A função `check_pumping_lemma` verifica se a cadeia `w` fornecida pertence à linguagem `L` e se seu comprimento é maior ou igual a `p`.
3.  **Particionamento**: O código itera sobre todas as maneiras possíveis de dividir `w` em `x`, `y`, `z` tal que `w = xyz`, `|xy| <= p` e `|y| >= 1`.
4.  **Bombeamento**: Para cada partição `(x, y, z)`, a função testa cadeias `x y^i z` para `i` de 0 até `max_i`.
5.  **Verificação da Linguagem**: Se para alguma partição, uma das cadeias bombeadas `x y^i z` não pertencer a `L`, então essa partição viola o lema.
6.  **Resultado**: Se *todas* as partições possíveis violarem o lema para algum `i`, o programa conclui que a linguagem é "provável que L não seja regular". Caso contrário, não é possível provar a irregularidade com os parâmetros dados.

## Créditos

Desenvolvido por [Attashiie](https://github.com/Attashiie)
