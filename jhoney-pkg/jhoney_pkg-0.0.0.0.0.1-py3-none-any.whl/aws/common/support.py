from boto3.session import Session
from ._session import root_session

def get_aws_support_plan_level(session):
    """
    입력받은 aws session의 aws_support_plan_level 값을 반환한다.
    - 실질적으로는 "Basic" 또는 "Business" 둘 중 하나의 값만 반환한다.
    - 입력받은 세션은 "support" 서비스에 대한 Read 권한이 존재해야한다.
    - 판단 기준은 해당 계정으로 Support 서비스 함수의 호출 성공 유무로 파악한다.
        - Support 서비스의 함수는 Business 또는 Enterprise Support plan 만 수행할 수 있다.
        - 설령 Enterprise 고객일 지라도 Business 값으로 반환된다.
        - 이를 제외한 AWS Support Plan Level 값을 바로 얻어오는 boto3 함수는 존재하지 않아서 우회 구현하는 방식이다.
    """
    # 참고로, 글로벌 서비스는 "us-east-1" 리전으로 연결해야 동작한다.
    aws_support_plan_level = "Basic"

    try:
        client = session.client("support")
        client.describe_services()
        aws_support_plan_level = "Business"  # 또는 Enterprise
    except Exception as e:
        # print(e)
        pass

    return aws_support_plan_level


# session값을 받아서, alias 값을 얻어서 반환하는 함수
def get_account_alias(tmpsession):
    """session값을 받아서, alias 값을 얻어서 반환하는 함수"""
    client = tmpsession.client("iam")
    res = client.list_account_aliases()["AccountAliases"]

    if not res:
        return ""

    return res[0]


# session값을 받아서, aws_account_id 값을 얻어서 반환하는 함수
def get_aws_account_id(tmpsession):
    client = tmpsession.client("sts")

    res = client.get_caller_identity()
    # print("res", res)
    if not res:
        return ""

    return res["Account"]


# session으로부터 service의 client값을 얻습니다.
def get_aws_client(session: Session, service: str):
    """# session으로부터 service의 client값을 얻습니다."""
    return session.client(service)


# 주어진 aws resource로부터 Tags 속성 값 중, Name 태그의 값을 반환한다.
def get_name_tag(resource: dict, Tag: str = "Tags", TagKey: str = "Name"):
    """
    주어진 aws resource로부터 Tags 속성 값 중, Name 태그의 값을 반환한다.
    - Name 태그가 없으면 " - " 값을 반환한다.
    """
    ret = next((item for item in resource.get(Tag, list()) if item["Key"] == TagKey), dict())
    alias = " - "
    if "Value" in ret:
        alias = ret["Value"]
    return alias


# EC2 서비스의 InstanceTypes에 따른 할당된 RamSize를 담고 있는 dict 데이터를 얻어서 반환한다.
def get_EC2_InstanceTypes_AllocatedRamSize_MiB_dict():
    """EC2 서비스의 InstanceTypes에 따른 할당된 RamSize를 담고 있는 dict 데이터를 얻어서 반환한다."""

    ec2_client = root_session.client("ec2")

    InstanceTypes = list()
    ret = ec2_client.describe_instance_types()
    InstanceTypes.extend(ret["InstanceTypes"])

    while "NextToken" in ret:
        ret = ec2_client.describe_instance_types(NextToken=ret["NextToken"])
        InstanceTypes.extend(ret["InstanceTypes"])

    temp_dict = dict()
    for InstanceType in InstanceTypes:
        temp_dict[InstanceType["InstanceType"]] = InstanceType["MemoryInfo"]["SizeInMiB"]

    # InstanceType으로 정렬
    tuples_from_sorted_dict = sorted(temp_dict.items())
    sorted_EC2_InstanceTypes_AllocatedRamSize_MiB_dict = dict()
    for tuple_val in tuples_from_sorted_dict:
        sorted_EC2_InstanceTypes_AllocatedRamSize_MiB_dict[tuple_val[0]] = tuple_val[1]

    return sorted_EC2_InstanceTypes_AllocatedRamSize_MiB_dict


