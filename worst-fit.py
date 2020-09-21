# Worst Fit

def worstFit(blockSize, m, processSize, n): 
	allocation = [-1] * n 
	for i in range(n): 
		wstIdx = -1
		for j in range(m): 
			if blockSize[j] >= processSize[i]: 
				if wstIdx == -1: 
					wstIdx = j 
				elif blockSize[wstIdx] < blockSize[j]: 
					wstIdx = j 

		if wstIdx != -1: 
			allocation[i] = wstIdx 
			blockSize[wstIdx] -= processSize[i] 

	print("Process No. Process Size Block no.") 
	for i in range(n): 
		print(i + 1, "		 ", 
			processSize[i], end = "	 ") 
		if allocation[i] != -1: 
			print(allocation[i] + 1) 
		else: 
			print("Not Allocated") 

if __name__ == '__main__': 
	m = int(input("Enter the block size: "))
	n = int(input("Enter the process size: "))
	blockSize = list(map(int, input("Enter block sizes: ").split()))  
	processSize = list(map(int, input("Enter process sizes: ").split())) 

	worstFit(blockSize, m, processSize, n) 
