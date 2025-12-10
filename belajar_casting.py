#belajar casting 
#merubah dari 1 data ke data tipe data lain
#tipedata = int, float, str, bool
print("---integer---")
data_int = -1;
print("data integer: ", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false bila 0
print("data float: ", data_float, ",type =",type(data_float))
print("data str: ", data_str, ",type =",type(data_str))
print("data bool: ", data_bool, ",type =",type(data_bool))

print("---float---")
data_float = 10.5;
print("data float: ", data_float, ",type =",type(data_float))

data_int = int(data_float) #akan dibuatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false bila 0
print("data int: ", data_int, ",type =",type(data_int))
print("data str: ", data_str, ",type =",type(data_str))
print("data bool: ", data_bool, ",type =",type(data_bool))


