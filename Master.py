import stepper_motors
import time

stepper_motors.scramble_real_cube()

print("It is time to solve the cube :)")
time.sleep(10)

stepper_motors.solve_real_cube()
