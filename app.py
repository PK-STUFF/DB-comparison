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

	for n_tests in (10, 100, 1000):
		# TODO: Measure time taken by n of each type of operation
		# TODO: Find a way to test all operations when relations are affected

		for i in range(n_tests):
			controller.create("test", i, create_test_data)

		for i in range(n_tests):
			controller.read("test", i)

		for i in range(n_tests):
			controller.update("test", i, update_test_data)

		for i in range(n_tests):
			controller.delete("test", i)

	print(controller.name, "testing complete")
