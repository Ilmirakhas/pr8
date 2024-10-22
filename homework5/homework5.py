s=0
P=True
while P:
    print("Введите число (или 'stop', 'end' для завершения): ")
    n=input()
    if n=="end" or n=='stop':
        P=False
        break
    else:
        for i in range(len(n)):
            if n[i] in "-0123456789.,":
                m=1
            else:
                m=0
                break
        if m==1:
            s+=float(n)
        else:
            print("Некорректный ввод. Введите число.")
            P=False
            break
print(s)