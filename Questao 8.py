nome=["Bob Smith","Sue Jones","Carl Max"]
resp=("")
for i in nome:
    nomesep=i.split()
    resp+=nomesep[1]+","
    nomesep[0]+";"
print(resp)
