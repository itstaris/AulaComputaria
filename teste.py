mensagem = 'Teste de procura de um valor'
print(mensagem.find('valor')) # 23
print(mensagem.find('abc')) # -1

#%%
mensagem = 'Teste de separação de uma mensagem'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem)) # type 'list'
print(nova_mensagem)
print(f"\n{'\n'.join(nova_mensagem)}")

#%%
meuTexto = "Esta lista contém muitos nomes"

print(f"{meuTexto if "muitos" in meuTexto else 'Nem são tantos nomes assim na lista'}")

#%%