import rhinoMorph

class Rhino :
    
    def __init__(self, pos = [], 
                 *,
                 exclude_pos = [], filters = []) :
        """
    def __init__(self, pos = [], 
                 *,
                 exclude_pos = [], filters = []) :
            1. pos: 선택할 품사. 기본값은 모든 품사
                    품사 약자가 들어간 str 혹은 list
                        ex) "XR"
                            ["NNP", "VV"]
                    pos가 정해지지 않은 메소드는 이 pos가 파라미터로 들어간다
                    print_word_classes() 함수로 사용가능한 품사 목록을 볼 수 있다
            3. exclude_pos : 제외할 품사, 기본값은 빈 리스트
                            품사 약자가 들어간 str 혹은 list
                                ex) "XR"
                                    ["NNP", "VV"]
                             exclude_pos가 정해지지 않은 메소드는 이 exclude_pos가 파라미터로 들어간다
                             print_word_classes() 함수로 사용가능한 품사 목록을 볼 수 있다
            2. filters : 불용어 목록, 기본값은 빈 값
                         이 값에 포함된 값은 결과에서 제외됨.
                         불용어가 들어간 str 혹은 list
                             ex) "뭐"
                                 ["이놈아", "는"]
                         filters의 리스트에 포함된 단어나 형태소는 onlyMorph_list() 와 wholeResult_list() 함수로 반환되지 않음
        """
        # 타입이 str 인 경우 다르게 처리
        def handle_str(parameter) :
            if isinstance(parameter, str) :
                parameter = [parameter]
            else :
                parameter = list(set(parameter))
            return parameter

        self.rn = rhinoMorph.startRhino()
        
        # 파라미터 handling
        if pos :
            self.pos = handle_str(pos)
        else :
            self.pos = ["NNG", "NNP", "NNB", "NP", "NR", "VV", "VA", "VX", "VCP", "VCN", "MM", "MAG", "MAJ", "IC",
                        "JKS", "JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JX", "JC",
                        "EP", "EF", "EC", "ETN", "ETM", "XPN", "XSN", "XSV", "XSA", "XR",
                        "SF", "SS", "SP", "SE", "SO", "SL", "SH", "SN", "SW"]
            
        if filters :
            self.filters = handle_str(filters)
        else :
            self.filters = []
            
        if exclude_pos :
            self.exclude_pos = handle_str(exclude_pos)
        else :
            self.exclude_pos = []
        
        self.word_classes = {
            "noun" : """
        - 명사 계열
        일반명사(NounNounGeneral, NNG) 
        고유명사(NounNounPerson, NNP) 
        의존명사(NounNounBojo, NNB) 
        대명사(NounPerson, NP) 
        수사(NumbeR, NR) 
        동사(Verb Verb, VV) 
        형용사(Verb Adjective, VA) 
        보조용언(Verb eXtended, VX) 
        긍정지정사(Verb Complement Positive, VCP)
        부정지정사(Verb Complement Negative, VCN)
        관형사(Modifier Modifier, MM) 
        일반부사(Modifier Adjective General, MAG)
        접속부사(Modifier Adjective Jupsok, MAJ)
        감탄사(InterjeCtion, IC)
            """,
            "josa" : """
        - 조사 계열 
        주격조사(Josa Kyok Subjective, JKS) 
        보격조사(Josa Kyok Complement, JKC) 
        관형격조사(Josa Kyok Genitive, JKG) 
        목적격조사(Josa Kyok Objective, JKO) 
        부사격조사(Josa Kyok Boosa, JKB) 
        호격조사(Josa Kyok Vocative, JKV) 
        인용격조사(Josa Kyok Quotation, JKQ) 
        보조사(Josa auXiliary, JX) :
        접속조사(Josa Connection, JC)
            """,
            "eomi" : """
        - 어미 계열 
        선어말어미(Eomi Preposition, EP)
        종결어미(Eomi Final, EF) :
        연결어미(Eomi Connection, EC) 
        명사형전성어미(Eomi Transitive Noun, ETN) 
        관형형전성어미(Eomi Transitive Modifier, ETM) 
        체언접두사(XPN) 
        명사파생접미사(eXtended Suffix Noun, XSN) 
        동사파생접미사(eXtended Suffix Verb, XSV)
        형용사파생접미사(eXtended Suffix Adjective, XSA)
        어근(eXtended Root, XR)
            """,
            "sign" : """
        - Sign 계열 
        마침표, 물음표, 느낌표(Sign Final, SF) 
        따옴표, 괄호표, 줄표(SS) 
        쉼표, 가운뎃점, 콜론, 빗금(SP) 
        줄임표(Sign Ending, SE) 
        붙임표(물결, 숨김, 빠짐)(SO) 
        외국어(Sign Language, SL) 
        한자(Sign Hanja, SH) 
        숫자(Sign Number, SN) 
        기타기호(논리수학기호, 화폐기호)(SW)
            """
        }

    def onlyMorph_list(self, input, pos = [], 
                       *,
                       exclude_pos = [], filters = [], 
                       eomi = False, combineN = False, xrVv = False) -> list :
        """
    def onlyMorph_list(self, input, pos = [], 
                       *,
                       exclude_pos = [], filters = [], 
                       eomi = False, combineN = False, xrVv = False) -> list :
        형태소 분석 결과를 Python의 리스트로 가지고 오되, 지정된 품사의 형태 부분만 가져온다
            1. input: 입력문 또는 문장 리스트(list), 튜플(tuple)
            2. pos: 선택할 품사. 기본값은 모든 품사
                    품사 약자가 들어간 str 혹은 list
                        ex) "XR"
                            ["NNP", "VV"]
                    입력되지 않으면 __init__()의 pos를 사용한다
            3. exclude_pos : 제외할 품사. 기본값은 빈 리스트
                            품사 약자가 들어간 str 혹은 list
                                ex) "XR"
                                    ["NNP", "VV"]
                             입력되지 않으면 __init__()의 exclude_pos를 사용한다
            4. filters : 불용어 목록, 기본값은 빈 리스트
                         이 값에 포함된 값은 결과에서 제외됨.
                         불용어가 들어간 str 혹은 list
                             ex) "뭐"
                                 ["이놈아", "는"]
                         입력되지 않으면 __init__()의 filters를 사용한다
            5. eomi: 어말어미 부착 여부, 기본값은 부착없이 원형 사용
            6. combineN: True시 하나의 어절 내에서 연속된 NNG, NNP를 하나의 NNG로 연결한 뒤, morphs, poses 결과를 출력
            7. xrVv: XR+하 형태를 동사로 변환할 것인지 여부
        """
        # 타입이 str 인 경우 다르게 처리
        def handle_str(parameter) :
            if isinstance(parameter, str) :
                parameter = [parameter]
            else :
                parameter = list(set(parameter))
            return parameter
        
        # 불용어 처리
        def filter_stopwords(input) :
            if input in filters :
                return False
            return True
        
        def tokenize(input) :
            input = str(input)
            result = rhinoMorph.onlyMorph_list(self.rn, input, pos, eomi, combineN, xrVv)
            if filters :
                result = list(filter(filter_stopwords, result))
            return result

        # 파라미터 handling
        if pos :
            pos = handle_str(pos)
        else :
            pos = self.pos
            
        if filters :
            filters = handle_str(filters)
        else :
            filters = self.filters  
            
        if exclude_pos :
            exclude_pos = handle_str(exclude_pos)
        else :
            exclude_pos = self.exclude_pos  
            
        pos = list(set(pos) - set(exclude_pos))
        
        # 토크나이징
        result = []
        if isinstance(input, str) :
            result = tokenize(input)
        else :
            result = list(map(tokenize, input))
        
        return result
    
    def wholeResult_list(self, input, pos = [], 
                         *,
                         exclude_pos = [], filters = [],
                         eomi = False, combineN = False, xrVv = False) -> list :
        """
    def wholeResult_list(self, input, pos = [], 
                         *,
                         exclude_pos = [], filters = [],
                         eomi = False, combineN = False, xrVv = False) -> list :
        형태소 분석 결과를 Python의 (morph, pos) 형태의 튜플을 요소로 가지는 리스트 반환한다
            1. input: 입력문 또는 문장 리스트(list), 튜플(tuple)
            2. pos: 선택할 품사. 기본값은 모든 품사
                    품사 약자가 들어간 str 혹은 list
                        ex) "XR"
                            ["NNP", "VV"]
                    입력되지 않으면 __init__()의 pos를 사용한다
            3. exclude_pos : 제외할 품사. 기본값은 빈 리스트
                            품사 약자가 들어간 str 혹은 list
                                ex) "XR"
                                    ["NNP", "VV"]
                             입력되지 않으면 __init__()의 exclude_pos를 사용한다
            4. filters : 불용어 목록, 기본값은 빈 리스트
                         이 값에 포함된 값은 결과에서 제외됨.
                         불용어가 들어간 str 혹은 list
                             ex) "뭐"
                                 ["이놈아", "는"]
                         입력되지 않으면 __init__()의 filters를 사용한다
            5. eomi: 어말어미 부착 여부, 기본값은 부착없이 원형 사용
            6. combineN: True시 하나의 어절 내에서 연속된 NNG, NNP를 하나의 NNG로 연결한 뒤, morphs, poses 결과를 출력
            7. xrVv: XR+하 형태를 동사로 변환할 것인지 여부
        """
        # 타입이 str 인 경우 다르게 처리
        def handle_str(parameter) :
            if isinstance(parameter, str) :
                parameter = [parameter]
            else :
                parameter = list(set(parameter))
            return parameter
        
        # 불용어 처리
        def filter_stopwords(input) :
            if input[0] in filters :
                return False
            return True
        
        def tokenize(input) :
            input = str(input)
            # ([형태소 목록], [품사 목록])의 형태로 반환
            result = rhinoMorph.wholeResult_list(self.rn, input, pos, eomi, combineN, xrVv)
            # zip() 함수로 [[(형태소, 품사), (형태소, 품사), ...], [(형태소, 품사), ...],[...], ...]로 변환
            result = zip(result[0], result[1])
            if filters :
                result = list(filter(filter_stopwords, result))
            else : 
                result = list(result)
            return result
        
        # 파라미터 handling
        if pos :
            pos = handle_str(pos)
        else :
            pos = self.pos
            
        if filters :
            filters = handle_str(filters)
        else :
            filters = self.filters  
            
        if exclude_pos :
            exclude_pos = handle_str(exclude_pos)
        else :
            exclude_pos = self.exclude_pos  
            
        pos = list(set(pos) - set(exclude_pos))
        
        # 토크나이징
        result = []
        if isinstance(input, str) :
            result = tokenize(input)
        else :
            result = list(map(tokenize, input))
        
        return result
    
    def wholeResult_text(self, input,
                         *,
                         xrVv = False) -> str :
        """
    def wholeResult_text(self, input,
                         *,
                         xrVv = False) -> str :
        형태소 분석 결과를 TEXT로 된 원 분석 결과 형태(str)로 가지고 온다
            1. input: 입력문(str) 또는 문장 리스트(list), 튜플(tuple)
            2. xrVv: XR+하 형태를 동사로 변환할 것인지 여부
        """
        def tokenize(input) :
            input = str(input)
            return rhinoMorph.wholeResult_text(self.rn, input, xrVv)
        
        if isinstance(input, str) :
            result = tokenize(input)
        else :
            result = list(map(tokenize, input))
        
        return result

    def print_word_classes(self, type = ["noun", "josa", "eomi", "sign"]) -> None :  
        """
    def print_word_classes(self) -> None :
        사용 가능한 품사 종류를 출력한다,
        1. type : "noun", "josa", "eomi", "sign"이 요소로 쓰인 리스트
                  기본값은 ["noun", "josa", "eomi", "sign"]
        """
        word_classes_str = ""
        for t in type : 
            word_classes_str += self.word_classes[t]
                
        print(word_classes_str)
    
    # Rhino 클래스의 Doc String
    __doc__ = __init__.__doc__ + \
            onlyMorph_list.__doc__ + \
            wholeResult_list.__doc__ + \
            wholeResult_text.__doc__ + \
            print_word_classes.__doc__