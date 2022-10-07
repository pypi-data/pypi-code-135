# dictionary에 해당 key값이 없으면 그 key에 _Dict를 할당해서 반환하는 dictionary 클래스입니다.
class _Dict(dict):
    """
    dictionary에 해당 key값이 없으면 그 key에 _Dict를 할당해서 반환하는 dictionary 클래스입니다.
    - 매커니즘
        if key not in self:
            self[key] = _Dict()

    - key 값으로 내부 딕셔너리까지 재귀함수로 정렬시키는 sort_by_key 메소드를 추가했습니다.
    - dict 자료형을 _Dict로 형변환하는 dict_to_Dict 메소드를 추가 구현했습니다.
    """

    def __missing__(self, key):
        self[key] = _Dict()
        return self[key]

    def sort_by_key(self, *, is_return: bool = False) -> dict:
        """
        인스턴스 메소드로, self dict 데이터를 key 값으로 정렬합니다.
        - is_return값이 True이면 기존 값을 정렬시키고 None 값을 반환하고,
                      False이면 기존값은 그대로 유지시킨채 정렬된 값을 반환합니다.
        """
        # print("old_self:", self)
        new_self = _Dict()

        for key, val in sorted(self.items()):
            if isinstance(val, _Dict) or isinstance(val, dict):
                if not is_return:
                    _Dict.dict_sort_by_key(val)
                else:
                    val = _Dict.dict_sort_by_key(val)
            new_self[key] = val

        if not is_return:
            self.clear()
            self.update(new_self)
        else:
            return new_self

    @classmethod
    def dict_sort_by_key(cls, old_dict: dict, *, is_return: bool = False) -> dict:
        """
        클래스 메소드로, dict 데이터를 key 값으로 정렬합니다.
        - is_return값이 True이면 기존 값을 정렬시키고 None 값을 반환하고,
                        False이면 기존값은 그대로 유지시킨채 정렬된 값을 반환합니다.
        """
        new_dict = _Dict()

        for key, val in sorted(old_dict.items()):
            if isinstance(val, _Dict) or isinstance(val, dict):
                if not is_return:
                    _Dict.dict_sort_by_key(val)
                else:
                    val = _Dict.dict_sort_by_key(val)
            new_dict[key] = val

        if is_return:
            old_dict.clear()
            old_dict.update(new_dict)
        else:
            return new_dict

    @classmethod
    def dict_to_Dict(cls, dict_data: dict):
        """dict_data를 _Dict 구조로 바꿉니다."""
        new_dict = _Dict()

        for key, val in sorted(dict_data.items()):
            if isinstance(val, dict):
                new_dict[key] = _Dict.dict_to_Dict(val)
            else:
                new_dict[key] = val

        return new_dict
