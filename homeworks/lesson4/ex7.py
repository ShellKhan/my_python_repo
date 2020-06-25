# формулировка задачи неясна. как я понял, функция должна выдавать генератор ряда факториалов от 1 до n
# функцию factorial импортировать не стал, так как оно и так достаточно просто считается
def fact(number: int) -> int:
    counter = 1
    result = 1
    while counter <= number:
        result *= counter
        counter += 1
        yield result


n = 15
for el in fact(n):
    print(el)