# 임시 주석처리 이유: 매번 get_EC2_InstanceTypes_AllocatedRamSize_MiB_dict를 실행하기보다는 고정된 값을 넣었다.
# EC2_InstanceTypes_AllocatedRamSize_MiB_dict = None
# def get_EC2_InstanceTypes_AllocatedRamSize_MiB(InstanceTypes):
#     # logger.info(f'InstanceTypes:', InstanceTypes)
#     global EC2_InstanceTypes_AllocatedRamSize_MiB_dict
#     if not EC2_InstanceTypes_AllocatedRamSize_MiB_dict:
#         EC2_InstanceTypes_AllocatedRamSize_MiB_dict = get_EC2_InstanceTypes_AllocatedRamSize_MiB_dict()
#     return EC2_InstanceTypes_AllocatedRamSize_MiB_dict.get(InstanceTypes, 1)

# EC2 서비스에서 해당 InstanceTypes에 할당된 RamSize값(MiB)을 반환합니다.
def get_EC2_InstanceTypes_AllocatedRamSize_MiB(InstanceTypes: str) -> int:
    """EC2 서비스에서 해당 InstanceTypes에 할당된 RamSize값(MiB)을 반환합니다."""
    # 2021-04-20-화 기준. get_EC2_InstanceTypes_AllocatedRamSize_MiB_dict를 호출한 결과. 총 237개
    return {
        "c4.2xlarge": 15360,
        "c4.4xlarge": 30720,
        "c4.8xlarge": 61440,
        "c4.large": 3840,
        "c4.xlarge": 7680,
        "c5.12xlarge": 98304,
        "c5.18xlarge": 147456,
        "c5.24xlarge": 196608,
        "c5.2xlarge": 16384,
        "c5.4xlarge": 32768,
        "c5.9xlarge": 73728,
        "c5.large": 4096,
        "c5.metal": 196608,
        "c5.xlarge": 8192,
        "c5a.12xlarge": 98304,
        "c5a.16xlarge": 131072,
        "c5a.24xlarge": 196608,
        "c5a.2xlarge": 16384,
        "c5a.4xlarge": 32768,
        "c5a.8xlarge": 65536,
        "c5a.large": 4096,
        "c5a.xlarge": 8192,
        "c5d.12xlarge": 98304,
        "c5d.18xlarge": 147456,
        "c5d.24xlarge": 196608,
        "c5d.2xlarge": 16384,
        "c5d.4xlarge": 32768,
        "c5d.9xlarge": 73728,
        "c5d.large": 4096,
        "c5d.metal": 196608,
        "c5d.xlarge": 8192,
        "c5n.18xlarge": 196608,
        "c5n.2xlarge": 21504,
        "c5n.4xlarge": 43008,
        "c5n.9xlarge": 98304,
        "c5n.large": 5376,
        "c5n.metal": 196608,
        "c5n.xlarge": 10752,
        "c6g.12xlarge": 98304,
        "c6g.16xlarge": 131072,
        "c6g.2xlarge": 16384,
        "c6g.4xlarge": 32768,
        "c6g.8xlarge": 65536,
        "c6g.large": 4096,
        "c6g.medium": 2048,
        "c6g.metal": 131072,
        "c6g.xlarge": 8192,
        "d2.2xlarge": 62464,
        "d2.4xlarge": 124928,
        "d2.8xlarge": 249856,
        "d2.xlarge": 31232,
        "g3.16xlarge": 499712,
        "g3.4xlarge": 124928,
        "g3.8xlarge": 249856,
        "g3s.xlarge": 31232,
        "g4dn.12xlarge": 196608,
        "g4dn.16xlarge": 262144,
        "g4dn.2xlarge": 32768,
        "g4dn.4xlarge": 65536,
        "g4dn.8xlarge": 131072,
        "g4dn.metal": 393216,
        "g4dn.xlarge": 16384,
        "i2.2xlarge": 62464,
        "i2.4xlarge": 124928,
        "i2.8xlarge": 249856,
        "i2.xlarge": 31232,
        "i3.16xlarge": 499712,
        "i3.2xlarge": 62464,
        "i3.4xlarge": 124928,
        "i3.8xlarge": 249856,
        "i3.large": 15616,
        "i3.metal": 524288,
        "i3.xlarge": 31232,
        "i3en.12xlarge": 393216,
        "i3en.24xlarge": 786432,
        "i3en.2xlarge": 65536,
        "i3en.3xlarge": 98304,
        "i3en.6xlarge": 196608,
        "i3en.large": 16384,
        "i3en.metal": 786432,
        "i3en.xlarge": 32768,
        "inf1.24xlarge": 196608,
        "inf1.2xlarge": 16384,
        "inf1.6xlarge": 49152,
        "inf1.xlarge": 8192,
        "m4.10xlarge": 163840,
        "m4.16xlarge": 262144,
        "m4.2xlarge": 32768,
        "m4.4xlarge": 65536,
        "m4.large": 8192,
        "m4.xlarge": 16384,
        "m5.12xlarge": 196608,
        "m5.16xlarge": 262144,
        "m5.24xlarge": 393216,
        "m5.2xlarge": 32768,
        "m5.4xlarge": 65536,
        "m5.8xlarge": 131072,
        "m5.large": 8192,
        "m5.metal": 393216,
        "m5.xlarge": 16384,
        "m5a.12xlarge": 196608,
        "m5a.16xlarge": 262144,
        "m5a.24xlarge": 393216,
        "m5a.2xlarge": 32768,
        "m5a.4xlarge": 65536,
        "m5a.8xlarge": 131072,
        "m5a.large": 8192,
        "m5a.xlarge": 16384,
        "m5ad.12xlarge": 196608,
        "m5ad.16xlarge": 262144,
        "m5ad.24xlarge": 393216,
        "m5ad.2xlarge": 32768,
        "m5ad.4xlarge": 65536,
        "m5ad.8xlarge": 131072,
        "m5ad.large": 8192,
        "m5ad.xlarge": 16384,
        "m5d.12xlarge": 196608,
        "m5d.16xlarge": 262144,
        "m5d.24xlarge": 393216,
        "m5d.2xlarge": 32768,
        "m5d.4xlarge": 65536,
        "m5d.8xlarge": 131072,
        "m5d.large": 8192,
        "m5d.metal": 393216,
        "m5d.xlarge": 16384,
        "m6g.12xlarge": 196608,
        "m6g.16xlarge": 262144,
        "m6g.2xlarge": 32768,
        "m6g.4xlarge": 65536,
        "m6g.8xlarge": 131072,
        "m6g.large": 8192,
        "m6g.medium": 4096,
        "m6g.metal": 262144,
        "m6g.xlarge": 16384,
        "p2.16xlarge": 749568,
        "p2.8xlarge": 499712,
        "p2.xlarge": 62464,
        "p3.16xlarge": 499712,
        "p3.2xlarge": 62464,
        "p3.8xlarge": 249856,
        "r3.2xlarge": 62464,
        "r3.4xlarge": 124928,
        "r3.8xlarge": 249856,
        "r3.large": 15360,
        "r3.xlarge": 31232,
        "r4.16xlarge": 499712,
        "r4.2xlarge": 62464,
        "r4.4xlarge": 124928,
        "r4.8xlarge": 249856,
        "r4.large": 15616,
        "r4.xlarge": 31232,
        "r5.12xlarge": 393216,
        "r5.16xlarge": 524288,
        "r5.24xlarge": 786432,
        "r5.2xlarge": 65536,
        "r5.4xlarge": 131072,
        "r5.8xlarge": 262144,
        "r5.large": 16384,
        "r5.metal": 786432,
        "r5.xlarge": 32768,
        "r5a.12xlarge": 393216,
        "r5a.16xlarge": 524288,
        "r5a.24xlarge": 786432,
        "r5a.2xlarge": 65536,
        "r5a.4xlarge": 131072,
        "r5a.8xlarge": 262144,
        "r5a.large": 16384,
        "r5a.xlarge": 32768,
        "r5ad.12xlarge": 393216,
        "r5ad.16xlarge": 524288,
        "r5ad.24xlarge": 786432,
        "r5ad.2xlarge": 65536,
        "r5ad.4xlarge": 131072,
        "r5ad.8xlarge": 262144,
        "r5ad.large": 16384,
        "r5ad.xlarge": 32768,
        "r5d.12xlarge": 393216,
        "r5d.16xlarge": 524288,
        "r5d.24xlarge": 786432,
        "r5d.2xlarge": 65536,
        "r5d.4xlarge": 131072,
        "r5d.8xlarge": 262144,
        "r5d.large": 16384,
        "r5d.metal": 786432,
        "r5d.xlarge": 32768,
        "r6g.12xlarge": 393216,
        "r6g.16xlarge": 524288,
        "r6g.2xlarge": 65536,
        "r6g.4xlarge": 131072,
        "r6g.8xlarge": 262144,
        "r6g.large": 16384,
        "r6g.medium": 8192,
        "r6g.metal": 524288,
        "r6g.xlarge": 32768,
        "t2.2xlarge": 32768,
        "t2.large": 8192,
        "t2.medium": 4096,
        "t2.micro": 1024,
        "t2.nano": 512,
        "t2.small": 2048,
        "t2.xlarge": 16384,
        "t3.2xlarge": 32768,
        "t3.large": 8192,
        "t3.medium": 4096,
        "t3.micro": 1024,
        "t3.nano": 512,
        "t3.small": 2048,
        "t3.xlarge": 16384,
        "t3a.2xlarge": 32768,
        "t3a.large": 8192,
        "t3a.medium": 4096,
        "t3a.micro": 1024,
        "t3a.nano": 512,
        "t3a.small": 2048,
        "t3a.xlarge": 16384,
        "t4g.2xlarge": 32768,
        "t4g.large": 8192,
        "t4g.medium": 4096,
        "t4g.micro": 1024,
        "t4g.nano": 512,
        "t4g.small": 2048,
        "t4g.xlarge": 16384,
        "x1.16xlarge": 999424,
        "x1.32xlarge": 1998848,
        "x1e.16xlarge": 1998848,
        "x1e.2xlarge": 249856,
        "x1e.32xlarge": 3997696,
        "x1e.4xlarge": 499712,
        "x1e.8xlarge": 999424,
        "x1e.xlarge": 124928,
        "z1d.12xlarge": 393216,
        "z1d.2xlarge": 65536,
        "z1d.3xlarge": 98304,
        "z1d.6xlarge": 196608,
        "z1d.large": 16384,
        "z1d.metal": 393216,
        "z1d.xlarge": 32768,
    }.get(InstanceTypes, 1)


