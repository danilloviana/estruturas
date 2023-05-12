#Classe Livro
class Livro:

    def __init__(self, titulo , autor ,quantidadepag,):
        self.titulo = titulo
        self.autor = autor
        self.quantidadepag = quantidadepag


    def exibir_informacoes_da_tv(self):
        return(self.titulo , self.autor ,self.quantdadedepag)

