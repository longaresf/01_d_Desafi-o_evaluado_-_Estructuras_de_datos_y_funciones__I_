import sys

tas_conv_sol = sys.argv[1]
tas_conv_peso_ar = sys.argv[2]
tas_conv_dolar = sys.argv[3]
monto_peso_ch = sys.argv[4]

monto_sol =  int(monto_peso_ch) * float(tas_conv_sol)
monto_peso_ar =  int(monto_peso_ch) * float(tas_conv_peso_ar)
monto_dolar =  int(monto_peso_ch) * float(tas_conv_dolar)

print(f"Los {monto_peso_ch} pesos chilenos equivalen a:\n {monto_sol} Soles \n {monto_peso_ar} Pesos Argentinos \n {monto_dolar} Dólares")
