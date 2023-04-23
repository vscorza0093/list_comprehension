# List_comprehension

List comprehension is a great sintax to create lists based on other existent lists, enumerating their elements and passing to the new list based on our needs and conditions.

It has a beautiful capacity to create powerful funcionalitys and save us lines of code

The sintax is very simple, but has space to be a lot more complex if we start nesting loops inside a single list comprehension


Base sintax:
  
    new_list = [num for num in iterable]
    
    fruits = ["apple", "banana", "watermeloon"]
    new_fruit_list = [fruit for fruit in fruits]
    
    
Adding if statement using generator

    new_list = [num for num in generator(n) if num % 2 == 0]
    

