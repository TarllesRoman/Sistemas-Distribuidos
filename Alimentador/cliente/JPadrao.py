#coding: utf-8



def iniciaJanela(janela):
	w = 300
	h = 300
	ws = janela.winfo_screenwidth()/2 - w/2
	hs = janela.winfo_screenheight()/2 - h/2
	janela.geometry('+%d+%d' % (ws,hs))
