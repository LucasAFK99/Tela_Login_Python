import customtkinter
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('500x300')
def clique():
    print('Fazer Login')
def clique2():
    print('Esqueceu a Senha')

texto = customtkinter.CTkLabel(janela, text='Fazer Login')
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Email')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='Senha', show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar Login')
checkbox.pack(padx=8, pady=10)

botao = customtkinter.CTkButton(janela, text='Login', command=clique)
botao.pack(padx=10, pady=10)

esqueceuSenha = customtkinter.CTkButton(janela, text='Esqueceu a Senha', command=clique2)
esqueceuSenha.pack(padx=10, pady=10)

janela.mainloop()
