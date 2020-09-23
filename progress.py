# Create by John
# 23/09/20
import time
def progress(r=30, c=50):
	i = range(r + 1)
	for n in i:
		p = int((n / i[-1]) * 100) # Primeiro calculamos a porcentagem do item iterado, e o final
		p_ = int((p / 100) * c) # Agora calculamos x% do tamanho da barra
		print('\rProgress |{}| {}/{}'.format(('#' * p_) + ' ' * (c - p_), n, i[-1]), end="")
		time.sleep(0.1)
progress(c=30)