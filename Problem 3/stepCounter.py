def feet_to_steps(user_feet):
   feet_per_step = 2.5
   return user_feet / feet_per_step

if __name__ == '__main__':
    user_feet=float(input("Enter feet:"))
    print(f'Steps: {feet_to_steps(user_feet):.2f}')
    