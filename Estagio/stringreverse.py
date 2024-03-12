def stringInverter(string):
    inverterString = ''
    for char in string[::-1]:
        inverterString += char
    return inverterString

originalString = input("Digite uma string para inverter: ")
inverterString = stringInverter(originalString)
print("A string invertida é:", inverterString)
