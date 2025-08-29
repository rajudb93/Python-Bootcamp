def my_generator():
    for i in range(5):
        yield i
        
        
value = my_generator()
for i in value:
    print(i)
        
        