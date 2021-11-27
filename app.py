#!/usr/bin/python

from gen_test_data import gen_test_data
from NanoController import NanoController

controllers = [
	NanoController("http://127.0.0.1:3000")
	# TODO: Add OracleController to this list
]

if __name__ == "__main__":
	n_tests = 100

	print("Generating test data...")
	(cr_authors, cr_books, up_authors, up_books) = gen_test_data(n_tests)
	print("Test data generated")

	# Start tests
	for controller in controllers:
		print("Testing", controller.name, "...")

		# TODO: Measure time taken by n of each type of operation
		# TODO: Find a way to test all operations when relations are affected

		# 1st test checks creating author records ( no references/relations  )
		for i in range(n_tests):
			controller.create_author(i, cr_authors[i])

		# 2nd test checks creating book records   ( yes references/relations )
		for i in range(n_tests):
			controller.create_book(i, cr_books[i])

		# 3rd test checks reading  author records ( no references/relations  )
		for i in range(n_tests):
			controller.read_author(i)

		# 4th test checks reading  book records   ( yes references/relations )
		for i in range(n_tests):
			controller.read_book(i)

		# 5th test checks updating author records ( no references/relations  )
		for i in range(n_tests):
			controller.update_author(i, up_authors[i])

		# 6th test checks updating book records   ( yes references/relations )
		for i in range(n_tests):
			controller.update_book(i, up_books[i])

		# 7th test checks deleting author records ( no references/relations  )
		for i in range(n_tests):
			controller.delete_author(i)

		# 8th test checks deleting book records   ( yes references/relations )
		for i in range(n_tests):
			controller.delete_book(i)

		print(controller.name, "testing complete")
