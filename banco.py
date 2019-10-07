# Linguagem de Programação II
# AC05 ADS2D - Banco
#
# Alunos: guilherme.asantos@aluno.faculdadeimpacta.com.br
#         aluno2.sobrenome@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.
    possui os atributos: nome, telefone e email, todos privados
    caso o email não seja um email válido gera um ValueError,
    caso o telefone não seja um número gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        
            

    def get_nome(self) -> str:
        """Acessor do atributo Nome."""
        return self._nome

    def get_telefone(self) -> int:
        """Acessor do atributo Telefone."""
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        if type(novo_telefone) is not int:
            raise TypeError("Telefone deve ser um número inteiro sem o hifen")
        self._telefone = novo_telefone

    def get_email(self) -> str:
        """Acessor do atributo Email."""
        return self._email
        

    def set_email(self, novo_email: str) -> None:
        """
        Mutador do atributo Email, caso não receba um email válido
        gera um ValueError.
        """
        self.novo_email = list(novo_email)
        if '@' not in self.novo_email:
            raise ValueError('e-mail invalido, tente novamente.')
        self._email = "".join(self.novo_email)



class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    * abre_contas: abre uma nova conta, atribuindo o numero da conta em ordem
    crescente.
    * lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__(self, nome: str):
        self._nome_banco = nome

    def get_nome(self) -> str:
        """Acessor do Atributo Nome."""
        return self._nome_banco

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """
        pass

    def lista_contas(self) -> List['Conta']:
        """Retorna a lista com todas as contas do banco."""
        pass


class Conta():
    """
    Classe Conta.
    * Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito'), 200) etc.
    * Caso o saldo inicial seja menor que zero deve lançar um ValueError
    * A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)
    DICA: Crie uma variável interna privada para guardar as
    operaões feitas na conta
    """

    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        self._clientes = clientes
        self._numero_da_conta = numero_conta
        self._saldo_inicial = saldo_inicial
        self._extrato = []
        if self._saldo_inicial < 0:
            raise ValueError('Não é possivel abrir uma conta com saldo negativo.')
        self._extrato.append(('saldo_inicial', saldo_inicial))

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor para o atributo Clientes
        '''
        return self._clientes
        

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        return self._saldo_inicial

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        return self._numero_da_conta


    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        self.valor = valor
        if self.valor > self._saldo_inicial:
            raise ValueError('Não foi possivel efetuar a operação')
        self._saldo_inicial = self._saldo_inicial - self.valor
        saque = ("saque", self.valor)
        self._extrato.append(saque)
        return self._saldo_inicial
        



    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        self.valor = valor
        self._saldo_inicial = self._saldo_inicial + self.valor
        deposito = ("deposito", self.valor)
        self._extrato.append(deposito)
        return self._saldo_inicial


    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''
        extrato = self._extrato
        return extrato


if __name__ == '__main__':
    cliente = Cliente('Amanda', '999999999', 'email@email')
    conta = Conta([cliente], 1, 1000)
    s = conta.saque(100)
    print(conta.extrato())
    d = conta.deposito(200)
    print(conta.extrato())

    
