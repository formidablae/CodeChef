# cook your dish here
input_of_prob = input().split(" ")
if float(input_of_prob[0]) % 5 != 0 or float(input_of_prob[1]) - float(input_of_prob[0]) < 0.5: print(input_of_prob[1])
else: print("{}0".format(float(input_of_prob[1]) - float(input_of_prob[0]) - 0.5))
