class Paginator:
    # add_response_metadata
    @staticmethod
    def describe_allpages(func, *, allpages: bool = True, metaData: bool = False, **params: dict) -> list or dict:
        """
        주어진 func 에 매개변수 Key=Value,... 형식의 **params를 부여해서 메소드를 호출하고 반환한다.
        - allpages 의 Default 값은 True 이며, Next 반복문을 돌아서 끝까지 모두 호출후에 반환한다.
            - False 이면, 끝까지 반복하지 않고 1번만 수행한 값을 반환한다.
        - metaData 의 Default 값은 False 이며, list 값을 반환한다.
            - True 이면, MetaData를 포함시켜서 dict 값을 반환한다.
        """

        # params['MaxResults'] = 1000
        # print(f" func: {func!r} \n metaData: {metaData!r} \n allpages: {allpages!r} \n params: {params!r} \n")
        ret = dict()
        while True:
            response = func(**params)
            if len(ret) == 0:
                ret = response
            else:
                for key, item in ret.items():
                    if type(item) == list:
                        item.extend(response[key])

            if allpages:
                if "NextToken" in response:
                    params["NextToken"] = response["NextToken"]
                elif "NextMarker" in response:
                    params["Marker"] = response["NextMarker"]
                elif "PaginationToken" in response:
                    params["PaginationToken"] = response["PaginationToken"]
                else:
                    break
            else:
                break

        if not metaData:
            for key, item in ret.items():
                if type(item) == list:
                    ret = item
                    break
        return ret
