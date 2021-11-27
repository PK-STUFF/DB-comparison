import random as rng
import string
from datetime import datetime as dt, timedelta


def _gen_string(N):
	return "".join(rng.choices(string.ascii_lowercase, k=N))


def _gen_date(start, end):
	return start + timedelta(
		seconds=rng.randint(0, int((end - start).total_seconds()))
	)


def gen_test_data(N):
	cr_authors = []
	cr_books   = []
	up_authors = []
	up_books   = []

	for i in range(N):
		cr_authors.append({
			"fname":   "andrzej",
			"lname":   "{}ski".format(_gen_string(5)),
			"country": "pl"
		})

		up_authors.append({
			"fname":   "andrzej",
			"lname":   "{}ski".format(_gen_string(5)),
			"country": "pl"
		})

		cr_books.append({
			"id_aut":   i,
			"title":    "saga o {}".format(_gen_string(8)),
			"price":    rng.randrange(5, 50),
			"pages":    rng.randrange(100, 500),
			"date_pub": _gen_date(dt.min, dt.now())
		})

		up_books.append({
			"id_aut":   i,
			"title":    "saga o {}".format(_gen_string(8)),
			"price":    rng.randrange(5, 50),
			"pages":    rng.randrange(100, 500),
			"date_pub": _gen_date(dt.min, dt.now())
		})

	return (cr_authors, cr_books, up_authors, up_books)
