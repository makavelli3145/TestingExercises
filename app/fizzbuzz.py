def fizzbuzz(n: int)-> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 3 != 0 and n % 5 == 0:
        return "Buzz"
    else:
        return str(n)