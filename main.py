#yearly IRA at IFRN

#switch final function
def switch_final(response, final_matrix):
	if(response == 1):
		before_score = float(input("\ninforme seu IRA anterior: "))
		final_score = (final_matrix + before_score)/2
		print('próximo IRA: {final_s:.2f}'.format(final_s = final_score))
		print("\n\nthe end")
	else:
		print("\n \nthe end")
			


print("###### Calculadora de IRA para o IFRN ##### \n")
#how much subjects
qtd_subjects = int(input("quantas disciplinas? "))

#variable initialization
score_list = []
workload_list = []

#recording values in lists
for c in range(0,qtd_subjects):
	count = c + 1
	score = float(input("qual a nota {}? ".format(count)))
	score_list.append(score)
	wl = float(input("qual a carga-horária da disciplina {}? ".format(count)))
	workload_list.append(wl)

#calculating
final_matrix = []
for c in range(0,qtd_subjects):
	calc_one = score_list[c] * workload_list[c]
	#print (calc_one)
	final_matrix.append(calc_one)

#final calculation of annual income (IRA)
final_matrix = sum(final_matrix)
sum_wl = sum(workload_list)
final_matrix = final_matrix/sum_wl

print("IRA: {score:.2f}".format(score = final_matrix))

#final operation

decision = int(input('\nDeseja saber a atualização do seu IRA?\n[ 1 ] - Sim\n[ 2 ] - não\n '))
switch_final(decision, final_matrix)
