def ex32sp(x,y):
	i=0
	numbers=[]

	
	while i < x:
		print "The i is:%d" % i 
		i = i + y
		numbers.append(i)
		
	print "The numbers elements is:"
	
	for num in numbers:
		print num