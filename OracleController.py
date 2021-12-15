import cx_Oracle

class OracleController():
	name = "OracleDB"

	def __init__(self, addr, ic_path):
		# Init connection, etc.
		self.addr = addr
		self.ic_path = ic_path
		self.conn = self.connect()

	def connect(self):
		cx_Oracle.init_oracle_client(lib_dir=self.ic_path)
		conn = cx_Oracle.connect(user="SYS", 
								 password="adminztbd",
                               	 dsn=self.addr,
                                 mode=cx_Oracle.SYSDBA)
		return conn	


	def create_author(self, identifier, data):
		addr = self._create_address("author", identifier)
		# Returns True if record was created, otherwise False
		return True

	def create_book(self, identifier, data):
		addr = self._create_address("book", identifier)
		data["id_aut"] = "REF::author:{}".format(data["id_aut"])
		# Returns True if record was created, otherwise False
		return True

	def read_author(self, identifier):
		addr = self._create_address("author", identifier)
		# Returns data read from database as parsed JSON
		return True

	def read_book(self, identifier):
		addr = self._create_address("book", identifier)
		# Returns data read from database as parsed JSON
		return True

	def update_author(self, identifier, data):
		# Returns True if record was updated, otherwise False
		return True

	def update_book(self, identifier, data):
		# Returns True if record was updated, otherwise False
		return True

	def delete_author(self, identifier):
		addr = self._create_address("author", identifier)
		# Returns True if record was deleted, otherwise False
		return True

	def delete_book(self, identifier):
		addr = self._create_address("book", identifier)
		# Returns True if record was deleted, otherwise False
		return True
