import json
import requests


class NanoController():
	name = "NanoDB"

	def __init__(self, addr):
		self.addr = addr

	def _create_address(self, table, identifier):
		return "{}/{}:{}".format(self.addr, table, identifier)

	def create_author(self, identifier, data):
		addr = self._create_address("author", identifier)
		# Returns True if record was created, otherwise False
		return requests.put(addr, data=json.dumps(data)).ok

	def create_book(self, identifier, data):
		addr = self._create_address("book", identifier)
		_data = data.copy()
		_data["id_aut"] = "REF::author:{}".format(data["id_aut"])
		# Returns True if record was created, otherwise False
		return requests.put(addr, data=json.dumps(_data, default=str)).ok

	def read_author(self, identifier):
		addr = self._create_address("author", identifier)
		# Returns data read from database as parsed JSON
		return requests.get(addr).json()

	def read_book(self, identifier):
		addr = self._create_address("book", identifier)
		# Returns data read from database as parsed JSON
		return requests.get(addr).json()

	def update_author(self, identifier, data):
		# Returns True if record was updated, otherwise False
		return self.create_author(identifier, data)

	def update_book(self, identifier, data):
		# Returns True if record was updated, otherwise False
		return self.create_book(identifier, data)

	def delete_author(self, identifier):
		addr = self._create_address("author", identifier)
		# Returns True if record was deleted, otherwise False
		return requests.delete(addr).ok

	def delete_book(self, identifier):
		addr = self._create_address("book", identifier)
		# Returns True if record was deleted, otherwise False
		return requests.delete(addr).ok
