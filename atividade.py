class Historico:
    def __init__(self):
        self.pedidos = []
        
    def inserir_pedido(self, pedido):
        self.pedidos.append(pedido)

    def calcular_faturamento(self):
        soma = 0
        for pedido in self.pedidos:  
            soma += pedido.valor_final_da_placa
        return soma


class Cliente:
    def __init__(self,nome: str, telefone: str, endereco):

        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco




class Endereco:
    def __init__(self,rua: str, numero: str, complemento: str, bairro: str,
     cidade: str, uf: str, cep: str):

        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep  = cep




class Pedido:
    def __init__(self,cliente,altura: float, largura: float, frase: str , cor_placa: str,
                 cor_letra: str, valor_fixo_material: float = 172.00 ,valor_fixo_letra: float = 0.55):
       
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.valor_fixo_material = valor_fixo_material
        self.valor_fixo_letra = valor_fixo_letra

    def calcular_total(self):
        self.area = self.altura * self.largura
        self.custo_do_material = self.area * self.valor_fixo_material
        self.custo_do_desenho = self.valor_fixo_letra * len(self.frase.replace(" ", "")) 
        self.valor_final_da_placa = self.custo_do_material + self.custo_do_desenho
        return self.valor_final_da_placa



