import boto3
from boto3.session import Session
from src.pkg_main_module import is_test_local_platform
from src.common._logging import logger

# 메인 root 세션 연결
profile_name = "assume-role-only-user" if is_test_local_platform else "sts-to-nds-role"
root_session = boto3.Session(region_name="ap-northeast-2", profile_name=profile_name)

### 입력받은 aws_connect_keys tuple 또는 aws_connect_key_dict 값을 통해서 aws_session을 연결 및 반환합니다.
def connect_aws_session(*aws_connect_keys: tuple, region_name: str = "ap-northeast-2", **aws_connect_key_dict: dict) -> Session:
    """
    입력받은 aws_connect_keys tuple 또는 aws_connect_key_dict dict 값을 통해서 aws_session을 연결 및 반환합니다.
    -- [Session 연결 정의]
    - 순수하게 session만 연결하고 값을 반환합니다.

    - Session 연결은 매개변수가 aws_connect_keys tuple 또는 aws_connect_key_dict dict 인지에 따라 달라집니다.

    1. 매개변수가 aws_connect_keys tuple 일 경우,
      => tuple의 매개변수 개수에 따라 결정됩니다.

      이는 아예 기본 연결[매개변수 0개 ~ 1개(리전값)]을 제외하면
      2개 이상의 값[profile_name 또는 접근, 비밀키]은 꼭 받는다고 가정합니다.

      - 첫번째 값인 region_name으로 연결하는건 모든 부분에서 똑같습니다.
      - aws_connect_keys의 개수에 따라서 다음과 같이 간주합니다.
        0: 현재 운영체제의 Default session 연결
        2: (region_name, profile_name)
        3: (region_name, aws_access_key_id, aws_secret_access_key)
        4: (region_name, aws_access_key_id, aws_secret_access_key, aws_session_token)
        5개 이상의 값: 에러를 발생시킵니다.

    2. 매개변수가 aws_connect_key_dict dict 일 경우,
      - region_name는 무조건 존재해야하며, Default 값으로 "ap-northeast-2"이 들어갑니다.
      - 그 밖에는 aws_account_id 또는 aws_access_key_id, aws_secret_access_key, aws_session_token, ... 값이 있습니다.
      - dict 에 aws_account_id 가 있으면, connect_aws_assumeRole_session를 호출합니다.
      -         aws_account_id 가 없으면, Session 함수에 필요한 값이라 가정하고 바로 Session함수를 연결합니다.
    """
    session = None
    # print("region_name", region_name, "aws_connect_keys:", aws_connect_keys, "aws_connect_key_dict:", aws_connect_key_dict)

    ### 1. 매개변수가 aws_connect_keys tuple 일 경우,
    if not aws_connect_key_dict:
        # logger.info(f'=== get_aws_session() 내부 - aws_connect_keys: ', aws_connect_keys)
        # logger.info(f'    len(aws_connect_keys):', len(aws_connect_keys))
        # 만약 Key가 없으면, 기본(Default) 리전 + 키 값으로 갑니다.
        if len(aws_connect_keys) == 0:
            # region_name = ~/.aws/config 의 [default] 설정 리전
            # profile_name = ~/.aws/credentials 의 [default] 프로파일
            session = Session()

        # Key가 1개면,
        elif len(aws_connect_keys) == 1:
            # 해당 값이 문자열이면 그 값은 region_name입니다.
            if type(aws_connect_keys[0]) == type("string"):
                # region_name = 받은 region_name
                # profile_name = ~/.aws/credentials 의 [default] 프로파일
                session = Session(region_name=aws_connect_keys[0])

            # 받은 인자 값이, dict()인 경우
            elif type(aws_connect_keys[0]) == type(dict()):
                # AccessKey, SecretKey, Region은 무조건 존재하며,
                # TokenKey는 있는경우, 없는 경우의 dict() 데이터를 받았다고 가정하고 처리한다.
                conf_dict = aws_connect_keys[0]
                if "TokenKey" in conf_dict:
                    session = Session(
                        region_name=conf_dict["Region"],
                        aws_access_key_id=conf_dict["AccessKey"],
                        aws_secret_access_key=conf_dict["SecretKey"],
                        aws_session_token=conf_dict["TokenKey"],
                    )
                else:
                    session = Session(
                        region_name=conf_dict["Region"],
                        aws_access_key_id=conf_dict["AccessKey"],
                        aws_secret_access_key=conf_dict["SecretKey"],
                    )

            else:
                # 어차피 안될거, 해당 내용의 에러를 출력시키고 Exception 발생
                logger.info("The aws_connect_keys format is not correct. [The first argument is not of str or dict type]")
                raise Exception("The aws_connect_keys format is not correct. [The first argument is not of str or dict type]")

        # Key가 2개면, 받은 region_name + profile_name 값입니다.
        # profile_name은 ~/.aws/credentials 에 존재해야 합니다.
        elif len(aws_connect_keys) == 2:
            session = Session(region_name=aws_connect_keys[0], profile_name=aws_connect_keys[1])
        # Key가 3개면, 받은 region_name + 접근키(aws_access_key_id), 비밀키(aws_secret_access_key) 값입니다.
        elif len(aws_connect_keys) == 3:
            session = Session(
                region_name=aws_connect_keys[0],
                aws_access_key_id=aws_connect_keys[1],
                aws_secret_access_key=aws_connect_keys[2],
            )
        # Key가 4개면, 받은 region_name + 접근키(aws_access_key_id), 비밀키(aws_secret_access_key), 토근(aws_session_token) 값입니다.
        elif len(aws_connect_keys) == 4:
            session = Session(
                region_name=aws_connect_keys[0],
                aws_access_key_id=aws_connect_keys[1],
                aws_secret_access_key=aws_connect_keys[2],
                aws_session_token=aws_connect_keys[3],
            )
        # Key가 5개 이상이면, 정상이 아니다.
        else:
            # 어차피 안될거, 해당 내용의 에러를 출력시키고 Exception 발생
            logger.info("The aws_connect_keys format is not correct. [More than 5 parameters]")
            raise Exception("The aws_connect_keys format is not correct. [More than 5 parameters]")

    ### 2. 매개변수가 aws_connect_key_dict dict 일 경우,
    else:
        # dict 에 aws_account_id 가 있으면, connect_aws_assumeRole_session를 호출합니다.
        if "aws_account_id" in aws_connect_key_dict:
            session = connect_aws_assumeRole_session(aws_connect_key_dict["aws_account_id"], region_name=region_name)

        # aws_account_id 가 없으면, Session 함수에 필요한 값이라 가정하고 바로 Session함수를 연결합니다.
        else:
            session = Session(region_name=region_name, **aws_connect_key_dict)

    return session


