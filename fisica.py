import math

def angulo(u,v):
    num = int(u[0])*int(v[0]) + int(u[1])*int(v[1]) + int(u[2])*int(v[2])
    mod_u = math.sqrt((int(u[0])**2)+(int(u[1])**2)+(int(u[2])**2))
    mod_v = math.sqrt((int(v[0])**2)+(int(v[1])**2)+(int(v[2])**2))
    return int(math.degrees(math.acos(num/(mod_u*mod_v))))


v = [1,-2,1] #valor da velocidade atribuido
f = []

while True:
	forca = raw_input("\nDigite o vetor forca i j k: ")
	f = forca.split(" ")
	resp = angulo(f,v)
	print resp
	if resp == 0 or resp== 180:
		print("Resposta: ZERO")
	elif resp == 90 or resp == 270:
		print("Resposta: MCU")
	else:
		print("Resposta: MC")
	