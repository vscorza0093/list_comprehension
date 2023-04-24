# &#128013; List_comprehension

List comprehension is a great and dynamic feature to create lists based on other existent list, iterating their elements and saving on a new list based on our needs and conditions.

It has a beautiful capacity to create powerful funcionalitys using one line of code

The sintax is very simple, but has space to be a lot more complex if we start nesting loops inside a single list comprehension

 

&#128209; Base sintax:
  
    new_list_of_int = [num for num in list_of_int]
    
    fruits = ["apple", "banana", "watermeloon"]
    new_fruit_list = [fruit for fruit in fruits]
    
    
&#128272; Using if statement and generator

    new_list = [num for num in range(n) if num % 2 == 0]
    
    
&#9889; List comprehension with nested loops

    x = 2
    y = 2
    z = 2
    n = 4
    
    new_list = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != 4]

The code above will produce the same effect as:

    x = 2
    y = 2
    z = 2
    n = 4

    final_list = []
    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):
                if a + b + c != n:
                    temp_list = []
                    temp_list.append(a)
                    temp_list.append(b)
                    temp_list.append(c)
                    final_list.append(temp_list)

    print(final_list)

            
