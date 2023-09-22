#user input
pool_volume_ltr = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours_worker_missing = float(input())


#Logic
#Calculate liter per pipe
pipe_one = pipe_one_debit * hours_worker_missing
pipe_two = pipe_two_debit * hours_worker_missing

#calculate full debit of both pipes
combine_pipes = pipe_one + pipe_two

#calculate how filled is the pool
overflow = combine_pipes - pool_volume_ltr

#calculate percentage of filling the pool as per pipe
#full capacity of pool
full_percentage = combine_pipes /  pool_volume_ltr * 100
#as per pipe one
pipe_one_percentage = (pipe_one / combine_pipes * 100)
#as per pipe two
pipe_two_percentage = (pipe_two / combine_pipes * 100)

if pool_volume_ltr >= combine_pipes:
    print(f'The pool is {full_percentage:.2f}% full. Pipe 1: {pipe_one_percentage:.2f}%. Pipe 2: {pipe_two_percentage:.2f}%.')
else:
    print(f'For {hours_worker_missing:.2f} hours the pool overflows with {overflow:.2f} liters.')

