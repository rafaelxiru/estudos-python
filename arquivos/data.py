#F-string:
from datetime import datetime
hoje = datetime.now()
data_formatada = f"{hoje:%d/%m/%Y}"
print("data formatada :" ,data_formatada)


#Método format()
from datetime import datetime 
hoje= datetime.now()
data_formatada=hoje.strftime ("%d/%m/%Y")
print ("data formatada :" , data_formatada)