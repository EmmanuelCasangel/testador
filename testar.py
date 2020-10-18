import os
import argparse

parser = argparse.ArgumentParser(description="Testa os labs")
parser.add_argument('-l', '--lab-number', type=str, help="O numero do lab que voce quer testar (01, 02, ...)", required=True)
args = parser.parse_args()

lab_number = args.lab_number
dir = "./testes/lab" + lab_number + "/"

if not os.path.exists(dir):
  os.makedirs(dir)

for i in range (1, 10):

    executar_s = "python3  lab"+ lab_number +".py < aux"+ lab_number + "/open/arq0"+ str(i) +".in > "+ dir + "rq0" + str(i) + ".result"
    comparar_s = "diff aux" + lab_number + "/open/arq0" + str(i) + ".out "+ dir + "rq0" + str(i) + ".result"


    print("Linhas diferentes entre a saida gerada atraves do arq0"+ str(i) + ".in e a saida esperada (arq0" + str(i) + ".out):")
    print("\n")

    os.system(executar_s)
    os.system(comparar_s)

    print("\n\n\n\n")

