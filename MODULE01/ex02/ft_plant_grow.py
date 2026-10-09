#!/usr/bin/python3

class Plant:
	def __init__(plant, name, height, age):
		plant.name = name
		plant.height = height
		plant.age = age

	def grow(plant):
		plant.height = plant.height + 0.8

	def one_day_passes(plant):
		plant.age = plant.age + 1
	
	def show(plant):
		print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

	
if __name__ == "__main__":
	print("=== Garden Plant Growth === ")

	rose = Plant("Rose", 25.0, 30)
	rose.show()

	initial_height = rose.height

	for day in range(1, 8):
		rose.grow()
		rose.one_day_passes()
		print(f"=== Day {day} ===")
		rose.show()

	growth = round(rose.height - initial_height, 1)
	print(f"Growth this week: {growth}cm")