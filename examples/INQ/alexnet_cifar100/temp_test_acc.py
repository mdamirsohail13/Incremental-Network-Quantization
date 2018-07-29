import os
import csv


all_files = ['alexnet_cifar100_5-bit-inq-solver-train-out.txt'] #os.listdir('Out') 					#Lx

for w in all_files:
	
	out_path = str(w) # Path for ...-Out.txt files 
	new_path = str(w[:-4])+'-accuracy.txt' # Path to save	#Lx
	print(out_path)
	out_file = open(out_path, 'r')

	num_lines = 0
	all_lines = out_file.readlines()

	save_file = open( new_path,'w+')
	save_file.write(out_path)
	
	ite = -200
	for i in range(len(all_lines)):
		line = all_lines[i]
		if 'Test net output #0: accuracy@1' in line:

			ite += 200 # test after 3000 iterations
			acc1 = float( all_lines[i].split(': accuracy@1 = ')[1] )
			acc5 = float( all_lines[i+1].split(': accuracy@5 = ')[1] )
			loss = float(  ( (all_lines[i+2].split(': loss = ')[1]).split(' (*') )[0]  )

			save_file.write( '\nIteration : '+ str(ite)+'\t\t\tAcc@1 : '+ str(acc1)+'\t\t\tAcc@5 : '+ str(acc5) +'\t\tloss : '+str(loss) )
			print (ite, 'acc@1', acc1, 'acc@5',acc5, loss)
			# save_file.write('--------------------------------------------\n')

	save_file.close()

	print('-----------------------------------------------------')	

print ('Done')

