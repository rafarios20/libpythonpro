import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'rafaelsrios12@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(destinatario,
                    'rafaelsrios12@hotmail.com',
                    'Cursos Python Pro',
                    'Primeiro teste de spam'
    )
    assert destinatario in resultado
