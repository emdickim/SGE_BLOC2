import create_registre as cr
import read_registre as rr
import uptade_registre as ur
from delete_registre import delete_reg

if __name__ == "__main__":
    print(delete_reg("Albert"))

#Trucada per executar la funció a l'arxiu create_registre.py
cr.create_reg()

results = rr.read_reg()
for i in results:
        print('\n')
        print('Nom: ' + str(i[0]))
        print('Adreça: ' + str(i[1]))
        print('Telèfon: ' + str(i[2]))
        print('Email: ' + str(i[3]))
        print('Neixement: ' + str(i[4]))
ur.update_reg('931111111', 'albert')