# RDS 서비스에서 해당 DBInstanceClass에 할당된 RamSize값(GiB)을 반환합니다.
def get_RDS_DBInstanceClass_AllocatedRamSize_GiB(DBInstanceClass: str) -> int:
    """
    RDS 서비스에서 해당 DBInstanceClass에 할당된 RamSize값(GiB)을 반환합니다.
    - 2021-04-20-화 기준
    - Amazon RDS 인스턴스 유형 : https://aws.amazon.com/ko/rds/instance-types/
    # - M5d, R5b 내용 추가
    """
    return {
        ##### 범용
        # T3
        "db.t3.micro": 1,
        "db.t3.small": 2,
        "db.t3.medium": 4,
        "db.t3.large": 8,
        "db.t3.xlarge": 16,
        "db.t3.2xlarge": 32,
        # T2
        "db.t2.micro": 1,
        "db.t2.small": 2,
        "db.t2.medium": 4,
        "db.t2.large": 8,
        "db.t2.xlarge": 16,
        "db.t2.2xlarge": 32,
        # M6g
        "db.m6g.large": 8,
        "db.m6g.xlarge": 16,
        "db.m6g.2xlarge": 32,
        "db.m6g.4xlarge": 64,
        "db.m6g.8xlarge": 128,
        "db.m6g.12xlarge": 192,
        "db.m6g.16xlarge": 256,
        # M5
        "db.m5.large": 8,
        "db.m5.xlarge": 16,
        "db.m5.2xlarge": 32,
        "db.m5.4xlarge": 64,
        "db.m5.8xlarge": 128,
        "db.m5.12xlarge": 192,
        "db.m5.16xlarge": 256,
        "db.m5.24xlarge": 384,
        # M5d
        "db.m5d.large": 8,
        "db.m5d.xlarge": 16,
        "db.m5d.2xlarge": 32,
        "db.m5d.4xlarge": 64,
        "db.m5d.8xlarge": 128,
        "db.m5d.12xlarge": 192,
        "db.m5d.16xlarge": 256,
        "db.m5d.24xlarge": 384,
        # M4
        "db.m4.large": 8,
        "db.m4.xlarge": 16,
        "db.m4.2xlarge": 32,
        "db.m4.4xlarge": 64,
        "db.m4.10xlarge": 160,
        "db.m4.16xlarge": 256,
        ##### 메모리 최적화
        # R6g
        "db.r6g.large": 16,
        "db.r6g.xlarge": 32,
        "db.r6g.2xlarge": 64,
        "db.r6g.4xlarge": 128,
        "db.r6g.8xlarge": 256,
        "db.r6g.12xlarge": 384,
        "db.r6g.16xlarge": 512,
        # R5
        "db.r5.large": 16,
        "db.r5.xlarge": 32,
        "db.r5.2xlarge": 64,
        "db.r5.4xlarge": 128,
        "db.r5.8xlarge": 256,
        "db.r5.12xlarge": 384,
        "db.r5.16xlarge": 512,
        "db.r5.24xlarge": 768,
        # R5b
        "db.r5b.large": 16,
        "db.r5b.xlarge": 32,
        "db.r5b.2xlarge": 64,
        "db.r5b.4xlarge": 128,
        "db.r5b.8xlarge": 256,
        "db.r5b.12xlarge": 384,
        "db.r5b.16xlarge": 512,
        "db.r5b.24xlarge": 768,
        # R4
        "db.r4.large": 15.25,
        "db.r4.xlarge": 30.5,
        "db.r4.2xlarge": 61,
        "db.r4.4xlarge": 122,
        "db.r4.8xlarge": 244,
        "db.r4.16xlarge": 488,
        # X1e
        "db.x1e.xlarge": 122,
        "db.x1e.2xlarge": 244,
        "db.x1e.4xlarge": 488,
        "db.x1e.8xlarge": 976,
        "db.x1e.16xlarge": 1952,
        "db.x1e.32xlarge": 3904,
        # X1
        "db.x1.16xlarge": 976,
        "db.x1.32xlarge": 1952,
        # Z1d
        "db.z1d.large": 16,
        "db.z1d.xlarge": 32,
        "db.z1d.2xlarge": 64,
        "db.z1d.3xlarge": 96,
        "db.z1d.6xlarge": 192,
        "db.z1d.12xlarge": 384,
    }.get(DBInstanceClass, 1)


