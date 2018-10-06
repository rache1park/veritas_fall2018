import veritas_lib

my= input('What is yours? [r,p,s] ')
comp=veritas_lib.get_comp()
print(comp)
winner=veritas_lib.who_is_winner(my,comp)
print(winner)
