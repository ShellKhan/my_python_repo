from sys import argv

script_name, worktime, rate, prize = argv

print(int(worktime) * int(rate) + int(prize))
