C = float(input('What is the value of the final capital? '))
Co = float(input('What is the value of the original capital? '))
Cj = float(input('What is the value of the initial capital? '))
Ts = float(input('What is the next time in days? '))
Tt = float(input('What is the total time in days? '))

L_MT = 100 * ((((C / Co) ** (Ts / Tt)) * (Co / Cj)) - 1)

print('The average total profit for the next day is: ', L_MT, '%')