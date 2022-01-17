#!/usr/bin/python

from dotenv import dotenv_values
from timeit import default_timer as timer

from gen_test_data import gen_test_data
from NanoController import NanoController
from OracleController import OracleController

controllers = [
	NanoController("http://127.0.0.1:3000"),
	OracleController("localhost:1521/ztbd", r"C:\instantclient_21_3")
]


def run_with_parameters(
	n_tests,
	test_c_authors=True, test_c_books=True,
	test_r_authors=True, test_r_books=True,
	test_u_authors=True, test_u_books=True,
	test_d_authors=True, test_d_books=True):

	time_results = []

	print("Generating test data...")
	(cr_authors, cr_books, up_authors, up_books) = gen_test_data(n_tests)
	print("Test data generated")

	# Start tests
	for ci, controller in enumerate(controllers):
		time_results.append([None, None, None, None, None, None, None, None])

		print("Testing", controller.name, "...")

		# Test creating author records (no references/relations)
		start = timer()

		for i in range(n_tests):
			controller.create_author(i, cr_authors[i])

		if test_c_authors:
			time_results[ci][0] = (timer() - start) / n_tests

		# Test creating book records (yes references/relations)
		start = timer()

		for i in range(n_tests):
			controller.create_book(i, cr_books[i])

		if test_c_books:
			time_results[ci][1] = (timer() - start) / n_tests

		# Test reading author records (no references/relations)
		if test_r_authors:
			start = timer()

			for i in range(n_tests):
				controller.read_author(i)

			time_results[ci][2] = (timer() - start) / n_tests

		# Test reading book records (yes references/relations)
		if test_r_books:
			start = timer()

			for i in range(n_tests):
				controller.read_book(i)

			time_results[ci][3] = (timer() - start) / n_tests

		# Test updating author records (no references/relations)
		if test_u_authors:
			start = timer()

			for i in range(n_tests):
				controller.update_author(i, up_authors[i])

			time_results[ci][4] = (timer() - start) / n_tests

		# Test updating book records (yes references/relations)
		if test_u_books:
			start = timer()

			for i in range(n_tests):
				controller.update_book(i, up_books[i])

			time_results[ci][5] = (timer() - start) / n_tests

		# Test deleting author records (no references/relations)
		start = timer()

		for i in range(n_tests):
			controller.delete_author(i)

		if test_d_authors:
			time_results[ci][6] = (timer() - start) / n_tests

		# Test deleting book records (yes references/relations)
		start = timer()

		for i in range(n_tests):
			controller.delete_book(i)

		if test_d_books:
			time_results[ci][7] = (timer() - start) / n_tests

		print(controller.name, "testing complete")

	# Print out the results
	print("All controller tests complete")
	for ci, controller in enumerate(controllers):
		print(f"\n{controller.name} results:")

		for ti, result in enumerate(time_results[ci]):
			if result is None:
				continue

			print((
				"\tAuthor creation", "\tBook creation",
				"\tAuthor reading", "\tBook reading",
				"\tAuthor updating", "\tBook updating",
				"\tAuthor deletion", "\tBook deletion")[ti], end=" test:\t")

			result *= 1000
			print(f"{result:.2f}ms")

	print("")


# Read .env and run the tests
if __name__ == "__main__":
	config = dotenv_values(".env")
	run_with_parameters(
		int(config["N_TESTS"]),
		test_c_authors=config["TEST_C_AUTHORS"] == "TRUE",
		test_c_books=config["TEST_C_BOOKS"] == "TRUE",
		test_r_authors=config["TEST_R_AUTHORS"] == "TRUE",
		test_r_books=config["TEST_R_BOOKS"] == "TRUE",
		test_u_authors=config["TEST_U_AUTHORS"] == "TRUE",
		test_u_books=config["TEST_U_BOOKS"] == "TRUE",
		test_d_authors=config["TEST_D_AUTHORS"] == "TRUE",
		test_d_books=config["TEST_D_BOOKS"] == "TRUE",
	)
