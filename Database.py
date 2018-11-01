import pymysql


class Database_manager:
    _db = None;
    _cursor = None

    def __init__(self):
        # TODO inicializar conexão banco
        self._connection = pymysql.connect("localhost", "root", "", "mercadao")
        self._cursor = self._connection.cursor();
        self.create_tables_if_not_exists()

    # create tables
    def create_tables_if_not_exists(self):
        sql = """CREATE TABLE IF NOT EXISTS produtos ( \
            id int(3) NOT NULL AUTO_INCREMENT, \
            codigo int(16) NOT NULL, \
            descricao text, \
            unidade_medida VARCHAR(4), \
            preco float NOT NULL, \
            preco_venda float NOT NULL, \
            PRIMARY KEY (id) \
        )"""
        self.execute_query(sql)
        sql = """CREATE TABLE IF NOT EXISTS clientes ( \
            id int(3) NOT NULL AUTO_INCREMENT, \
            nome VARCHAR(255) NOT NULL, \
            cpf VARCHAR(15) NOT NULL, \
            email VARCHAR(255), \
            telefone VARCHAR(255), \
            PRIMARY KEY (id) \
        )"""
        self.execute_query(sql)

    # insert into tables
    def insert_into_clientes(self, nome, cpf, email, telefone):
        sql = """INSERT INTO clientes 
        (nome, cpf, email, telefone) 
        VALUES ('{0}', '{1}', '{2}', '{3}')""".format(nome, cpf, email, telefone)
        self.execute_query(sql)

    def insert_into_produtos(self, codigo, descricao, unidade_medida, preco, preco_venda):
        sql = """INSERT INTO produtos 
        (codigo, descricao, unidade_medida, preco, preco_venda) 
        VALUES ({0}, {1}, {2}, {3}, {4})""".format(codigo, descricao, unidade_medida, preco, preco_venda)
        self.execute_query(sql)

    # query
    def execute_query(self, query):
        res = None;
        try:
            res = self._cursor.execute(query);
        except (pymysql.MySQLError) as e:
            print("Erro na consulta: {} " .format(e));

        return res

    # select
    def get_all_products(self):
        sql = "SELECT * FROM produtos;"
        return self.execute_query(sql)

    def get_product_by_id(self, id):
        sql = "SELECT * FROM produtos WHERE id = {0};".format(id)
        return self.execute_query(sql)

    def get_client_by_id(self, id):
        sql = "SELECT * FROM clientes WHERE id = {0};".format(id)
        return self.execute_query(sql)

    # delete
    def delete_product(self, id):
        sql = "DELETE FROM produtos WHERE id = {0};".format(id)
        self.execute_query(sql)

    def delete_client(self, id):
        sql = "DELETE FROM clientes WHERE id = {0};".format(id)
        self.execute_query(sql)

    # close connection
    def close_connection(self):
        # TODO fechar conexão com banco
        pass
