# List_comprehension

List comprehension is a great sintax to create lists based on other existent lists, enumerating their elements and passing to the new list based on our needs and conditions.

Its a method to add values that are in other lists to a new list in, a dinamcly way

It has a beautiful capacity to create powerful funcionalitys and save us lines of code

The sintax is very simple, but has space to be a lot more complex if we start nesting loops inside a single list comprehension

U+1F916
 
Base sintax:
  
    new_list = [num for num in iterable]
    
    fruits = ["apple", "banana", "watermeloon"]
    new_fruit_list = [fruit for fruit in fruits]
    
    
Using if statement and generator

    new_list = [num for num in generator(n) if num % 2 == 0]
    
    
List comprehension with nested loops

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
                    new_list = []
                    new_list.append(a)
                    new_list.append(b)
                    new_list.append(c)
                    final_list.append(new_list)

    print(final_list)

            
