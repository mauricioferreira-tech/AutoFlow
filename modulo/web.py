from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def execultar_automacao():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    time.sleep(2)
    username = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
    login = driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    dados = []

    try:
        limite = int(input("Digite o número de produtos a serem extraídos: "))
    except ValueError:
        print("Entrada inválida. O número de produtos será definido como 10.")
        limite = 10

    for produto in produtos[:limite]:
        nome = produto.find_element(By.CLASS_NAME, "inventory_item_name").text
        preco = produto.find_element(By.CLASS_NAME, "inventory_item_price").text
        dados.append({
        "nome": nome, 
        "preco": preco})

    df = pd.DataFrame(dados)
    df.to_csv("produtos.xlsx", index=False)

def menu():
    print("-" * 30)
    print("AutoFlow")
    print("-" * 30)
    print("1. Executar Automação")
    print("2. Sair")
   
def main():
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            execultar_automacao()
        elif escolha == "2":
            print("Saindo...")
            quit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()