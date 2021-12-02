#!/usr/bin/python

from timeit import default_timer as timer

from gen_test_data import gen_test_data
from NanoController import NanoController

controllers = [
	NanoController("http://127.0.0.1:3000")
	# TODO: Add OracleController to this list
]

if __name__ == "__main__":
	n_tests = 100
	time_results = []

	print("Generating test data...")
	(cr_authors, cr_books, up_authors, up_books) = gen_test_data(n_tests)
	print("Test data generated")

	# Start tests
	for ci, controller in enumerate(controllers):
		time_results.append([])

		print("Testing", controller.name, "...")

		# 1st test checks creating author records ( no references/relations  )
		start = timer()

		for i in range(n_tests):
			controller.create_author(i, cr_authors[i])

		time_results[ci].append((timer() - start) / n_tests)

		# 2nd test checks creating book records   ( yes references/relations )
		start = timer()

		for i in range(n_tests):
			controller.create_book(i, cr_books[i])

		time_results[ci].append((timer() - start) / n_tests)

		# 3rd test checks reading  author records ( no references/relations  )
		start = timer()

		for i in range(n_tests):
			controller.read_author(i)

		time_results[ci].append((timer() - start) / n_tests)

		# 4th test checks reading  book records   ( yes references/relations )
		start = timer()

		for i in range(n_tests):
			controller.read_book(i)

		time_results[ci].append((timer() - start) / n_tests)

		# 5th test checks updating author records ( no references/relations  )
		start = timer()

		for i in range(n_tests):
			controller.update_author(i, up_authors[i])

		time_results[ci].append((timer() - start) / n_tests)

		# 6th test checks updating book records   ( yes references/relations )
		start = timer()

		for i in range(n_tests):
			controller.update_book(i, up_books[i])

		time_results[ci].append((timer() - start) / n_tests)

		# 7th test checks deleting author records ( no references/relations  )
		start = timer()

		for i in range(n_tests):
			controller.delete_author(i)

		time_results[ci].append((timer() - start) / n_tests)

		# 8th test checks deleting book records   ( yes references/relations )
		start = timer()

		for i in range(n_tests):
			controller.delete_book(i)

		time_results[ci].append((timer() - start) / n_tests)

		print(controller.name, "testing complete")

	print("All controller tests complete")
	for i, _ in enumerate(controllers):
		print(f"\nController #{i} results:")
		print("Test #1\t| Test #2\t| Test #3\t| Test #4\t| Test #5\t| Test #6\t| Test #7\t| Test #8\t|")
		for result in time_results[0]:
			result *= 1000
			print(f"{result:.2f}ms", end="\t| ")

	print("")

