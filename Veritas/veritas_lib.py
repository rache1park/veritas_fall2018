import random
_list=['r','p','s']
def get_comp():
    #result=random.choice(_list)
    comp=random.randint(0,2)
    if comp==0:
        result='r'
    elif comp==1:
        result='s'
    else:
        result='p'
    return result
def who_is_winner(user,computer):
    if (user=='r') and (computer=='p'):
        return "computer"
    elif (user=='r') and (computer=='s'):
        return "user"
    elif (user=='p') and (computer=='s'):
        return "computer"
    elif (user=='p') and (computer=='r'):
        return "user"
    elif (user=='s') and (computer=='r'):
        return "computer"
    elif (user=='s') and (computer=='p'):
        return "user"
    elif (user=='r') and (computer=='r') :
        return "Tie"
    elif (user=='s') and (computer=='s') :
        return "Tie"
    elif (user=='p') and (computer=='p') :
        return "Tie"
