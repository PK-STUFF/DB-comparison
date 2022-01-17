import cx_Oracle

class OracleController():
	name = "OracleDB"

	def __init__(self, addr, ic_path):
		# Init connection, etc.
		cx_Oracle.init_oracle_client(lib_dir=ic_path)
		self.addr = addr
		self.ic_path = ic_path

	def connect(self):
		conn = cx_Oracle.connect(user="SYS", 
								 password="adminztbd",
                               	 dsn=self.addr,
                                 mode=cx_Oracle.SYSDBA)
		return conn	


	def create_author(self, identifier, data):
		# Returns True if record was created, otherwise False
		cmd=f"insert into author(id_aut, fname, lname, country) values( {identifier}, '{data['fname']}', '{data['lname']}', '{data['country']}') returning id_aut into :id_aut"
		
		conn = self.connect()
		c = conn.cursor()
		id_aut_wrap = c.var(cx_Oracle.NUMBER)
		sql_params = { "id_aut" : id_aut_wrap }
		c.execute(cmd, sql_params)
		conn.commit()

		id_aut=id_aut_wrap.getvalue()
		if id_aut:
			return True
		else:
			return False

	def create_book(self, identifier, data):
		# Returns True if record was created, otherwise False
		cmd=f"insert into book(id_book, title, price, id_aut, pages, date_pub) values( {identifier}, '{data['title']}', {data['price']}, {data['id_aut']}, {data['pages']}, to_date('{data['date_pub']}', 'YYYY-MM-DD HH24:MI:SS')) returning id_book into :id_book"
		
		conn = self.connect()
		c = conn.cursor()
		id_book_wrap = c.var(cx_Oracle.NUMBER)
		sql_params = { "id_book" : id_book_wrap }
		c.execute(cmd, sql_params)
		conn.commit()

		id_book=id_book_wrap.getvalue()
		if id_book:
			return True
		else:
			return False

	def read_author(self, identifier):
		cmd = f"select * from author where id_aut ={identifier}"

		conn = self.connect()
		c = conn.cursor()
		c = conn.cursor()
		c.execute(cmd)

		return True

	def read_book(self, identifier):
		cmd = f"select * from author where id_aut ={identifier}"

		conn = self.connect()
		c = conn.cursor()
		c = conn.cursor()
		c.execute(cmd)
				
		return True

	def update_author(self, identifier, data):
		# Returns True if record was updated, otherwise False
		cmd=f"update author set fname='{data['fname']}', lname='{data['lname']}', country='{data['country']}' where id_aut={identifier} returning id_aut into :id_aut"
		
		conn = self.connect()
		c = conn.cursor()
		id_aut_wrap = c.var(cx_Oracle.NUMBER)
		sql_params = { "id_aut" : id_aut_wrap }
		c.execute(cmd, sql_params)
		conn.commit()

		id_aut=id_aut_wrap.getvalue()
		if id_aut:
			return True
		else:
			return False

	def update_book(self, identifier, data):
		# Returns True if record was updated, otherwise False
		cmd=f"update book set title='{data['title']}', price={data['price']}, id_aut={data['id_aut']}, pages={data['pages']}, date_pub=to_date('{data['date_pub']}', 'YYYY-MM-DD HH24:MI:SS') where id_book={identifier} returning id_book into :id_book"
		
		conn = self.connect()
		c = conn.cursor()
		id_book_wrap = c.var(cx_Oracle.NUMBER)
		sql_params = { "id_book" : id_book_wrap }
		c.execute(cmd, sql_params)
		conn.commit()

		id_book=id_book_wrap.getvalue()
		if id_book:
			return True
		else:
			return False

	def delete_author(self, identifier):
		# Returns True if record was deleted, otherwise False
		cmd=f"delete from author where id_aut={identifier} returning id_aut into :id_aut"
		
		conn = self.connect()
		c = conn.cursor()
		id_aut_wrap = c.var(cx_Oracle.NUMBER)
		sql_params = { "id_aut" : id_aut_wrap }
		c.execute(cmd, sql_params)
		conn.commit()

		id_aut=id_aut_wrap.getvalue()
		if id_aut:
			return True
		else:
			return False

	def delete_book(self, identifier):
		# Returns True if record was deleted, otherwise False
		cmd=f"delete from book where id_book={identifier} returning id_book into :id_book"
		
		conn = self.connect()
		c = conn.cursor()
		id_book_wrap = c.var(cx_Oracle.NUMBER)
		sql_params = { "id_book" : id_book_wrap }
		c.execute(cmd, sql_params)
		conn.commit()

		id_book=id_book_wrap.getvalue()
		if id_book:
			return True
		else:
			return False

