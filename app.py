# Crie um programa que calcule o IMC do usuário, em Flet

import flet as ft

def main(page: ft.Page):
    def calcular_imc(e):
        try:
            peso = float(peso_input.value)
            altura = float(altura_input.value) / 100 # Convertendo altura para metros
            imc = peso / (altura ** 2)
            resultado_text.value = f"Seu IMC é: {imc:.2f}"
        except ValueError:
            resultado_text.value = "Por favor, insira valores válidos."
        resultado_text.update()

    # Criando os campos de entrada e o botão
    peso_input = ft.TextField(label="Peso (kg)", width=200)
    altura_input = ft.TextField(label="Altura (cm)", width=200)
    calcular_button = ft.ElevatedButton(text="Calcular IMC", on_click=calcular_imc)
    resultado_text = ft.Text()

    # Adicionando os elementos à página
    page.add(ft.Text("Calculadora de IMC", size=20, weight="bold"), peso_input, altura_input, calcular_button, resultado_text)

# Iniciar a aplicação
ft.app(target=main)
