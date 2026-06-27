from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Función para validar que el campo nombre no sea vacio y contenga al menos dos caracteres.
def validar_nombre(valor):
    if not valor.strip():
        return "El campo nombre no debe ser vacío"
    if len(valor.strip()) <2:
        return "El campo nombre debe tener al menos 2 caracteres"

    return None

def validar_email(valor):
    if not valor.strip():
        return "El campo email no debe ser vacío"
    
    if '@' not in valor:
        return "El campo email debe tener @"

    if '.' not in valor.split('@')[1]:
        return "El email debe tener un domino correcto"

    return None

def validar_edad(valor):
    try:
        edad = int(valor)
        if not (18 <= edad <=65):
            return "La edad debe ser entre 18 y 65 años"

    except ValueError:
        return "La edad deber ser un numero entero"
    
def validar_sueldo(valor):
    try:
        sueldo = float(valor)
        if sueldo <= 0:
            return "El sueldo debe ser mayor a cero"

    except ValueError:
        return "El sueldo debe ser un numero"


def validar_formulario(datos):
    erorres = {}

    validaciones = {
        'nombre':validar_nombre,
        'email':validar_email,
        'edad':validar_edad,
        'sueldo':validar_sueldo
    }

    for campo, funcion in validaciones.items():
        valor = datos.get(campo,'')
        error = funcion(str(valor))
        if error:
            erorres[campo] = error
        
    return erorres  


@app.route('/validar',methods=['POST']) 
def validar():
    datos = request.get_json()
    errores = validar_formulario(datos)

    if errores:
        return jsonify({'ok':False,'errores':errores})

    return jsonify({'ok':True,'mensaje':'Registro exitoso'})


if __name__=='__main__':
    app.run(debug=True)
    


    

    






#JSON


