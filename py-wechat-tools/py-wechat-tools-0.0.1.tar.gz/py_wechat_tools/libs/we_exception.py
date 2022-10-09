class WeError(Exception):
    """ 微信异常类 """

    def __init__(self, result, *args):  # real signature unknown
        errcode = result.json().get("errcode")

        err = {
            -1: "系统繁忙，此时请开发者稍候再试！",
            1: "加密数据不存在，数据生成的时间超过保存的限制（3天）或者key不存在",
            1000: "微信系统错误",
            1001: "请求参数非法",
            1003: "请求频率过快",
            1005: "插件appid与数据不匹配",
            1007: "openpid数据不存在",
            1022: "json数据解析错误",
            40001: "AppSecret 错误或者 AppSecret 不属于这个小程序，请开发者确认 AppSecret 的正确性	",
            40003: "openid 错误",
            40013: "不合法的 AppID，请开发者检查 AppID 的正确性，避免异常字符，注意大小写",
            40029: "不合法的code（code不存在、已过期或者使用过）",
            40037: "模板id不正确，weapp_template_msg.template_id或者mp_template_msg.template_id",
            40066: "无效的url，已发布小程序没有对应url",
            40097: "请求里的encrypted_msg_hash参数无效",
            40129: "场景值错误（目前支持场景 1 资料；2 评论；3 论坛；4 社交日志）",
            40163: "code已被使用",
            40225: "无效的页面标题",
            40226: ("高风险等级用户，小程序登录拦截 。风险等级详见用户安全解方案："
                    "https://developers.weixin.qq.com/miniprogram/dev/framework/operation.html"
                    "#%E7%94%A8%E6%88%B7%E5%AE%89%E5%85%A8%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88"),
            41028: "weapp_template_msg.form_id过期或者不正确",
            41029: "weapp_template_msg.form_id已被使用",
            41030: "page路径不正确，需要保证在现网版本小程序中存在，与app.json保持一致",
            42001: "调用接口凭证已过期",
            43101: "用户拒绝接受消息，如果用户之前曾经订阅过，则表示用户取消了订阅关系",
            43104: "appid与 openid 不匹配",
            43302: "方法调用错误，请用 post 方法调用",
            44002: "传入的数据为空",
            45009: "当日请求数量已达上限(接口调用超过限额)",
            45011: "频率限制，每个用户每分钟100次",
            47001: "传入的数据格式错误",
            47003: "模板参数不准确，可能为空或者不满足规则，errmsg会提示具体是哪个字段出错",
            47501: "参数 activity_id 错误",
            47502: "参数 target_state 错误",
            47503: "参数 version_type 错误",
            47504: "activity_id 过期",
            48001: "小程序无该 api 权限",
            61010: "用户访问记录超时（用户未在近两小时访问小程序）",
            85400: "长期有效Short Link达到生成上限10万",
            89002: "没有绑定开放平台帐号",
            89300: "订单无效",
            101000: "图片 URL 错误或拉取 URL 图像错误",
            101001: "图片中无法找到证件",
            101002: "图片数据无效",
            101003: "市场配额不足",
            200014: "模版 tid 参数错误",
            200011: "此账号已被封禁，无法操作",
            200012: "个人模版数已达上限，上限25个",
            200013: "此模版已被封禁，无法选用",
            200020: "关键词列表 kidList 参数错误",
            200021: "场景描述 sceneDesc 参数错误",
            9410009: "测试额度已耗尽",

            # 公众号
            10003: "redirect_uri域名与后台配置不一致",
            10004: "此公众号被封禁",
            10005: "此公众号并没有这些scope的权限",
            10006: "必须关注此测试号",
            10009: "操作太频繁了，请稍后重试",
            10010: "scope不能为空",
            10011: "redirect_uri不能为空",
            10012: "appid不能为空",
            10013: "state不能为空",
            10015: "公众号未授权第三方平台，请检查授权状态",
            10016: "不支持微信开放平台的Appid，请使用公众号Appid",

        }

        errmsg = "errcode：%s；errmsg：%s" % (errcode, err.get(errcode, result.json()))

        super().__init__(errmsg, *args)


class WeAccessTokenExpired(Exception):
    """ 微信access_token过期异常 """

    def __init__(self, *args):
        super().__init__("errcode：42001；errmsg：调用接口凭证已过期", *args)
