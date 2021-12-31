import random as r

mail = "test@test.com"

mail1 = mail.split('@')[0]
mail2 = mail.split('@')[1]

print(f'{mail1}{mail2}')

mail1_new = f'{mail1}{r.randrange(999, 10000)}'

mail_final = f'{mail1_new}@{mail2}'
print(f'{mail_final}')
