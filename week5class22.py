score = int(input('What is your score? '))
if score >= 60:
    print('You passed')
else:
    print('You failed')
if score >= 90:
    print('Your grade is A')
if 90 > score >= 80:
    print('Your grade is B')
if 80 > score >= 70:
    print('Your grade is C')
if 70 > score >= 60:
    print('Your grade is D')
if 60 > score >= 0:
    print('Your grade is F')