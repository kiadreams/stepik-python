class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


for word in input().split():
    if hasattr(Person, word.lower()):
        print(f"{word}-YES")
    else:
        print(f"{word}-NO")
