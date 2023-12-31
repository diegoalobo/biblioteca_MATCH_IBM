import tkinter as tk

class Livro:
    def __init__(self, titulo, autor, exemplares_disponiveis):
        self.titulo = titulo
        self.autor = autor
        if exemplares_disponiveis > 0:
            self.exemplares_disponiveis = exemplares_disponiveis
        else:
            raise ValueError("O número de exemplares disponíveis deve ser maior que zero.")

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Exemplares Disponíveis: {self.exemplares_disponiveis}'

class Catalogo:
    def __init(self):
        self.catalogo = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def listar_livros(self):
        return self.catalogo

    def pesquisar_livros(self, termo):
        resultados = []
        for livro in self.catalogo:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower():
                resultados.append(livro)
        return resultados

    def salvar_catalogo(self, filename):
        with open(filename, 'w') as file:
            for livro in self.catalogo:
                file.write(f'{livro.titulo},{livro.autor},{livro.exemplares_disponiveis}\n')

    def carregar_catalogo(self, filename):
        self.catalogo = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    titulo, autor, exemplares = line.strip().split(',')
                    exemplares = int(exemplares)
                    livro = Livro(titulo, autor, exemplares)
                    self.adicionar_livro(livro)
        except FileNotFoundError:
            pass

def adicionar_livro():
    titulo = titulo_entry.get()
    autor = autor_entry.get()
    exemplares = exemplares_entry.get()
    try:
        exemplares = int(exemplares)
        livro = Livro(titulo, autor, exemplares)
        catalogo.adicionar_livro(livro)
        resultado_label.config(text="Livro adicionado com sucesso!")
    except ValueError:
        resultado_label.config(text="Número de exemplares inválido!")

def pesquisar_livros():
    termo = pesquisa_entry.get()
    resultados = catalogo.pesquisar_livros(termo)
    resultado_listbox.delete(0, tk.END)
    if resultados:
        for livro in resultados:
            resultado_listbox.insert(tk.END, str(livro))
    else:
        resultado_listbox.insert(tk.END, "Nenhum livro encontrado para o termo de pesquisa.")

def salvar_catalogo():
    catalogo.salvar_catalogo('catalogo.txt')
    resultado_label.config(text="Catálogo salvo com sucesso!")

# Criar um catálogo e carregar dados, se houver
catalogo = Catalogo()
catalogo.carregar_catalogo('catalogo.txt')

# Configurar a interface gráfica
root = tk.Tk()
root.title("Catálogo de Livros")

frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)
frame_pesquisar = tk.Frame(root)
frame_pesquisar.pack(pady=10)

titulo_label = tk.Label(frame_adicionar, text="Título:")
autor_label = tk.Label(frame_adicionar, text="Autor:")
exemplares_label = tk.Label(frame_adicionar, text="Exemplares:")
titulo_entry = tk.Entry(frame_adicionar)
autor_entry = tk.Entry(frame_adicionar)
exemplares_entry = tk.Entry(frame_adicionar)
adicionar_button = tk.Button(frame_adicionar, text="Adicionar Livro", command=adicionar_livro)
resultado_label = tk.Label(frame_adicionar, text="")

pesquisa_label = tk.Label(frame_pesquisar, text="Pesquisar por Título ou Autor:")
pesquisa_entry = tk.Entry(frame_pesquisar)
pesquisar_button = tk.Button(frame_pesquisar, text="Pesquisar Livros", command=pesquisar_livros)
resultado_listbox = tk.Listbox(frame_pesquisar, width=100, height=10)

salvar_catalogo_button = tk.Button(root, text="Salvar Catálogo", command=salvar_catalogo)

titulo_label.grid(row=0, column=0)
autor_label.grid(row=1, column=0)
exemplares_label.grid(row=2, column=0)
titulo_entry.grid(row=0, column=1)
autor_entry.grid(row=1, column=1)
exemplares_entry.grid(row=2, column=1)
adicionar_button.grid(row=3, column=0, columnspan=2)
resultado_label.grid(row=4, column=0, columnspan=2)

pesquisa_label.grid(row=0, column=0)
pesquisa_entry.grid(row=0, column=1)
pesquisar_button.grid(row=1, column=0, columnspan=2)
resultado_listbox.grid(row=2, column=0, columnspan=2)

salvar_catalogo_button.pack(pady=10)

root.mainloop()