# EC2 서비스에서 해당 InstanceTypes에서 적립 가능한 최대 적립 크레딧을 반환합니다.
def get_EC2_CPUCreditBalance_Max(InstanceTypes: str) -> float:
    """
    EC2 서비스에서 해당 InstanceTypes에서 적립 가능한 최대 적립 크레딧을 반환합니다.
    - 버스트 가능한 성능 인스턴스에 대한 CPU 크레딧 및 기준 사용률 : https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html
    - 2021-01-07-목 기준
    """
    return {
        ##### 범용
        # T2
        "t2.nano": 72,
        "t2.micro": 144,
        "t2.small": 288,
        "t2.medium": 576,
        "t2.large": 864,
        "t2.xlarge": 1296,
        "t2.2xlarge": 1958.4,
        # T3
        "t3.nano": 144,
        "t3.micro": 288,
        "t3.small": 576,
        "t3.medium": 576,
        "t3.large": 864,
        "t3.xlarge": 2304,
        "t3.2xlarge": 4608,
        # T3a
        "t3a.nano": 144,
        "t3a.micro": 288,
        "t3a.small": 576,
        "t3a.medium": 576,
        "t3a.large": 864,
        "t3a.xlarge": 2304,
        "t3a.2xlarge": 4608,
        # T4g
        "t4g.nano": 144,
        "t4g.micro": 288,
        "t4g.small": 576,
        "t4g.medium": 576,
        "t4g.large": 864,
        "t4g.xlarge": 2304,
        "t4g.2xlarge": 4608,
    }.get(InstanceTypes, 1)


