C = float(input('What is the value of the final capital? '))
Cj = float(input('What is the value of the initial capital? '))
Tt = float(input('What is the total time in days? '))
Tj = float(input('What is the actual time in days? '))

LM_P = 100 * ((C / Cj) ** (1 / (Tt - Tj)) - 1)

print('The average periodic profit for the next few days is: ', LM_P, '%')