import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear universo y conjuntos difusos
edad = ctrl.Antecedent(np.arange(0, 101, 1), 'edad')
edad['joven'] = fuzz.trimf(edad.universe, [0, 25, 50])
edad['adulto'] = fuzz.trimf(edad.universe, [25, 50, 75])
edad['viejo'] = fuzz.trimf(edad.universe, [50, 75, 100])

# Crear conjunto difuso de salida
resultado_edad = ctrl.Consequent(np.arange(0, 101, 1), 'resultado_edad', defuzzify_method='centroid')

# Definir conjuntos difusos para el resultado
resultado_edad['joven'] = fuzz.trimf(resultado_edad.universe, [0, 25, 50])
resultado_edad['adulto'] = fuzz.trimf(resultado_edad.universe, [25, 50, 75])
resultado_edad['viejo'] = fuzz.trimf(resultado_edad.universe, [50, 75, 100])

# Crear reglas difusas
regla1 = ctrl.Rule(edad['joven'], resultado_edad['joven'])
regla2 = ctrl.Rule(edad['adulto'], resultado_edad['adulto'])
regla3 = ctrl.Rule(edad['viejo'], resultado_edad['viejo'])

# Crear sistema de control
sistema = ctrl.ControlSystem([regla1, regla2, regla3])
motor_edad = ctrl.ControlSystemSimulation(sistema)

# Asignar un valor a la entrada
motor_edad.input['edad'] = 30

# Computar la salida
motor_edad.compute()

# Obtener el resultado
resultado = motor_edad.output['resultado_edad']
print("Resultado de la lógica difusa:", resultado)