# ElastiCache 서비스에서 해당 CacheNodeType에 할당된 vCPU값을 반환합니다.
def get_ElastiCache_vCPU(CacheNodeType: str) -> int:
    """
    ElastiCache 서비스에서 해당 CacheNodeType에 할당된 vCPU값을 반환합니다.
    - Amazon ElastiCache 인스턴스 유형 : https://aws.amazon.com/ko/elasticache/pricing/
    - 2021-03-11-목 기준
    """
    return {
        ##### 표준 - 현재 세대
        "cache.t2.micro": 1,
        "cache.t2.small": 1,
        "cache.t2.medium": 2,
        "cache.t3.micro": 2,
        "cache.t3.small": 2,
        "cache.t3.medium": 2,
        "cache.m4.large": 2,
        "cache.m4.xlarge": 4,
        "cache.m4.2xlarge": 8,
        "cache.m4.4xlarge": 16,
        "cache.m4.10xlarge": 40,
        "cache.m5.large": 2,
        "cache.m5.xlarge": 4,
        "cache.m5.2xlarge": 8,
        "cache.m5.4xlarge": 16,
        "cache.m5.12xlarge": 48,
        "cache.m5.24xlarge": 96,
        "cache.m6g.large": 2,
        "cache.m6g.xlarge": 4,
        "cache.m6g.2xlarge": 8,
        "cache.m6g.4xlarge": 16,
        "cache.m6g.8xlarge": 32,
        "cache.m6g.12xlarge": 48,
        "cache.m6g.16xlarge": 64,
        # Memory Optimized - Current, Generation
        "cache.r4.large": 2,
        "cache.r4.xlarge": 4,
        "cache.r4.2xlarge": 8,
        "cache.r4.4xlarge": 16,
        "cache.r4.8xlarge": 32,
        "cache.r4.16xlarge": 64,
        "cache.r5.large": 2,
        "cache.r5.xlarge": 4,
        "cache.r5.2xlarge": 8,
        "cache.r5.4xlarge": 16,
        "cache.r5.12xlarge": 48,
        "cache.r5.24xlarge": 96,
        "cache.r6g.large": 2,
        "cache.r6g.xlarge": 4,
        "cache.r6g.2xlarge": 8,
        "cache.r6g.4xlarge": 16,
        "cache.r6g.8xlarge": 32,
        "cache.r6g.12xlarge": 48,
        "cache.r6g.16xlarge": 64,
    }.get(CacheNodeType, 1)


