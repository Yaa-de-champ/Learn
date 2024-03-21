# DOKU-AMPONSAH NANA YAA ADOMAA

# ASSIGNMENT





# Question 1

def count_vow():
    
    sentence = input('Enter a sentence: ')
    
    vowels = 'aeiouAEIOU'
    
    count = 0
    
    for char in sentence:
        if char in vowels:
            count += 1
        
    return f'There are {count} vowels in this sentence.'



# Question 2
def remov_dup():
    
    numlist =  input('Enter  a list of numbers (comma-separated): ').split(',')
    
    duplist = [int(num) for num in numlist]
    
    uniquenum = list(set(duplist))
    
    if len(uniquenum) == len(duplist):
        
        return 'There are no duplicates!'
    else:
           
        return f'This is the list without duplicates: {uniquenum}'


    
# Question 3

def sqv_even():

    numbered_list = input('Enter  a list of numbers (comma-separated): ').split(',')

    newlist = [int(num) for num in numbered_list]
        
    even_numbers = [num for num in newlist if num % 2 == 0]   
    
    result = sum([num ** 2 for num in even_numbers])

    if not even_numbers:
        
        return 'No even numbers found'
    else:  

        return f'The sum of squares of even numbers present in the list is {result}'



