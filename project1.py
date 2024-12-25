def counting_sort(arr):
    max_value  =max(arr)
    min_value  = min(arr)
    
    
    offset = -min_value 
    
    counting = [0] * (max_value - min_value + 1)  
    
    for num in arr:
        counting[num + offset] += 1
        
    for i in range(1, len(counting)):
        counting[i] += counting[i - 1]
        
        output = [0] * len(arr)
    
    for num in reversed(arr): 
        output[counting[num + offset] - 1] = num
        counting[num + offset] -= 1 
    
    return output



user_input = input("")
arr = list(map(int, user_input.split(','))) 
sorted_arr = counting_sort(arr)


print("", sorted_arr)