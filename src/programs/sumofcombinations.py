input_string = "2,4,6,8"



sum = "16"





num_ar = [int(i) for i in input_string.split(",")]



sum = int(sum) if type(sum) == str and sum else 0





def get_combi(num_ar):

	res =  []

	tsum = sum

	for i in num_ar:

		if not sum:

			return

		tsum = sum

		tmp = i

		tmpres = []

		while (tsum % tmp == 0):

			tmpres.append(tmp)

			tsum = int(tsum//tmp)

		if(tmpres):

			res.append(tmpres)



	print(res)





get_combi(num_ar)