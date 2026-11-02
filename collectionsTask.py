students = [
	("Alice", 78),
	("Bob", 45),
	("Charlie", 90),
	("Diana", 62),
	("Kent", 30)
]

for name, score in students:
	print(name, score)

print("\nStudents who scored 60 or above:")

for name, score in students:
	if score >= 60:
		print(name)

pass_mark = 50
passed = 0

for name, score in students:
	if score >= pass_mark:
		passed += 1

print("\nNumber of students who passed:", passed)
 





employees = [
	("John", "IT", 50000),
	("Jane", "HR", 45000),
	("Mike", "IT", 60000),
	("Sara", "Finance", 70000)
]

for name, department, salary in employees:
	print(name, department, salary)

print("\nIT employees earning more than 55000:")

for name, department, salary in employees:
	if department == "IT" and salary > 55000:
		print(name)




points = [
	(2, 3),
	(-1, 4),
	(5, -6),
	(0, 7),
	(-3, -2)
]

positive_points = []

for x, y in points:
	if x > 0 and y > 0:
		positive_points.append((x, y))

print("Positive points:", positive_points)






products = [
	("Laptop", 1200),
	("Mouse", 25),
	("Keyboard", 45),
	("Monitor", 300),
	("USB Cable", 10)
]

def expensive_products(product):
	name, price = product
	return price > 100

expensive = list(filter(expensive_products, products))

print("Products costing more than 100:")

for name, price in expensive:
	print(name, price)

total = 0

for name, price in products:
	total += price

print("\nTotal price of all products:", total)

print("\nProduct details:")

for name, price in products:
	print(f"Product: {name} - Price: {price}")