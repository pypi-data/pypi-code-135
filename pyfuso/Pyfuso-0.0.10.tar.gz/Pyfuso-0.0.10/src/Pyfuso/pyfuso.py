
# 157 paises
# from time import timezone
from datetime import datetime, timedelta,timezone
class Pyfuso():
    """ Classe utilizada para representar os fuso horários
    ...

    Atributos
    ----------
    locais : str
        variável utilizada para armazenar os nomes de todos os países com fusos horarios disponíveis 
    UTC : str
        variávels utilizada para armazenar todas as variações de fusos horarios relacionando o país com a cidade 
    
    Metodos
    ---------
    get_local()
        Printa todos os locais disponíveis para a conversão de fuso horário

    get_data(local,formato = '%d/%m/%Y %H:%M')
        Retorna a data e hora relativa ao local determinado no formato padrão brasileiro
    
    get_hora(local,formato = '%H:%M:%S')
        Retorna apenas a hora relativa ao local determinado no formato brasileiro  

    get_data_formato(local,formato)
        Retorna a data e hora relativa ao local determinado no formato determinado
    
    get_time_diff(local1,local2)
        Retorna a diferença de horas entre dois locais determinados pelo usuário
    """
    def __init__(self):
        self.locais = ['Afeganistão','Angola','Emirados Árabes Unidos', 'Argentina', 'Arménia','Antártida','Austrália','Áustria','Azerbaijão','Burundi','Bélgica','Benin','Burkina Faso','Bangladesh','Bulgária','Bahamas','Bósnia e Hezergovina','Bielorussia','Belize','Bolivia','Brasil','Butão','Botswana','República Centro-Africa',
        'Canadá','Suiça','Chile','China','Costa do Marfim','Camarões','República Democrática do Congo','Congo','Colômbia','Cuba','Chipre','Chéquia','Alemanha','Djibouti','Dinamarca','República Dominicana','Argélia','Equador','Egito','Eritreia','Espanha','Estônia','Etiopia','Finlândia','Ilhas Malvinas','França','Gabão','Reino Unido',
        'Geórgia','Gana','Guiné','Gâmbia','Guiné-Bissau','Guiné Equatorial','Grécia','Guatemala','Guiana Francesa','Honduras','Croácia','Haiti','Hungria','Indonésia','Índia','Irlanda','Irão','Iraque','Islandia','Israel','Itália','Jordânia','Japão','Cazaquistão','Quénia','Quirquistão','Camboja','Coreia do Sul','Kuwait','Laos','Líbano',
        'Libéria','Líbia','Sri Lanka','Lesoto','Lituânia','Luxemburgo','Letónia','Marrocos','Moldavia','Madagascar','México','Macedónia do Norte','Mali','Myanmar','Montenegro','Mongólia','Moçambique','Mauritânia','Malawi','Malásia','Namíbia','Nova Caledónia','Níger','Nigéria','Nicaragua','Holanda','Noruega','Nepal','Nova Zelândia','Omã',
        'Paquistão','Panamá','Peru','Filipinas','Papau Nova Guiné','Polônia','Coreia do Norte','Portugal','Paraguai','Roménia','Rússia','Ruanda','Arábia Saudita','Sudão','Sudão do Sul','Senegal','Serra Leoa','Somália','Sérvia','Suriname','Eslováquia','Eslovénia','Suécia','Suazilândia','Síria','Togo','Tailândia','Tajiquistão','Turquemenistão',
        'Timor-Leste','Tunísia','Turquia','Ilha Formosa','Uganda','Ucrênia','Uruguai','Estados Unidos','Uzbequistão','Venezuela','Palestina','Iémen','África do Sul','Zâmbia','Zimbabwe']
        
        self.UTC = [('Burkina Faso/Ouagadougou','Costa do Marfim/Abidjan','Gana/Acra','Guiné/Conacri','Gâmbia/Banjul','Guiné-Bissau/Bissau','Islândia/Reiquiavique','Libéria/Monróvia','Mali/Bamako','Mauritânia/Nouakchott','Senegal/Dacar',	'Serra Leoa/Freetown','Togo/Lomé'),
        ('Benin/Porto-Novo','República Centro-Africana/Bangui','Camarões/Douala','República Democrática do Congo/Quinxassa','Congo/Brazzaville','Angola/Luanda','Argélia/Argel','Gabão/Libreville'	,'Guiné Equatorial/Malabo'	,'Irlanda/Dublin'	,'Reino Unido/Londres','Marrocos/Casablanca','Níger/Niamey'	,'Nigéria/Lagos','Tunísia/Tunes','Portugal/Lisboa'),
        ('Áustria/Viena','Burundi/Bujumbura','Bélgica/Bruxelas','Bósnia e Herzegovina/Sarajevo','Botswana/Gaborone','Suíça/Zurique','República Democrática do Congo/Lubumbashi','Chéquia/Praga','Alemanha/Berlim','Alemanha/Büsingen','Djibouti/Djibouti','Dinamarca/Copenhaga','Espanha/Madrid','Espanha/Ceuta','Egito/Cairo','França/Paris','Croácia/Zagreb','Hungria/Budapeste','Itália/Roma','Líbia/Trípoli','Lesoto/Maseru','Luxemburgo/Luxemburgo','Macedónia do Norte/Escópia','Montenegro/Podgorica','Malawi/Blantyre','Namíbia/Vinduque','Moçambique/Maputo','Holanda/Amesterdão','Noruega/Polónia	Varsóvia','Rússia/Caliningrado','Ruanda/Kigali','Sudão/Cartum','Sudão do Sul/Juba','Sérvia/Belgrado','Eslováquia/Bratislava','Eslovénia/Liubliana','Suécia/Estocolmo','Suazilândia/Mbabane','África do Sul/Johannesburgo','Zâmbia/Lusaka','Zimbabwe/Harare'),
        ('Bulgária/Sófia','Bielorússia/Minsk','Chipre/Nicósia','Chipre/Famagusta','Eritreia/Asmara','Estónia/Tallinn','Etiópia/Adis Abeba','Finlândia/Helsínquia','Grécia/Atenas','Iraque/Bagdá','Israel/Jerusalém','Jordânia/Amã','Quénia/Nairóbi','Líbano/Beirute','Kuwait/Kuwait','Lituânia/Vilnius','Letónia/Riga','Moldávia/Chişinău','Madagáscar/Antananarivo','Roménia/Bucareste','Rússia/Volgogrado','Rússia/Moscou','Rússia/Kirov','Arábia Saudita/Riade','Somália/Mogadíscio','Síria/Damasco','Turquia/Istambul','Uganda/Kampala','Ucrânia/Uzhhorod','Ucrânia/Simferopol','Palestina/Gaza','Palestina/Hebrom','Iémen/Áden'),
        ('Irão/Teerã'),
        ('Emirados Árabes Unidos/Dubai','Arménia/Yerevan','Geórgia/Tiblíssi','Omã/Mascate','Rússia/Ulianovsk','Rússia/Saratov','Rússia/Samara','Rússia/Astracã','Azerbeijão/Bacu'),
        ('Afeganistão/Cabul'),
        ('Cazaquistão/Oral','Cazaquistão/Atyrau','Rússia/Yekaterinburg','Paquistão/Carachi','Tajiquistão/Dushanbe','Turquemenistão/Asgabate','Uzbequistão/Samarcanda','Uzbequistão/Tashkent'),
        ('Índia/Calcutá','Sri Lanka/Colombo'),
        ('Nepal/Catmandu'),
        ('Bangladesh/Daca','Butão/Thimbu','China/Urumqi','Cazaquistão/Almaty','Quirguistão/Bisqueque','Rússia/Omsk'),
        ('Myanmar/Rangum'),
        ('Indonésia/Pontianak','Indonésia/Jakarta','Camboja/Pnom Pene','Laos/Vienciana','Rússia/Tomsk','Rússia/Novosibirsk','Rússia/Novokuznetsk','Rússia/Krasnoyarsk','Rússia/Barnaul','Tailândia/Bancoque'),
        ('Austrália/Perth','Indonésia/Macassar','Mongólia/Choibalsan','Rússia/Irkutsk','Ilha Formosa/Taipé','Filipinas/Manila','Malásia/Kuala Lumpur','Malásia/Kuching','China/Xangai'),
        ('Indonésia/Jayapura','Japão/Tóquio','Coreia do Sul/Seul','Coreia do Norte/Pionguiangue','Rússia/Yakutsk','Rússia/Chita','Timor-Leste/Díli'),
        ('Austrália/Darwin','Austrália/Adelaide','Austrália/Broken Hill'),
        ('Austrália/Sydney','Austrália/Melbourne','Austrália/Hobart','Austrália/Currie','Austrália/Brisbane','Papua Nova Guiné/Port Moresby','Rússia/Vladivostok'),
        ('Rússia/Magadan','Nova Caledónia/Nouméa'),
        ('Rússia/Anadyr'),
        ('Nova Zelândia/Auckland','Antártida/Estação McMurdo'),
        ('Argentina/Buenos Aires','Argentina/Ushuaia','Argentina/San Luis','Argentina/San Juan','Argentina/Salta','Argentina/Río Gallegos','Argentina/Mendoza','Argentina/Rioja','Argentina/Córdova','Brasil/Santarém','Brasil/Recife','Brasil/Maceió','Brasil/Fortaleza','Brasil/Belém','Brasil/Araguaina','Brasil/São Paulo','Brasil/Brasília','Canadá/Glace Bay','Canadá/Moncton','Canadá/Halifax','Chile/Santiago do Chile','Chile/Punta Arenas','Ilhas Malvinas/Port Stanley','Guiana Francesa/Caiena','Suriname/Paramaribo','Uruguai/Montevidéu'),
        ('Bahamas/Nassau','Bolívia/La Paz','Brasil/Campo Grande','Brasil/Cuiabá','Brasil/Porto Velho','Brasil/Manaus','Brasil/Boa Vista','Canadá/Iqaluit','Canadá/Pangnirtung','Canadá/Thunder Bay','Canadá/Toronto','Cuba/Havana','República Dominicana/Santo Domingo','Haiti/Porto Príncipe','Paraguai/Assunção','Estados Unidos/Indianápolis','Estados Unidos/Marengo','Estados Unidos/Petersburg','Estados Unidos/Vevay','Estados Unidos/Vincennes','Estados Unidos/Louisville','Estados Unidos/Monticello','Estados Unidos/Winamac','Estados Unidos/Detroit','Estados Unidos/Nova Iorque','Venezuela/Caracas'),
        ('Brasil/Rio Branco','Brasil/Eirunepe','Canadá/Atikokan','Canadá/Rankin Inlet','Canadá/Winnipeg','Equador/Guaiaquil','Colômbia/Bogotá','México/Merida','México/Cidade do México','México/Cancún','México/Monterrey','Panamá/Panamá','Perú/Lima','Estados Unidos/Tell City','Estados Unidos/Chicago','Estados Unidos/Knox','Estados Unidos/Menominee','Estados Unidos/Beulah','Estados Unidos/Center','Estados Unidos/New Salem'),
        ('Belize/Belize','Canadá/Edmonton','Canadá/Inuvik','Canadá/Regina','Canadá/Swift Current','Canadá/Yellowknife','Guatemala/Cidade da Guatemala','Honduras/Tegucigalpa','México/Mazatlán','México/Ojinaga','México/Chihuahua','Nicarágua/Manágua','Estados Unidos/Boise'),
        ('Canadá/Creston','Canadá/Dawson Creek','Canadá/Fort Nelson','Canadá/Vancôver','Canadá/Whitehorse','Canadá/Dawson','México/Tijuana','México/Hermosillo','Estados Unidos/Phoenix','Estados Unidos/Los Angeles'),
        ('Estados Unidos/Juneau','Estados Unidos/Metlakatla','Estados Unidos/Sitka','Estados Unidos/Yakutat','Estados Unidos/Nome','Estados Unidos/Anchorage'),
        ('Estados Unidos/Honolulu')
        ]

    def get_local(self):
        """
        Descrição
        --------
        Mostra na tela todas os países disponíveis para a conversão de fuso horario
        """
        for x in self.locais:
            print(x)
    
    def get_data(self,local,formato = '%d/%m/%Y %H:%M'):
        """
            Retorna o fuso horario convertido de acordo com o local determinado pelo usuário, 
            se o argumento 'formato' não for passado, o valor padrão será o formato brasileiro

            Parametros
            ----------
            local : str
                representa o país no qual será convertido o fuso horario

                ex.: 'Brasil/Brasilia'

            formato : str, opcional 
                representa o formato da data e hora(default é o formato brasileiro)
        """


        if local in self.UTC[0][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+0)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[1][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+1)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[2][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+2)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto

        elif local in self.UTC[3][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+3)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto

        elif local in self.UTC[4][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+3.5)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto

        elif local in self.UTC[5][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+4)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto

        elif local in self.UTC[6][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+4.5)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto

        elif local in self.UTC[7][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+5)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[8][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+5.5)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[9][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+5.75)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[10][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+6)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[11][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+6.5)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[12][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+7)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[13][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+8)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[14][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+9)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[15][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+9.5)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[16][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+10)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[17][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+11)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[18][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+12)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[19][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=+13)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[20][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=-3)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[21][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=-4)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[22][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=-5)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[23][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=-6)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[24][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=-7)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[25][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=-8)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        elif local in self.UTC[26][:]:
            dataehora = datetime.now()
            diferenca = timedelta(hours=-10)
            fuso_horario = timezone(diferenca)

            data = dataehora.astimezone(fuso_horario)
            data_texto =  data.strftime(formato)
            return data_texto
        
    def get_hora(self,local,formato = '%H:%M:%S'):
        """
            Retorna a hora do local determinado

            Paramentros
            -----------
            local : str
                representa o país no qual será convertido o fuso horario

                ex.: 'Brasil/Brasilia'

            formato : str, opcional 
                representa o formato da hora(default é o formato brasileiro)    

                ex.: '%H:%M'
        """
        return self.get_data(local,formato)

    def get_data_formato(self,local,formato):

        """
            Retorna a data e hora do local determinado no formato determinado 

            Parametros
            ----------
            local : str
                Representa o país no qual será convertido o fuso horario

                ex.: 'Brasil/Brasilia'

            formato : str, obrigatório
                Representa o formato da data e hora determinado pelo usuário

                ex.: 'A/M/D' 
        """

        if formato == 'A/M/D':
            return self.get_data(local,'%Y/%m/%d %H:%M')
        elif formato == 'A/D/M':
            return self.get_data(local,'%Y/%d/%m %H:%M')
        elif formato == 'D/M/A':
            return self.get_data(local)
        elif formato == 'D/A/M':
            return self.get_data(local,'%d/%Y/%m %H:%M')
        elif formato == 'M/A/D':
            return self.get_data(local,'%m/%Y/%d %H:%M')
        elif formato == 'M/D/A':
            return self.get_data(local,'%m/%d/%Y %H:%M')
 
    def get_time_diff(self,local1,local2):
        """
            Retorna a subtração das horas entre dois locais com fusos horarios diferentes

            Parametros
            ----------
            local1 : str
                representa o primeiro fuso horario

                ex.: 'Brasil/Brasilia'
            local2 : str
                representa o segundo fuso horario

                ex.: 'Burkina Faso/Ouagadougou'
        """



        L1 = self.get_hora(local1)
        L2 = self.get_hora(local2)
        L1 = timedelta(seconds = int(L1[6:8])  ,minutes = int(L1[3:5]), hours = int(L1[0:2]))
        L2 = timedelta(seconds = int(L2[6:8])  ,minutes = int(L2[3:5]), hours = int(L2[0:2]))
        if L1 > L2:
            return L1 - L2
        else:
            return L2 - L1


