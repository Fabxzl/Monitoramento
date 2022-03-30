import json
import locale
import time
import requests
from datetime import datetime
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")


def logo(titulo):
    print("=" * 80)
    print(figlet_format(text=titulo, font="standard", justify="center"))
    print("=" * 80)


def obter_hora():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
    return data_e_hora_em_texto


def buscar_dados(coin):
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/ticker")
    payload = json.loads(request.content)
    coin = payload['ticker']['last']
    return float(coin)


def calc_porc(anterior, nova):
    anterior = anterior
    nova = nova

    if anterior < nova:
        x = (nova*100.00) / anterior
        x = 100.00 - x
        x = str(x)
        x = x.replace('-', '')
        x = float(x)
        x = round(x, 2)
        x = ("+" + str(x))
        return x

    elif anterior > nova:
        x = (nova*100.00) / anterior
        x = 100.00 - x
        x = str(x)
        x = float(x)
        x = round(x, 2)
        x = ("-" + str(x))
        return x

    else:
        x = ("-%")
        return x


logo("Mercado Bitcoin")
list_btc = [1.00]
list_eth = [1.00]
list_xrp = [1.00]
list_paxg = [1.00]
list_usdc = [1.00]

print(Panel.fit("Desenvolvido por: Fabxzl. \n Versão beta!", ))

while True:
    # Realizando as requisições
    btc = float(buscar_dados("BTC"))
    eth = float(buscar_dados("ETH"))
    xrp = float(buscar_dados("MANA"))
    paxg = float(buscar_dados("CHZ"))
    usdc = float(buscar_dados("SAND"))

    # Armazenando os dados em listas para comparações
    list_btc.append(btc)
    btc = locale.currency(btc, grouping=True)
    list_eth.append(eth)
    eth = locale.currency(eth, grouping=True)
    list_xrp.append(xrp)
    xrp = locale.currency(xrp, grouping=True)
    list_paxg.append(paxg)
    paxg = locale.currency(paxg, grouping=True)
    list_usdc.append(usdc)
    usdc = locale.currency(usdc, grouping=True)

    table = Table(title="")
    table.add_column("Criptomoeda", justify="center", no_wrap=True)
    table.add_column("Valor", justify="center")
    table.add_column("Data/Hora", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Porcentagem", justify="center")

    data_hora = obter_hora()

    # Monitoramento BTC
    if list_btc[-1] > list_btc[-2]:
        if list_btc[-2] == 1.00:
            response = "Calculando..."
        else:
            response = str(calc_porc(list_btc[-2], list_btc[-1]))
        table.add_row(
            "BITCOIN",
            str(btc),
            data_hora,
            "⬆",
            response,
            style="green"
        )
        console = Console()

    elif list_btc[-1] < list_btc[-2]:
        response = str(calc_porc(list_btc[-2], list_btc[-1]))
        table.add_row("BITCOIN", str(btc), data_hora,
                      "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("BITCOIN", str(btc), data_hora, "=", "%", style="yellow")
        console = Console()

    # Monitoramento ETH
    if list_eth[-1] > list_eth[-2]:
        if list_eth[-2] == 1.00:
            response = "Calculando..."
        else:
            response = str(calc_porc(list_eth[-2], list_eth[-1]))
        table.add_row("ETHEREUM", str(eth), data_hora,
                      "⬆", response, style="green")
        console = Console()

    elif list_eth[-1] < list_eth[-2]:
        response = str(calc_porc(list_eth[-2], list_eth[-1]))
        table.add_row("ETHEREUM", str(eth), data_hora,
                      "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("ETHEREUM", str(eth), data_hora,
                      "=", "%", style="yellow")
        console = Console()

    # Monitoramento SAND
    if list_xrp[-1] > list_xrp[-2]:
        if list_xrp[-2] == 1.00:
            response = "Calculando..."
        else:
            response = str(calc_porc(list_xrp[-2], list_xrp[-1]))
        table.add_row("MANA", str(xrp), data_hora, "⬆", response, style="green")
        console = Console()

    elif list_xrp[-1] < list_xrp[-2]:
        response = str(calc_porc(list_xrp[-2], list_xrp[-1]))
        table.add_row("MANA", str(xrp), data_hora, "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("MANA", str(xrp), data_hora, "=", "%", style="yellow")
        console = Console()

    # Monitoramento CHZ
    if list_paxg[-1] > list_paxg[-2]:
        if list_paxg[-2] == 1.00:
            response = "Calculando..."
        else:
            response = str(calc_porc(list_paxg[-2], list_paxg[-1]))
        table.add_row("CHZ", str(paxg), data_hora,
                      "⬆", response, style="green")
        console = Console()

    elif list_paxg[-1] < list_paxg[-2]:
        response = str(calc_porc(list_paxg[-2], list_paxg[-1]))
        table.add_row("CHZ", str(paxg), data_hora, "⬇", response, style="red")
        console = Console()

    else:
        table.add_row("CHZ", str(paxg), data_hora, "=", "%", style="yellow")
        console = Console()

    # Monitoramento SAND
    if list_usdc[-1] > list_usdc[-2]:
        if list_usdc[-2] == 1.00:
            response = "Calculando..."
        else:
            response = str(calc_porc(list_usdc[-2], list_usdc[-1]))
        table.add_row("SAND", str(usdc), data_hora,
                      "⬆", response, style="green")
        console = Console()
        console.print(table)

    elif list_usdc[-1] < list_usdc[-2]:
        response = str(calc_porc(list_usdc[-2], list_usdc[-1]))
        table.add_row("SAND", str(usdc), data_hora, "⬇", response, style="red")
        console = Console()
        console.print(table)

    else:
        table.add_row("SAND", str(usdc), data_hora, "=", "%", style="yellow")
        console = Console()
        console.print(table)

    print("==============================================================================")
    time.sleep(60)