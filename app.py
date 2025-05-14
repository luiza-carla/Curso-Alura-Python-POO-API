from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

bebida_suco = Bebida('Suco de Morango', 5.0, 'grande')
prato_pao = Prato('Pão', 2.0, 'pão recheado')
sobremesa_pudim = Sobremesa('Pudim', 10, 'Sobremesa de leite condensado')
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
sobremesa_pudim.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)

# restaurante_mexicano.receber_avaliacao('Luiza', 9.5)
# restaurante_mexicano.receber_avaliacao('Lucas', 10)
# restaurante_mexicano.alternar_estado()

def main():
    # Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()