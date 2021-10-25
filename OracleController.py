class OracleController():
	name = "OracleDB"

	def __init__(self, addr):
		# Init connection, etc.
		raise NotImplementedError

	def create(self, table, identifier, data):
		# INSERT
		raise NotImplementedError

	def read(self, table, identifier):
		# SELECT
		raise NotImplementedError

	def update(self, table, identifier, data):
		# UPDATE
		raise NotImplementedError

	def delete(self, table, identifier):
		# DELETE
		raise NotImplementedError
