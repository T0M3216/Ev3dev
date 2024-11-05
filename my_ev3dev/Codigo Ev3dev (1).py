import ev3dev.ev3 as ev3

# Configuração dos sensores de cor
sensor_esquerdo = ev3.ColorSensor('in1')
sensor_direito = ev3.ColorSensor('in2')

# Configuração dos motores
motor_esquerdo = ev3.LargeMotor('outA')
motor_direito = ev3.LargeMotor('outD')

while True:
    # Lê os valores dos sensores de cor
    cor_esquerdo = sensor_esquerdo.color
    cor_direito = sensor_direito.color

    # Verifica se ambos os sensores estão vendo preto
    if cor_esquerdo == 1 and cor_direito == 1:
        # Anda para frente
        motor_esquerdo.run_forever(speed=50)
        motor_direito.run_forever(speed=50)

    # Verifica se o sensor esquerdo está vendo preto e o direito está vendo branco
    elif cor_esquerdo == 1 and cor_direito == 6:
        # Vira para a esquerda
        motor_esquerdo.run_forever(speed=-50)
        motor_direito.run_forever(speed=50)

    # Verifica se o sensor direito está vendo preto e o esquerdo está vendo branco
    elif cor_esquerdo == 6 and cor_direito == 1:
        # Vira para a direita
        motor_esquerdo.run_forever(speed=50)
        motor_direito.run_forever(speed=-50)

    # Verifica se o sensor esquerdo está vendo verde
    elif cor_esquerdo == 3:
        # Vira para a esquerda e anda
        motor_esquerdo.run_forever(speed=-50)
        motor_direito.run_forever(speed=50)

    # Verifica se o sensor direito está vendo verde
    elif cor_direito == 3:
        # Vira para a direita e anda
        motor_esquerdo.run_forever(speed=50)
        motor_direito.run_forever(speed=-50)

    # Verifica se ambos os sensores estão vendo verde
    elif cor_esquerdo == 3 and cor_direito == 3:
        # Faz meia volta
        motor_esquerdo.run_forever(speed=-50)
        motor_direito.run_forever(speed=-50)

    # Verifica se ambos os sensores estão vendo preto novamente após fazer meia volta
    elif cor_esquerdo == 1 and cor_direito == 1:
        # Para de fazer meia volta
        motor_esquerdo.stop()
        motor_direito.stop()

    # Se nenhum dos casos acima for verdadeiro, para os motores
    else:
        motor_esquerdo.stop()
        motor_direito.stop()