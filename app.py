from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_mexicano.receber_avaliacao('Luiza', 9.5)
restaurante_mexicano.receber_avaliacao('Lucas', 10)

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()