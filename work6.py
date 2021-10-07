try:
        n = int(input("Введите количество элементов массива")) 
except ValueError:
        print("Ошибка")
else:
        array = [0]*n
        try:
            for i in range(0,n):
                    array[i]=int(input("Введите элемент"))
        except ValueError:
                print("Ошибка")
        else:
            try:
                delta = int(input("Введите delta:"))
            except ValueError:
                print("Ошибка")
            else:    
                result1 = array.count(min(array) + delta)
                result2 = array.count(min(array) - delta)
                print(result1+result2) 
