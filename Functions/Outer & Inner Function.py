def outer():
    def inner():
        print("Inner Function")
    print("Outer Function")
    inner()

outer()