# 입력받은 'X' 값에 해당하는, XiB의 Byte값을 구해서 반환합니다.
def get_Bytes_from_XiB(X: str) -> int:
    """
    # 입력받은 'X' 값에 해당하는, XiB의 Byte값을 구해서 반환합니다.
    - X: N or B     | K         | M         | G         | T
    - None or Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes
    - 2^0           |  2^10     | 2^20      | 2^30      | 2^40
    """
    return {
        "B": 2 ** 0,
        "K": 2 ** 10,
        "M": 2 ** 20,
        "G": 2 ** 30,
        "T": 2 ** 40,
    }.get(X, 1)


# 주어진 aws_region_name 값을 문자열 명칭으로 변경합니다.
def aws_region_to_str(region_name: str, *, is_name_short: bool = True, is_language_eng: bool = True):
    """
    주어진 region_name 값을 문자열 명칭으로 변경합니다.
    - is_name_short 값이 True(Default)이면 축약값, False면 전체
    - is_language_eng 값이 True(Default)이면 영어, False면 한글
    - Ex. ap-northeast-2
      is_name_short=False, is_language_eng=False -> 아시아 태평양 (서울)
      version 2 -> 아시아 태평양 (서울)
    """
    aws_region_eng_short = {
        "global": "Global",
        "us-east-1": "N. Virginia",
        "us-east-2": "Ohio",
        "us-west-1": "N. California",
        "us-west-2": "Oregon",
        "af-south-1": "Cape Town",
        "ap-east-1": "Hong Kong",
        "ap-south-1": "Mumbai",
        "ap-northeast-3": "Osaka",
        "ap-northeast-2": "Seoul",
        "ap-southeast-1": "Singapore",
        "ap-southeast-2": "Sydney",
        "ap-northeast-1": "Tokyo",
        "ca-central-1": "Central",
        "eu-central-1": "Frankfurt",
        "eu-west-1": "Ireland",
        "eu-west-2": "London",
        "eu-south-1": "Milan",
        "eu-west-3": "Paris",
        "eu-north-1": "Stockholm",
        "me-south-1": "Bahrain",
        "sa-east-1": "São Paulo",
    }
    aws_region_eng_long = {
        "global": "Global Network Infra",
        "us-east-1": "US East (N. Virginia)",
        "us-east-2": "US East (Ohio)",
        "us-west-1": "US West (N. California)",
        "us-west-2": "US West (Oregon)",
        "af-south-1": "Africa (Cape Town)",
        "ap-east-1": "Asia Pacific (Hong Kong)",
        "ap-south-1": "Asia Pacific (Mumbai)",
        "ap-northeast-3": "Asia Pacific (Osaka)",
        "ap-northeast-2": "Asia Pacific (Seoul)",
        "ap-southeast-1": "Asia Pacific (Singapore)",
        "ap-southeast-2": "Asia Pacific (Sydney)",
        "ap-northeast-1": "Asia Pacific (Tokyo)",
        "ca-central-1": "Canada (Central)",
        "eu-central-1": "Europe (Frankfurt)",
        "eu-west-1": "Europe (Ireland)",
        "eu-west-2": "Europe (London)",
        "eu-south-1": "Europe (Milan)",
        "eu-west-3": "Europe (Paris)",
        "eu-north-1": "Europe (Stockholm)",
        "me-south-1": "Middle East (Bahrain)",
        "sa-east-1": "South America (São Paulo)",
    }
    aws_region_kor_short = {
        "global": "글로벌",
        "us-east-1": "버지니아_북부",
        "us-east-2": "오하이오",
        "us-west-1": "캘리포니아",
        "us-west-2": "오레곤",
        "af-south-1": "케이프타운",
        "ap-east-1": "홍콩",
        "ap-south-1": "뭄바이",
        "ap-northeast-2": "서울",
        "ap-southeast-1": "싱가포르",
        "ap-southeast-2": "시드니",
        "ap-northeast-1": "도쿄",
        "ca-central-1": "중부",
        "eu-central-1": "프랑크푸르트",
        "eu-west-1": "아일랜드",
        "eu-west-2": "런던",
        "eu-south-1": "밀라노",
        "eu-west-3": "파리",
        "eu-north-1": "스톡홀름",
        "me-south-1": "바레인",
        "sa-east-1": "상파울루",
    }
    aws_region_kor_long = {
        "global": "글로벌 네트워크 인프라",
        "us-east-1": "미국 동부 (버지니아 북부)",
        "us-east-2": "미국 동부 (오하이오)",
        "us-west-1": "미국 서부 (캘리포니아)",
        "us-west-2": "미국 서부 (오레곤)",
        "af-south-1": "아프리카 (케이프타운)",
        "ap-east-1": "아시아 태평양 (홍콩)",
        "ap-south-1": "아시아 태평양 (뭄바이)",
        "ap-northeast-2": "아시아 태평양 (서울)",
        "ap-southeast-1": "아시아 태평양 (싱가포르)",
        "ap-southeast-2": "아시아 태평양 (시드니)",
        "ap-northeast-1": "아시아 태평양 (도쿄)",
        "ca-central-1": "캐나다 (중부)",
        "eu-central-1": "유럽 (프랑크푸르트)",
        "eu-west-1": "유럽 (아일랜드)",
        "eu-west-2": "유럽 (런던)",
        "eu-south-1": "유럽 (밀라노)",
        "eu-west-3": "유럽 (파리)",
        "eu-north-1": "유럽 (스톡홀름)",
        "me-south-1": "중동 (바레인)",
        "sa-east-1": "남아메리카 (상파울루)",
    }

    if is_language_eng:
        if is_name_short:
            aws_region_dict = aws_region_eng_short
        else:
            aws_region_dict = aws_region_eng_long
    else:
        if is_name_short:
            aws_region_dict = aws_region_kor_short
        else:
            aws_region_dict = aws_region_kor_long

    return aws_region_dict[region_name]
