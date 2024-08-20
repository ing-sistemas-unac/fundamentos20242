"""
Crea un programa que pida al usuario una cantidad n de bytes y realice su conversión a:
kilobytes
megabytes
gigabytes
terabytes
"""
print("Ingrese la cantidad de bytes que desea convertir")
bytes = int(input())
kilobytes = bytes / 1024
megabytes = kilobytes / 1024
gigabytes = megabytes / 1024
terabytes = gigabytes / 1024
print(f"{bytes:.2f} bytes son {kilobytes:.2f} KB, {megabytes:.2f} MB, {gigabytes:.2f} GB y {terabytes:.2f} TB")