root_sts_client = None
# 고객사의 aws_account_id, region_name을 받아서, AssumeRole권한의 Session 값으로 반환합니다.
def connect_aws_assumeRole_session(aws_account_id: str, assume_role_name: str = "NdsManagingRole", region_name: str = "ap-northeast-2") -> Session:
    """
    고객사의 aws_account_id, region_name(디폴트값="ap-northeast-2")을 받아서, AssumeRole권한의 Session 값으로 반환합니다.

    - 테스트 환경(is_test_local_platform)이라면 profile_name="assume-role-only-user"이 설정되어 있어야 하고,
    - 아니라면, 해당 인스턴스에 sts-to-nds-role 이 부여되어 있어야 합니다.
    - 또한 고객사의 AWS 계정(aws_account_id)은 CloudBiz 계정(655457307385) 과 신뢰관계가 맺어진
      f"arn:aws:iam::{aws_account_id}:role/NdsManagingRole 역할이 존재해야합니다.
    """
    global root_session, root_sts_client

    # logger.info(f'connect_aws_assumeRole_session()')
    # logger.info(f'aws_account_id:', aws_account_id)
    # logger.info(f'sts_client:', sts_client)

    # 미리 얻었으면 또 얻을필요는 없습니다.
    if not root_sts_client:
        # 1. 1차 AssumeRole 권한 얻기 : NDS Support IAM 계정의 AWS Role 얻기
        #  1.1. NDS Support IAM 계정의 세션 연결

        # 얻은 세션. 권한 잘 얻어왔는지, 확인하는 테스트 코드
        # temp_client = my_session.client('ec2')
        # ret = temp_client.describe_instance_types()
        # logger.info(f'ret:{ret}')

        #  1.2. STS 서비스로부터 AssumeRole 생성
        root_sts_client = root_session.client("sts")
        if is_test_local_platform:
            assumed_role_object = root_sts_client.assume_role(
                RoleArn="arn:aws:iam::655457307385:role/KimjeheonManagingRole",
                RoleSessionName="NDS-session-1st",
            )
            # logger.info(f'assumed_role_object', assumed_role_object)

            # 2. 2차 AssumeRole 권한 얻기 : 고객사 계정의 AWS Role 얻기
            #  2.1. CloudBiz 계정의 sts client 연결
            root_sts_client = boto3.client(
                "sts",
                aws_access_key_id=assumed_role_object["Credentials"]["AccessKeyId"],
                aws_secret_access_key=assumed_role_object["Credentials"]["SecretAccessKey"],
                aws_session_token=assumed_role_object["Credentials"]["SessionToken"],
            )

    assumed_role_object = root_sts_client.assume_role(
        RoleArn=f"arn:aws:iam::{aws_account_id}:role/{assume_role_name}",
        RoleSessionName="NDS-session-2nd",
    )

    # 3. 고객사 AssumeRole의 세션 연결
    session = Session(
        region_name=region_name,
        aws_access_key_id=assumed_role_object["Credentials"]["AccessKeyId"],
        aws_secret_access_key=assumed_role_object["Credentials"]["SecretAccessKey"],
        aws_session_token=assumed_role_object["Credentials"]["SessionToken"],
    )

    return session
