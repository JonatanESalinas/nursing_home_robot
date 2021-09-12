import requests

class Cosa:
    def web(self):
        enviar = requests.get("https://api.thingspeak.com/update?api_key=PK1UENEO00MJXH4R&field1="+ str(37)+"&field2="+ str(95)+"&field3="+ str(110))

if __name__ == '__main__':
    print("Hola")

    una_cosa = Cosa()

    una_cosa.web()