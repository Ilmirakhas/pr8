while True:
 num1_str = input("Введите первое число: ")
 num2_str = input("Введите второе число: ")
 is_num1_valid = True
 is_num2_valid = True

 for char in num1_str:
  if not char.isdigit() and char != '-':
   is_num1_valid = False
   break
 for char in num2_str:
  if not char.isdigit() and char != '-':
   is_num2_valid = False
   break

 if is_num1_valid and is_num2_valid:
  num1 = int(num1_str)
  num2 = int(num2_str)
  sum = num1 + num2
  print("Сумма:", sum)
 else:
  print("Неверный ввод")
