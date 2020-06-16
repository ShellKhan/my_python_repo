rating = [7, 5, 3, 3, 2]

user_input = int(input('Введите число: '))

for ind, val in enumerate(rating):
    if val < user_input:
        rating.insert(ind, user_input)
        break

if rating[-1] > user_input:
    rating.append(user_input)

print(rating)