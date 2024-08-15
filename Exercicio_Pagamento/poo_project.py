'''Usando o método de abstração'''
from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass


class CartaoCredito(Pagamento):
    def __init__(self, numero_cartao, titular, validae, cvv):
         self.numero_cartao = numero_cartao
         self.titular = titular
         self.validade = validae
         self.cvv = cvv

    def processar_pagamento(self, valor):
        return f"Pagamento de {valor} processado com cartão de crédito."


class PicPay(Pagamento):
    def __init__(self, email):
        self.email = email

    def processar_pagamento(self, valor):
        return f"Pagamento de {valor} processado com PicPay"
    
def realizar_pagamento(metodo_pagamento, valor):
    print(metodo_pagamento.processar_pagamento(valor))

cartao = CartaoCredito("1234 5678 9012 3456", "João Silva", "12/25", "123")
picpay = PicPay("xaolimmatadordeporco@gmail.com")

realizar_pagamento(cartao,   1500.00)
realizar_pagamento(picpay,   500.00)

