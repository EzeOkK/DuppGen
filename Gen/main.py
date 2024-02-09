import os
import json
from datetime import datetime
from time import sleep, time
from concurrent.futures import ThreadPoolExecutor as executor

from timezone import tzFilter

try:
    from aminofix import Client, SubClient
except:
    os.system("pip install amino.fix json_minify")
    from aminofix import Client, SubClient

    os.system("clear")


# |  ------SCRIPT FEITO POR @elnescau_ ------  |
#
# |POR FAVOR, NÃO ALTERE OU MODIFIQUE NADA  NO|
# |SCRIPT, RISCO DO SCRIPT DEIXAR DE FUNCIONAR|

comunidades = [
    "http://aminoapps.com/c/AminoCoinsDreaming",
    "http://aminoapps.com/c/NarutoRpgShi492"
]


class app:
    def __init__(self):  # carrega as informações necessárias

        self.pfx = "\033[1;97;40m"
        self.sfx = "\033[1;30;107m"
        self.vrm = "\033[1;31m"
        self.brc = "\033[1;97m"
        self.marca = "[DUPP]"
        self.r = "\033[m"
        self.client = Client()

        print(f"{self.pfx} x Ranking    {self.sfx} x By @elnescau_ {self.r}\n")
        while True:
            try:
                with open("info.json", 'r') as x:
                    acc = json.load(x)
                    self.email = acc["email"]
                    self.password = acc["password"]
                    print(f"{self.pfx} x Informações  {self.sfx} OK {self.r}")
                    sleep(2)
                    self.clear()
                break

            except:
                email = input("email: ")
                password = input("password: ")
                info = f'{{"email": "{email}", "password": "{password}"}}'
                with open("info.json", 'w') as x:
                    x.write(info)
                    print(f"\n{self.pfx} x Conta salva com sucesso! {self.sfx} OK {self.r}")
                    sleep(2)
                    self.clear()
        self.run_forever()

    def auth(self, client: Client, email, password):  # Faz o login na conta!
        try:
            client.login(email, password)
        except Exception as e:
            print(e)
            print(f"{self.pfx} x [DUPP] Login {self.sfx} - 3RR0R {self.r}")
            exit()

    def send_minutes(self, comId, client: Client):  # Envia objetos ativos a API
        sbc = SubClient(
            comId=comId, profile=client.profile
        )
        timers = [{'start': int(time() * 1000), 'end': int(time() * 1000) + 300} for _ in range(13)]
        tz = tzFilter()
        response = sbc.send_active_obj(
            timers=timers, tz=tz, 
            timestamp=int(time() * 1000)
        )
        #print(response['api:message'])
        return response.json()

    def run(self):
        global comunidades
        
        device = "196E66012576DEC9F1FDF3885FDDC2B4D8EB3F5DC559A4A05FABDD88F0674E82B54B26F9F423CFC74F"
        self.client = Client(device)

        self.auth(self.client, self.email, self.password)
        print(f"{self.pfx} x Login {self.sfx} - OK {self.r}\n")
        for comunidade in comunidades:
            comId = self.client.get_from_code(comunidade).comId
            print(f"\n{comunidade}")
            for i in range(5):
                """executor(max_workers=100).submit(
                    self.send_minutes, 
                    comId, 
                    self.client
                )"""
                
                response = self.send_minutes(comId, self.client)
                #self.send_minutes(comId, self.client)
                print(f"{self.pfx} x [DUPP] Adicionando minutos {self.sfx} - {response['api:message']}{self.r}")
                sleep(1.5)
        self.client.logout()
        print(f"\n{self.pfx} x [DUPP] Minutos adicionandos com sucesso! {self.sfx} - OK {self.r}")

    def clear(self):  # Limpa a tela do terminal
        os.system("clear")
        
    def run_forever(self):
        ciclo = 1
        
        self.run()
        
        print(f"\033[1;31mAguardando a proxima hora...\n\n")
        
        while True:
            reset = "01:00"
            time_now = datetime.now().strftime("%M:%S")
            
            if time_now == reset:
                self.run()
                
                print(f"\n\033[1;31mciclo {ciclo} - Aguardando a proxima hora...\n\n")
                
                ciclo += 1
                
            sleep(1)


if __name__ == "__main__":
    app()
    
    
