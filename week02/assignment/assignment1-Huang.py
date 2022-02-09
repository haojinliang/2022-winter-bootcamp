@@ -2,16 +2,20 @@
 # This assignment is for exercising Python fundamental I and getting familiar with Python syntax.

 # 注意 - Copy this file and rename as assignment1-{first_name}.py then complete code with a PR.
 from datetime import datetime

 # Q1. Write a program which can compute the factorial of a given numbers.

 # Q1. Write a program which can compute the factorial of a given numbers.

 def factorial(x: int) -> int:
     if x == 0:
         return 1
     if x == 0 or x == 1:
         answer = 1
     else:
         return x * factorial(x - 1)
         answer = x * factorial(x - 1)
     return answer


 # print(factorial(2))

 assert factorial(0) == 1
 assert factorial(1) == 1
 @@ -22,12 +26,16 @@ def factorial(x: int) -> int:
 # [1 + 2 + ... + x] and x is always >= 1.

 def print_sum(x: int) -> str:
     sum_value = 0
     for i in range(1, x + 1):
         sum_value = sum_value + i
     return str(sum_value)
     if x >= 1:
         if x == 1:
             answer = str(1)
         else:
             answer = str(x + int(print_sum(x - 1)))
         return answer


 # print(print_sum(10))

 assert print_sum(1) == "1"
 assert print_sum(3) == "6"
 assert print_sum(5) == "15"
 @@ -36,11 +44,10 @@ def print_sum(x: int) -> str:
 # Q3. Write a program to check is a year is leap year (x is always > 0)

 def is_leap_year(year: int) -> bool:
     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
         return True
     else:
         return False
     return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False


 # print(is_leap_year(2022))

 assert is_leap_year(2000)
 assert is_leap_year(1996)
 @@ -51,11 +58,13 @@ def is_leap_year(year: int) -> bool:
 # Q4. Write a program to convert a list of lowercase words to uppercase words.

 def to_upper_case(words: [str]) -> [str]:
     for letter in range(len(words)):
         words[letter] = words[letter].upper()
     for i in range(len(words)):
         words[i] = words[i].upper()
     return words


 # print(to_upper_case(['hello', 'world']))

 assert to_upper_case(["abc", "de"]) == ["ABC", "DE"]
 assert to_upper_case(["Amazon", "Apple"]) == ["AMAZON", "APPLE"]

 @@ -64,22 +73,24 @@ def to_upper_case(words: [str]) -> [str]:
 # https://baike.baidu.com/item/%E5%BC%82%E6%88%96/10993677?fromtitle=xor&fromid=64178

 def xor(a: bool, b: bool) -> bool:
     return a and not b or b and not a
     return True if a != b else False


 # print(xor(True, True))

 assert not xor(True, True)
 assert xor(True, False)
 assert xor(False, True)
 assert not xor(False, False)

 # Q6. Write a Python program to display the current date and time under standard ISO 8601. e.g. 2021-12-03T10:15:30Z
 import datetime as dt

 # Q6. Write a Python program to display the current date and time under standard ISO 8601. e.g. 2021-12-03T10:15:30Z

 def get_current_time() -> str:
     current_time = dt.datetime.now().replace(microsecond=0).isoformat()
     return current_time + "Z"
     return datetime.now().isoformat(timespec='seconds') + 'Z'


 # print(get_current_time())

 assert "T" in get_current_time()
 assert "Z" in get_current_time()
 @@ -89,14 +100,16 @@ def get_current_time() -> str:
 # Q7. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
 # please define function and test yourself.

 def sum_integer(x, y):
     if 15 <= x + y <= 20:
         return 20
     else:
         return x + y

 def get_sum(a: int, b: int) -> int:
     sum_value = a + b
     if 15 <= sum_value <= 20:
         sum_value = 20
     return sum_value

 # print(sum_integer(16, 2))

 assert get_sum(5, 11) == 20
 assert get_sum(3, 7) == 10
 assert get_sum(10, 11) == 21
 assert sum_integer(1, 2) == 3
 assert sum_integer(1, 14) == 20
 assert sum_integer(2, 14) == 20
 assert sum_integer(12, 14) == 26
