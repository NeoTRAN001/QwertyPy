# -*- coding: utf-8 -*-
import os

class View:
    # Global variables and constants
    BANNER = '''
    
 ::::::::  :::::::::  :::    ::: :::::::::      :::::::::  :::   ::: 
:+:    :+: :+:    :+: :+:    :+: :+:    :+:     :+:    :+: :+:   :+: 
+:+        +:+    +:+ +:+    +:+ +:+    +:+     +:+    +:+  +:+ +:+  
+#+        +#++:++#:  +#+    +:+ +#+    +:+     +#++:++#+    +#++:   
+#+        +#+    +#+ +#+    +#+ +#+    +#+     +#+           +#+    
#+#    #+# #+#    #+# #+#    #+# #+#    #+# #+# #+#           #+#    
 ########  ###    ###  ########  #########  ### ###           ###    
         
    0 - Salir
    1 - Ver Datos
    2 - Insertar
    3 - Actualizar
    4 - Borrar
    5 - Buscar
    '''
    # Default: Class contructor
    def __init__(self):
        pass
    # Method: It ito display a banner and the user´s option return
    def create_banner(self):
        try:
            print(self.BANNER)
            option =  int(input(':'))

            return option
        except:
            return 0
    # Clean the terminal on both windows and linux
    def clear_window(self):
        clean = ''
        if os.name == "posix":
            clean = "clear"        
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            clean = "cls"
        os.system(clean)
