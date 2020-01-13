from view import View
from lenguage import Lenguage

def main():
    view = View()
    option_banner = 1

    while option_banner != 0:
        
        view.clear_window()
        option_banner = view.create_banner()

        if option_banner == 1:
            print('\n', Lenguage().get_lengauges())
            
        if option_banner == 2:
            lenguage = Lenguage()
            lenguage.id_lenguage = int(input('Ingresa el id: '))
            lenguage.name_lenguage = input('Ingresa el nombre: ')
            lenguage.type_lenguage = input('Ingresa el tipo: ')

            print(Lenguage().insert_lenguage(lenguage) )

        if option_banner == 3:
            id = int(input('Ingresa el id: '))
            lenguage = Lenguage(id)
            lenguage.name_lenguage = input('Ingresa el nuevo nombre: ')
            lenguage.type_lenguage = input('Ingresa el nuevo tipo: ')
            print(Lenguage().update_lenguage(lenguage))

        if option_banner == 4:
            id = int(input('Ingresa el id:'))
            print(Lenguage().delete_lengauje(id))

        if option_banner == 5:
            id = int(input('Ingresar el id del lenguaje que quiere buscar: '))
            print(Lenguage().get_lengauges(id))


        input()
    else:
        print('Hasta luego')

if __name__ == "__main__":
    main()