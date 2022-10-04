import mysql.connector
class FSP():
    """
    Cria um objeto de conexão com um banco de dados no sistema de gerenciamento de dados MySQL

    Permite a realização de instruções SQL através dos métodos nesta classe e que podem ser adaptados de acordo com os parâmetros  passados

    Attributes
    ----------
    conexao : class 'mysql.connector.connection_cext.CMySQLConnection'
        Objeto criado com a conexão ao banco de dados
    cursor : class 'mysql.connector.cursor_cext.CMySQLCursor' 
        Objeto quer permite a execução dos comando SQL no banco de dados
    
    Methods
    -------
    conectarBD(nomeBancoDeDados,enderecoDoBancoDeDados,nomeUsuarioDoBancoDeDados,senhaDoBancoDeDados)
        Tenta realizar a conexão a um banco de dados para permitir a utilização de outros métodos
    criarTabela(nomeTabela,nomeChavePrimaria)
        Cria uma tabela com uma coluna de chave primária
    limparDadosTabela(nomeTabela)
        Deleta as linhas de uma tabela
    excluirTabelaComDados(nomeTabela)
        Deleta a tabela
    adicionarColunaTabela(nomeTabela, nomeNovaColuna, stringComCaracteristicas,aposColuna='') 
        Adiciona uma coluna a uma tabela
    inserirDadosNaTabela(nomeTabela,colunas='',inserirValores='')
        Insere uma nova linha de dados em uma tabela
    atualizarDadosNaTabela(nomeTabela, colunaAlterada,novoValor,identificadorLinha,condicao,valorIdentificado)
        Permite alterar linhas de uma tabela para o valor enviado
    deletarDadosNaTabela(nomeTabela,colunaIdentificadora,condicaoFiltragem,valorFiltragem)
        Permite deletar linhas de uma tabela
    verTabelaCompleta(nomeTabela,colunasExibidas='*',filtrar=False,colunaFiltragem=None,condicaoFiltragem=None,valorFiltragem=None)    
        Retornar todas as linhas das colunas selecionada de uma tabela  
    """

    def __init__(self,nomeBancoDeDados,enderecoDoBancoDeDados='localhost',nomeUsuarioDoBancoDeDados='root',senhaDoBancoDeDados=''):
        """
        Parameters
        ----------
        nomeBancoDeDados : str 
            Nome do banco de dados a ser conectado
        enderecoDoBancoDeDados : str , optional
            Endereço do banco de dados (padrão é 'localhost')
        nomeUsuarioDoBancoDeDados : str , optional
            Nome do usuário que deseja conectar ao banco de dados (padrão é 'root')
        senhaDoBancoDeDados : str , optional
            Senha usada para se conectar ao banco de dados (padrão é '')
        """
        self.conexao = self.conectarBD(nomeBancoDeDados,enderecoDoBancoDeDados,nomeUsuarioDoBancoDeDados,senhaDoBancoDeDados)
        
    def conectarBD(self,nomeBancoDeDados,enderecoDoBancoDeDados,nomeUsuarioDoBancoDeDados,senhaDoBancoDeDados):
        """Tenta criar um objeto conectado ao banco de dados informado, e cria um atributo cursor para realizar as operações no banco.
        
        O atributo cursor só é criado se a conexão tiver sido criada.

        Parameters
        ----------
        nomeBancoDeDados : str
            Nome do banco de dados a ser conectado
        enderecoDoBancoDeDados : str
            Endereço do banco de dados
        nomeUsuarioDoBancoDeDados : str
            Nome do usuário que deseja conectar ao banco de dados
        senhaDoBancoDeDados : str 
            Senha usada para se conectar ao banco de dados

        Returns
        -------
        bool
            Retorna o valor booleano True se a tentativa de conexão tiver êxito, e False caso não consiga realizar a conexão
        """

        try:
            conexao = mysql.connector.connect(host=enderecoDoBancoDeDados,database=nomeBancoDeDados,user=nomeUsuarioDoBancoDeDados,password=senhaDoBancoDeDados)
            if conexao.is_connected():
                self.cursor = conexao.cursor()
                return conexao
            else:
                return False
        except:
            return False

    def criarTabela(self,nomeTabela,nomeChavePrimaria):
        """Cria uma tabela no banco de dados conectado.
        
        A tabela criada possuirá uma coluna para as chaves primárias, pois toda tabela criada precisa de pelo menos uma coluna.

        Attributes
        ----------
        nomeTabela : str 
            Nome da tabela a ser criada
        nomeChavePrimaria : str
            Nome da chave primária da tabela
        
        Returns
        -------
        bool
            Retorna o valor booleano True se a tabela for criada, e False caso a tabela não seja criada
        """

        try:
            self.cursor.execute(F'''CREATE TABLE IF NOT EXISTS {nomeTabela}(
	                                    {nomeChavePrimaria} int NOT NULL AUTO_INCREMENT,
	                                    PRIMARY KEY({nomeChavePrimaria})
                                    );''')
            return True
        except:
            return False

    def limparDadosTabela(self,nomeTabela):
        """Limpa as infomações da tabela selecionada no banco de dados.

        Deleta as linhas de tabela informada, a estrutura da tabela é mantida.

        Parameters
        ----------
        nomeTabela : str
            Nome da tabela que terá seus dados deletados

        Returns
        -------
        bool
            Retorna o valor booleano True todas as linhas da tabela forem deletadas, e False caso não seja possível realizar a deleção
        """

        try:
            self.cursor.execute(F'''TRUNCATE TABLE {nomeTabela};''')
            return True
        except:
            return False
    
    def excluirTabelaComDados(self,nomeTabela):
        """Exclui uma tabela selecionada no banco de dados.

        A estrutura e dados da tabela são apagados.

        Parameters
        ----------
        nomeTabela : str 
            Nome da tabela a ter a estrutura e dados deletados

        Returns
        -------
        bool
            Retorna o valor booleano True se a deleção da tabela e seus dados for feita, e False caso não seja possível deletar
        """

        try:
            self.cursor.execute(F'''DROP TABLE {nomeTabela};''')
            return True
        except:
            return False
    
    def adicionarColunaTabela(self, nomeTabela, nomeNovaColuna, stringComCaracteristicas,aposColuna=''):
        """Adiciona uma coluna na tabela selecionada.

        A novo coluna a ser inserida pode ser inserida no início, após determinada coluna ou no fim.

        Parameters
        ----------
        nomeTabela : str             
            Nome da tabela onde a coluna será adicionada
        nomeNovaColuna : str
            Nome da coluna que será adicionada
        stringComCaracterísticas : str 
            Atributos que a nova coluna possui, os atributos devem ser separados por um espaço
        aposColuna : str , optional
            Indica após qual coluna existente a nova coluna será adicionada (padrão é '')
        
        Returns
        -------
        bool
            Retorna o valor booleano True se a nova coluna for adicionada, e False caso não seja possível adicionar
        """

        try:
            stringComCaracteristicas = stringComCaracteristicas.split(' ')
        except:
            return False
        try:
            if aposColuna:
                sql = F'''ALTER TABLE {nomeTabela} ADD COLUMN {nomeNovaColuna}'''
                for atributo in stringComCaracteristicas:
                    sql += F" {atributo}"
                if aposColuna.upper() == "FIRST":
                    sql += F" FIRST;"
                else:
                    sql += F" AFTER {aposColuna};"
            else:
                sql = F'''ALTER TABLE {nomeTabela} ADD COLUMN {nomeNovaColuna}'''
                for atributo in stringComCaracteristicas:
                    sql += F" {atributo}"
                sql += ";"
            self.cursor.execute(sql)
            return True
        except:
            return False

    def inserirDadosNaTabela(self,nomeTabela,colunas='',inserirValores=''):
        """Insere dados na tabela selecionada.

        Os dados a serem inseridos são inseridos na ordem das colunas, strings a serem inseridas devem estar entre aspas duplas.

        Parameters
        ----------
        nomeTabela: str 
            Nome da tabela onde os dados serão adicionados
        colunas : str
            Colunas que receberão novos dados (padrão é '')
        inserirValores : str
            Valores a ser adicionados nas colunas selecionadas, os valores devem ser separados por vírgula (padrão é '')
        
        Returns
        -------
        bool
            Retorna o valor booleano True se os dados forem adicionados, e False caso não seja possível adicionar
        """

        try:
            if colunas:
                colunas = colunas.split(',')
                sql = F'''INSERT INTO {nomeTabela}('''
                for coluna in colunas:
                    sql += F"{coluna},"
                sql = sql[:-1]
                sql += ") VALUES("
                inserirValores = inserirValores.split(',')
                for valor in inserirValores:
                    sql += F"{valor},"
                sql = sql[:-1]
                sql += ");"
            else:
                sql = F'''INSERT INTO {nomeTabela} VALUES ('''
                for valores in inserirValores:
                    sql += valores
                sql += ');'
            self.cursor.execute(sql)
            return True
        except:
            return False

    def atualizarDadosNaTabela(self,nomeTabela, colunaAlterada,novoValor,identificadorLinha,condicao,valorIdentificado):
        """Atualiza dados em uma coluna na tabela selecionada.

        Os dados podem ser alterados em uma ou multiplas linhas dependendo dos parâmetros passados.

        Parameters
        ----------
        nomeTabela : str
            Nome da tabela onde o dado será alterado 
        colunaAlterada : str 
            Nome da coluna em que o dado será alterado
        novoValor : str 
            Novo valor da linha selecionada
        identificadorLinha : str 
            Nome da coluna para ser usada na condição para atualizar o valor
        condicao : str 
            Operador relacional a ser usada para fazer a condição para atualizar o valor
        valorIdentificado : str 
            Valor usado como referência para alterar o valor de uma linha

        Returns
        -------
        bool
            Retorna o valor booleano True se os dados forem atualizados, e False caso não seja possível atualizar
        """

        try:
            if isinstance(nomeTabela,str):
                sql = F"UPDATE {nomeTabela} SET {colunaAlterada} = '{novoValor}' WHERE {identificadorLinha} {condicao} {valorIdentificado}"
            else:
                sql = F"UPDATE {nomeTabela} SET {colunaAlterada} = {novoValor} WHERE {identificadorLinha} {condicao} {valorIdentificado}"
            self.cursor.execute(sql)
            return True
        except:
            return False

    def deletarDadosNaTabela(self, nomeTabela,colunaIdentificadora,condicaoFiltragem,valorFiltragem):
        """Deleta linhas de uma tabela selecionada.

        Deleta todas as linhas de uma tabela a partir de uma condição criada com os valores usados.

        Parameters
        ----------
        nomeTabela : str 
            Nome da tabela onde a linha será alterada
        colunaIdentificadora : str 
            Nome de da coluna para ser usada na condição para deletar a linha
        condicaoFiltragem : str 
            Operador relacional a ser usada para fazer a condição para deletar a linha
        stringComCaracterísticas : str 
            Atributos que a nova coluna possui
        valorIdentificado : str 
            Valor usado como referência para deletar uma linha

        Returns
        -------
        bool
            Retorna o valor booleano True se as linhas que cumprem a condição forem deletados, e False caso não seja possível deletar
        """

        try:
            sql = F"DELETE FROM {nomeTabela} WHERE {colunaIdentificadora} {condicaoFiltragem} {valorFiltragem};"
            self.cursor.execute(sql)
            return True
        except:
            return False

    def verTabelaCompleta(self,nomeTabela,colunasExibidas='*',filtrar=False,colunaFiltragem=None,condicaoFiltragem=None,valorFiltragem=None):
        """Permite a vizualização dos dados de uma tabela selecionada.

        Os dados retornados pertencem a tabela e coluna selecionadas também é possível fazer uma filtragem nos dados que retornarão.

        Parameters
        ----------
        nomeTabela : str 
            Nome da tabela a ter os dados retornados
        colunasExibidas : str 
            Colunas da tabela a ser retornadas (padrão é '*')
        filtrar : bool
            Permite fazer uma filtragem nas linhas da tabela (padrão é False)
        colunaFiltragem : None 
            Nome de da coluna para ser usada na condição para encontrar linhas a ser retornadas (padrão é None)
        condicaoFiltragem : None 
            Operador relacional a ser usada para fazer a condição para retornar a linha (padrão é None)
        valorFiltragem : None 
            Valor usado como referência para filtrar e retornar linhas (padrão é None)

        Returns
        -------
        list
            Retorna uma lista de tuplas que são as linhas da tabela, e False caso não haja valor a ser retornado
        """

        try:
            sql = F"SELECT "
            if colunasExibidas != '*':
                colunasExibidas = colunasExibidas.split(',')
                for colunas in colunasExibidas:
                    sql += F"{colunas},"
                sql = sql[:-1]
            else:
                sql += "*"
            sql += F" FROM {nomeTabela};"
            if filtrar:
                sql = sql[:-1]
                if isinstance(valorFiltragem,str):
                    sql += F" WHERE {colunaFiltragem} {condicaoFiltragem} '{valorFiltragem}';"
                else:
                    sql += F" WHERE {colunaFiltragem} {condicaoFiltragem} {valorFiltragem};"
            print(sql)
            self.cursor.execute(sql)
            dados = self.cursor.fetchall()
            return dados
        except:
            return False
