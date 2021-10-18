def slices(num_string: str, substring_length: int):
	
	    if substring_length > len(num_string) or substring_length <= 0:
	        raise ValueError("input not valid")
        
	
	    #return [num_string[i : i + substring_length] for i in range(len(num_string) - substring_length + 1)]
        for i in range(len(num_string) - substring_length + 1):
            # i : i + substring_length
            print('l')

print(slices('abcde',20))