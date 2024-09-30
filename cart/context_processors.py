from .cart import Cart

#  Create context processor so our cart can work on all page
# Crie um processador de contexto para que nosso carrinho possa funcionar em todas as páginas
def cart(request):
    # Return the default data from our Cart
    # Retorne os dados padrão do nosso carrinho
    return {'cart': Cart(request)}