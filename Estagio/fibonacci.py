def Fibonacci(n):
    fibonacciSeq = [0, 1]
    while fibonacciSeq[-1] < n:
        fibonacciSeq.append(fibonacciSeq[-1] + fibonacciSeq[-2])
    return fibonacciSeq

def verifyFibonacci(number):
    fibonacciSeq = Fibonacci(number)
    if number in fibonacciSeq:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."

number = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
print(verifyFibonacci(number))
