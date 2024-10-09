from store.models import Product

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


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)          

        self.session.modified = True


    def cart_total(self):
        # Get product IDDS
        product_ids = self.cart.keys()
        # Lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # Start counting at 0
        total = 0

        for key, value in quantities.items():
            # Convert key string into into so can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
            
            return total


    def __len__(self):
        return len(self.cart)
    

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)

        # Return those looked up products
        return products


    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # Get cart
        ourcart = self.cart
        # Update Dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    

    def delete(self, product):
        product_id = str(product)

        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


