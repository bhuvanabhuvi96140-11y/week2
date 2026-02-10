numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# Ascending Order
numbers.sort()
print("Ascending order:", numbers)
# Descending Order
numbers.sort(reverse=True)
print("Descending order:", numbers)
