import tkinter as tk
from tkinter import ttk

def init_window():
    window = tk.Tk()#crear pantalla
    window.title('Mi primera aplicacion')#titulo  pantlla
    window.geometry('1366x768')#establecer el tamaño de pantalla 
    
    label= tk.Label(window, text='calculadora' , font=('Arial bold',15))#texto cabecera
    label.grid(column = 0 , row = 0)

    label_entrada1= tk.Label (window, text = 'Ingrese el primer numero:', font=('Arial bold',10))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2= tk.Label (window, text = 'Ingrese el segundo numero:', font=('Arial bold', 10))
    label_entrada2.grid(column = 0, row = 2)
#agregar los 2 campos de texto(numeros)
    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)
    #aqui van los focus

    entrada1.grid(column = 1, row =1)
    entrada2.grid(column = 1, row =2)

    label_operador = tk.Label(window, text = 'Escoje un operador' , font=('Arial bold', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(window, text='resultado: ', font=('Arial bold', 15))
    label_resultado.grid(column =0, row = 6)
    def calculadora(num1, num2, operador):
        if operador=='+':
            resultado = num1 + num2
        elif operador=='-':
            resultado = num1 - num2
        elif operador=='*':
            resultado = num1 * num2
        elif operador=='/':
            resultado = round(num1 / num2, 2)
        else:
            resultado = num1 ** num2
        return resultado
    def click_calcular(label, num1, num2, operador):
        valor1= float(num1) 
        valor2= float(num2)

        res = calculadora(valor1, valor2, operador)
        label.configure(text = 'Resultado: ' + str(res))
    def click_transformar(label, num1, num2, operador):
        valor1= float(num1) 
        valor2= float(num2)

        res = int(calculadora(valor1, valor2, operador))
        label.configure(text = 'Entero: ' + str(res))
    def click_ac(label, num1, num2, operador):
        valor1= float(num1) 
        valor2= float(num2)
        
        res = int(0)
        label.configure(text = 'A/C: ' + str(res))


    boton = tk.Button(window,
                    command = lambda: click_calcular(
                             label_resultado,
                             entrada1.get(),
                             entrada2.get(),
                             combo_operadores.get()),
                    text='Calcular', 
                    bg="blue",
                    fg="white")

    boton_2 = tk.Button(window,
                    command = lambda: click_transformar(
                             label_resultado,
                             entrada1.get(),
                             entrada2.get(),
                             combo_operadores.get()),
                    text='Transformar(en un entero)', 
                    bg="purple",
                    fg="white")
    boton_3 = tk.Button(window,
                    command = lambda: click_ac(
                             label_resultado,
                             entrada1.get(),
                             entrada2.get(),
                             combo_operadores.get()),
                    text='A/C', 
                    bg="red",
                    fg="white")
    boton.grid(column = 0, row = 4)
    boton_2.grid(column = 1, row = 4)
    boton_3.grid(column = 0, row = 5)
    window.mainloop()
init_window()
def main():
    init_window()
main()