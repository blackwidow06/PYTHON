#!/usr/bin/python3

class Plant:
	def __init__(plant, name, height, age):
		plant.name = name
		plant.height = height
		plant.age = age

	def show(plant):
		print(f"{plant.name}: {plant.height}, {plant.age} days old")

if __name__ == "__main__":
	print("=== Garden Plant Registery ===")

	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15 , 120)

	rose.show()
	sunflower.show()
	cactus.show()