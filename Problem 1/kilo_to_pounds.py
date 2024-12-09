def kilo_to_pounds(kilos): 
    return kilos * 2.20462



if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.5f} lbs')