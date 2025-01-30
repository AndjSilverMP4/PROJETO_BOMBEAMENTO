# Criando função para ciclar um motor

import time
from datetime import datetime, timedelta


class MotorController:
    def __init__(self):
        self.motores = {
            "01": True,  # True indica que o motor está funcionando
            "02": True,
        }
        self.current_motor = "01"
        self.manual_mode = False

    def check_motor_status(self):
        return self.motores[self.current_motor]

    def switch_motor(self):
        if self.current_motor == "01":
            self.current_motor = "02"
        else:
            self.current_motor = "01"

    def run_manual(self):
        while True:
            command = (
                input("Digite 'on' para ligar, 'off' para desligar, 'exit' para sair: ")
                .strip()
                .lower()
            )
            if command == "on":
                self.motores[self.current_motor] = True
                print(f"Motor {self.current_motor} ligado manualmente.")
            elif command == "off":
                self.motores[self.current_motor] = False
                print(f"Motor {self.current_motor} desligado manualmente.")
            elif command == "exit":
                print("Saindo do modo manual.")
                break
            else:
                print("Comando inválido.")

    def run_automatic(self):
        end_time = datetime.now() + timedelta(hours=6)
        while datetime.now() < end_time:
            if not self.check_motor_status():
                print(f"Motor {self.current_motor} falhou. Trocando para o motor.")
                self.switch_motor()
                if not self.check_motor_status():
                    print(
                        f"Motor {self.current_motor} também falhou. Tentando o outro motor novamente."
                    )
                    self.switch_motor()
            print(f"Motor {self.current_motor} está operando.")
            time.sleep(10)  # Ajustar para tempo de verificação desejado


def main():
    controller = MotorController()

    mode = input("Escolha o modo ('manual' ou 'automatic'): ").strip().lower()
    if mode == "manual":
        controller.run_manual()
    elif mode == "automatic":
        controller.run_automatic()
    else:
        print("Modo inválido.")


if __name__ == "__main__":
    main()
