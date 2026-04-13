def add(a, b):
    
    return a + b 

def subtract(a, b):

    return a - b

def multiply(a, b):
   
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b):
    
    return a ** b

if __name__ == "__main__":
    print("🧪 Running internal tests...")

    # Test 1: Addition
    try:
        assert add(2, 3) == 5
    except AssertionError:
        print(f"❌ Test Failed: add(2, 3) returned {add(2, 3)}, expected 5")
        exit(1)

    # Test 2: Subtraction
    try:
        assert subtract(10, 3) == 7
    except AssertionError:
        print(f"❌ Test Failed: subtract(10, 3) returned {subtract(10, 3)}, expected 7")
        exit(1)

    # Test 3: Multiplication
    try:
        assert multiply(3, 4) == 12
    except AssertionError:
        print(f"❌ Test Failed: multiply(3, 4) returned {multiply(3, 4)}, expected 12")
        exit(1)

    # Test 4: Power
    try:
        assert power(2, 3) == 8
    except AssertionError:
        # Returns 1 (XOR) instead of 8
        print(f"❌ Test Failed: power(2, 3) returned {power(2, 3)}, expected 8")
        exit(1)

    print("✅ All tests passed!")