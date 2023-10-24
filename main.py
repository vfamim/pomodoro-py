# TODO: Criar um contador de acordo com o tempo
import time


def counter_time(minute):
    start = time.time()
    while True:
        elapsed = time.time() - start
        if elapsed >= 60 * minute:
            print('Fim da contagem')
            break
        time.sleep(60)


def pomodoro_exec():
    while True:
        input_minutes = input('Quantos minutos? ')
        try:
            value = int(input_minutes)
            counter_time(value)
            break
        except ValueError:
            print('Escolha um número inteiro, plz.')


def exec_pomodoro():
    while True:
        print('Contando tempo.')
        pomodoro_exec()
        answer_1 = input('Deseja continuar? (s/n) ')
        if answer_1.lower() == 's':
            pass
        elif answer_1.lower() == 'n':
            print('Encerrando aplicação.')
            break
        else:
            print('Escolha entre "s" e "n".')


if __name__ == '__main__':
    exec_pomodoro()
