# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import sys
import os
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'winauto' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

from pywinauto import mouse, keyboard

"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

if module == "click":
    coord = GetParams("coord")
    option = GetParams("option")
    type_ = GetParams("type")

    try:
        click = {
            "click": mouse.click,
            "double": mouse.double_click,
            "press": mouse.press,
            "release": mouse.release
        }

        coord = (int(c) for c in coord.split(","))
        click[option](button=type_, coords=coord)


    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "move":
    coord = GetParams("coord")

    try:
        coord = (int(c) for c in coord.split(","))
        mouse.move(coords=coord)

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "scroll":
    coord = GetParams("coord")
    dist = GetParams("dist")

    try:

        coord = tuple([int(c) for c in coord.split(",")])
        mouse.scroll(coords=coord, wheel_dist=int(dist))


    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e
