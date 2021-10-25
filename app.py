#!/usr/bin/python

from NanoController import NanoController

controllers = [
	NanoController("http://127.0.0.1:3000")
	# TODO: Add OracleController to this list
]

create_test_data = {"string": "abc", "number": 42, "boolean": True}
update_test_data = {"string": "abcd", "number": 5, "boolean": False}

for controller in controllers:
	print("Testing", controller.name, "...")

	# TODO: Generate random IDs and repeat tests different number of times
	# TODO: Measure time taken by each operation
	# TODO: Find a way to test all operations when relations are affected
	controller.create("test", 0, create_test_data)
	controller.read("test", 0)
	controller.update("test", 0, update_test_data)
	controller.delete("test", 0)

	print(controller.name, "testing complete")
