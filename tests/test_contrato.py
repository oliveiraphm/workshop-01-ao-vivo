import pytest
from datetime import datetime
from src.contrato import Vendas
from pydantic import ValidationError

def test_vendas_com_dados_validos():
    """
    Testa a criação de uma instância da classe Vendas com dados válidos.

    Este teste verifica se a classe Vendas aceita e armazena corretamente os dados válidos fornecidos.
    Dados válidos incluem um email correto, data atual, valor positivo, nome do produto, quantidade positiva
    e uma categoria existente. O teste confirma se os valores armazenados na instância correspondem aos dados fornecidos.
    """
    dados_validos = {
            "email": "comprador@example.com",
            "data": datetime.now(),
            "valor": 100.50,
            "produto": "Produto X",
            "quantidade": 3,
            "categoria": "categoria3",
        }

    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]