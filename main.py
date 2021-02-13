def isValidSubsequence(array, sequence):
	go = True
	j = 0
	pos = 0
	while go:
		if j == len(sequence):
			return True
		if len(array)-pos >= len(sequence)-j:
			for i in range(pos,len(array)):
				go = False
				if array[i] == sequence[j]:
					pos = i+1
					go = True
					j += 1
					break
					
		else:
			return False
	return go
		
