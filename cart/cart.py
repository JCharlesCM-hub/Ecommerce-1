
class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # get the current session key if it exists
        # obter a chave de sessão atual se existir
        cart = self.session.get('session_key')
        
        # if se user is new, no session key! create one!
        # se o usuário for novo, nenhuma chave de sessão! crie uma!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # Make sure cart is available on all pages of site
        # Certifique-se de que o carrinho esteja disponível em todas as páginas do site
        self.cart = cart





