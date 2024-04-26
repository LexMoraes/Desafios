def qtde_leds(num):
    # Lista dicionario com a quantidade de leds(valor) para cada número informado(chave)
    led_count = {
        '1': 2,  # Um led para o segmento superior e outro para o inferior
        '2': 5,  # Cinco leds: dois superiores, dois inferiores e um central
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6,
        '0': 6
    }

    total_leds = 0
    for digito in str(num):
        total_leds += led_count[digito]

    return total_leds

# Leitura do número de casos de teste
N = int(input("Digite o valor que João quer exibir nos leds"))

for _ in range(1):
    value = 0
    leds_necessarias = qtde_leds(value)
    print(f"{leds_necessarias} leds")