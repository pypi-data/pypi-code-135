from enum import *
import os
from typing import List

from pih.collection import FieldItem, FieldItemList, LogCommand, ParamItem, PasswordSettings, ServiceRoleValue


class DATA_EXTRACTOR:

    USER_NAME_FULL: str = "user_name_full"
    USER_NAME: str = "user_name"
    AS_IS: str = "as_is"


class USER_PROPERTY:

    TELEPHONE: str = "telephoneNumber"
    EMAIL: str = "mail"
    DN: str = "distinguishedName"
    USER_ACCOUNT_CONTROL: str = "userAccountControl"
    LOGIN: str = "samAccountName"
    DESCRIPTION: str = "description"
    PASSWORD: str = "password"
    USER_STATUS: str = "userStatus"
    NAME: str = "name"

class userPropertiNames(Enum):
    PASSWORD = "Пароль"
    TELEPHONE = "Телефон"

class SCHEDULER_EVENT_TYPE:
    MINUTE: int = 5
    HOUR: int = 5


class CONST:

    SITE: str = "pacifichosp.com"
    MAIL_PREFIX: str = "mail"
    SITE_PROTOCOL: str = "https://"
    EMAIL_ADDRESS: str = f"{MAIL_PREFIX}.{SITE}"
    PHONE_PREFIX: str = "+7"

    PYPI_URL: str = "https://pypi.python.org/pypi/pih/json"

    class TIME_TRACKING:

        REPORT_DAY_PERIOD_DEFAULT: int = 15

    class PYTHON:

        EXECUTOR: str = "py"
        PYPI: str = "pip"

    class SERVICE:

        NAME: str = "service"

    class FACADE:
    
        COMMAND_SUFFIX: str = "Core"
        PATH: str = "//pih/facade/"

    class PSTOOLS:

        NAME: str = "PSTools"
        EXECUTOR: str = "PsExec"
        PSKILL: str = "PsKill"

    class FILE:

        class EXTENSION:

            EXCEL_OLD: str = "xls"
            EXCEL_NEW: str = "xlsx"
            PYTHON: str = "py"

    class DOCS:

        EXCEL_TITLE_MAX_LENGTH: int = 31

        class INVENTORY:

            NAME_COLUMN_NAME: str = "наименование, назначение и краткая характеристика объекта"
            NUMBER_COLUMN_NAME: str = "инвентарный"
            QUANTITY_COLUMN_NAME: str = "фактическое наличие"
            NAME_MAX_LENTH: int = 30
            QUANTITY_NOT_SET: str = "-"

    class BARCODE_READER:

        PREFIX: str = "("
        SUFFIX: str = ")"

    class AD:

        SEARCH_ATTRIBUTES: List[str] = [
            USER_PROPERTY.LOGIN, USER_PROPERTY.NAME]
        SEARCH_ATTRIBUTE_DEFAULT: str = SEARCH_ATTRIBUTES[0]
        DOMAIN_NAME: str = "fmv"
        DOMAIN_ALIAS: str = "pih"
        DOMAIN_SUFFIX: str = "lan"
        DOMAIN: str = f"{DOMAIN_NAME}.{DOMAIN_SUFFIX}"
        DOMAIN_MAIN: str = DOMAIN
        USER_HOME_FOLDER_DISK: str = "U:"
        ROOT_CONTAINER_DN: str = f"OU=Unit,DC={DOMAIN_NAME},DC={DOMAIN_SUFFIX}"
        USERS_CONTAINER_DN_SUFFIX: str = f"Users,{ROOT_CONTAINER_DN}"
        ACTIVE_USERS_CONTAINER_DN: str = f"OU={USERS_CONTAINER_DN_SUFFIX}"
        INACTIVE_USERS_CONTAINER_DN: str = f"OU=dead{USERS_CONTAINER_DN_SUFFIX}"
        PATH_ROOT: str = f"\\\{DOMAIN_MAIN}"
        SEARCH_ALL_PATTERN: str = "*"
        GRUOPS_CONTAINER_DN: str = f"OU=Groups,{ROOT_CONTAINER_DN}"
        JOB_POSITIONS_CONTAINER_DN: str = f"OU=Job positions,{GRUOPS_CONTAINER_DN}"
        LOCATION_JOINER: str = ":"
        TEMPLATED_USER_SERACH_TEMPLATE: str = "_*_"
        USER_ACCOUNT_CONTROL: List[str] = [
            "SCRIPT",
            "ACCOUNTDISABLE",
            "RESERVED",
            "HOMEDIR_REQUIRED",
            "LOCKOUT",
            "PASSWD_NOTREQD",
            "PASSWD_CANT_CHANGE",
            "ENCRYPTED_TEXT_PWD_ALLOWED",
            "TEMP_DUPLICATE_ACCOUNT",
            "NORMAL_ACCOUNT",
            "RESERVED",
            "INTERDOMAIN_TRUST_ACCOUNT",
            "WORKSTATION_TRUST_ACCOUNT",
            "SERVER_TRUST_ACCOUNT",
            "RESERVED",
            "RESERVED",
            "DONT_EXPIRE_PASSWORD",
            "MNS_LOGON_ACCOUNT",
            "SMARTCARD_REQUIRED",
            "TRUSTED_FOR_DELEGATION",
            "NOT_DELEGATED",
            "USE_DES_KEY_ONLY",
            "DONT_REQ_PREAUTH",
            "PASSWORD_EXPIRED",
            "TRUSTED_TO_AUTH_FOR_DELEGATION",
            "RESERVED",
            "PARTIAL_SECRETS_ACCOUNT"
        ]


        ADMIN_USER: str = "Administrator"
        ADMIN_PASSOWORD: str = "Fortun@90"

        class JobPositions(Enum):
            HR: str = auto()
            IT: str = auto()

        class Groups(Enum):
            TimeTrackingReport: str = auto()
            Inventory: str = auto()
            Admin: str = auto()
            ServiceAdmin: str = auto()

    class NAME_POLICY:

        PARTS_LIST_MIN_LENGTH: int = 3
        PART_ITEM_MIN_LENGTH: int = 3

    class RPC:

        PING_COMMAND: str = "__ping__"
        EVENT_COMMAND: str = "__event__"
        SUBSCRIBE_COMMAND: str = "__subscribe__"

        @staticmethod
        def PORT(add: int = 0) -> int:
            return 50051 + add

    class HOST:

        class PRINTER_SERVER:
        
            NAME: str = "fmvdc1.fmv.lan"

        class PRINTER:

            NAME: str = "fmvdc2.fmv.lan"

        class ORION:
           
            NAME: str = "orion"

        class AD:

            NAME: str = "fmvdc2.fmv.lan"

        class DOCS:

            NAME: str = "fmvdc2.fmv.lan"

        class POLIBASE:

            NAME: str = "polibase.fmv.lan"

        class BACKUP_WORKER:

            NAME: str = "backup_worker.fmv.lan"

        class LOG:

            NAME: str = "logger.fmv.lan"

        class SCHEDULER:
    
            @staticmethod
            def NAME() -> str:
                return "ws-735"

    class POLIBASE:

        INSTANCE: str = "orcl.fmv.lan"
        USER: str = "POLIBASE"
        PASSWORD: str = "POLIBASE"

class PATH_SHARE:

    NAME: str = "shares"
    PATH: str = os.path.join(CONST.AD.PATH_ROOT, NAME)


class PATH_IT:

    NAME: str = "5. IT"
    NEW_EMPLOYEES_NAME: str = "New employees"
    ROOT: str = os.path.join(PATH_SHARE.PATH, NAME)

    @staticmethod
    def NEW_EMPLOYEE(name: str) -> str:
        return os.path.join(os.path.join(PATH_IT.ROOT, PATH_IT.NEW_EMPLOYEES_NAME), name)


class PATH_USER:

    NAME: str = "homes"
    HOME_FOLDER: str = os.path.join(CONST.AD.PATH_ROOT, NAME)
    HOME_FOLDER_FULL: str = os.path.join(CONST.AD.PATH_ROOT, NAME)

    @staticmethod
    def document(name: str, login: str = None) -> str:
        return PATH_IT.NEW_EMPLOYEE(name) + (f" ({login})" if login else "") + ".docx"


class PATH_WS:

    NAME: str = f"WS{CONST.FACADE.COMMAND_SUFFIX}"
    PATH: str = os.path.join(CONST.FACADE.PATH, NAME)

class PATHS:

    SHARE: PATH_SHARE = PATH_SHARE()
    IT: PATH_IT = PATH_IT()
    USER: PATH_USER = PATH_USER()
    WS: PATH_WS = PATH_WS()


class FIELD_NAME_COLLECTION:

    FULL_NAME: str = "FullName"
    GROUP_NAME: str = "GroupName"
    GROUP_ID: str = "GroupID"
    COMMENT: str = "Comment"
    TAB_NUMBER: str = "TabNumber"
    NAME: str = USER_PROPERTY.NAME
    PERSON_ID: str = "pID"
    MARK_ID: str = "mID"
    ID: str = "id"
    VALUE: str = "value"
    FILE: str = "file"
    DIVISION_NAME: str = "DivisionName"

    PORT_NAME: str = "portName"

    SEARCH_ATTRIBUTE_LOGIN: str = "samAccountName"
    SEARCH_ATTRIBUTE_NAME: str = USER_PROPERTY.NAME

    TELEPHONE: str = USER_PROPERTY.TELEPHONE
    EMAIL: str = USER_PROPERTY.EMAIL
    DN: str = USER_PROPERTY.DN
    LOGIN: str = USER_PROPERTY.LOGIN
    DESCRIPTION: str = USER_PROPERTY.DESCRIPTION
    PASSWORD: str = USER_PROPERTY.PASSWORD

    INVENTORY_NUMBER: str = "inventory_number"
    QUANTITY: str = "quantity"
    ROW: str = "row"
    NAME_COLUMN: str = "name_column"
    INVENTORY_NUMBER_COLUMN: str = "inventory_number_column"
    QUANTITY_COLUMN: str = "quantity_column"

    TEMPLATE_USER_CONTAINER: str = "templated_user"
    CONTAINER: str = "container"

    REMOVE: str = "remove"
    AS_FREE: str = "as_free"
    CANCEL: str = "cancel"


class FIELD_COLLECTION:

    INDEX: FieldItem = FieldItem("__Index__", "Индекс", True)

    class ORION:

        MARK_ACTION: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.REMOVE, "Удалить"),
            FieldItem(FIELD_NAME_COLLECTION.AS_FREE, "Сделать свободной"),
            FieldItem(FIELD_NAME_COLLECTION.CANCEL, "Оставить")
        )

        GROUP_BASE: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.GROUP_NAME, "Уровень доступа"),
            FieldItem(FIELD_NAME_COLLECTION.COMMENT, "Описание", False)
        )

        TAB_NUMBER_BASE: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.TAB_NUMBER, "Табельный номер"))

        FREE_MARK: FieldItemList = FieldItemList(
            TAB_NUMBER_BASE, GROUP_BASE)

        TAB_NUMBER: FieldItemList = FieldItemList(
            TAB_NUMBER_BASE,
            FieldItem(FIELD_NAME_COLLECTION.DIVISION_NAME, "Подразделение"),
            GROUP_BASE).position(FIELD_NAME_COLLECTION.DIVISION_NAME, 2)

        PERSON: FieldItemList = FieldItemList(
            TAB_NUMBER,
            FieldItem(FIELD_NAME_COLLECTION.TELEPHONE,
                      "Телефон", True),
            FieldItem(FIELD_NAME_COLLECTION.FULL_NAME, "Полное имя")
        ).position(FIELD_NAME_COLLECTION.FULL_NAME, 1).position(FIELD_NAME_COLLECTION.TELEPHONE, 2)

        PERSON_DIVISION: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.ID, "ID", False),
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Название подразделения")
        )

        PERSON_EXTENDED: FieldItemList = FieldItemList(
            PERSON,
            FieldItem(FIELD_NAME_COLLECTION.PERSON_ID, "Person ID", False),
            FieldItem(FIELD_NAME_COLLECTION.MARK_ID, "Mark ID", False)
        )

        GROUP: FieldItemList = FieldItemList(
            GROUP_BASE,
            FieldItem(FIELD_NAME_COLLECTION.GROUP_ID, "Group id", False)
        ).visible(FIELD_NAME_COLLECTION.COMMENT, True)

        GROUP_STATISTICS: FieldItemList = FieldItemList(
            GROUP,
            FieldItem("Count", "Количество"),
        ).visible(FIELD_NAME_COLLECTION.COMMENT, False)

        TIME_TRACKING: FieldItemList = FieldItemList(FieldItem(FIELD_NAME_COLLECTION.FULL_NAME, "Полное имя"),
                                                     FieldItem(
                                                         FIELD_NAME_COLLECTION.TAB_NUMBER, "Табельное имя"),
                                                     FieldItem(
                                                         "TimeVal", "Время"),
                                                     FieldItem(
                                                         "Remark", "Remark"),
                                                     FieldItem(
                                                         "Mode", "Mode"))

        TIME_TRACKING_RESULT: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.FULL_NAME, "ФИО"),
            FieldItem(FIELD_NAME_COLLECTION.TAB_NUMBER, "Табельный номер"),
            FieldItem(
                "Date", "Дата"),
            FieldItem(
                "EnterTime", "Время прихода"),
            FieldItem(
                "ExitTime", "Время ухода"),
            FieldItem(
                "Duration", "Продолжительность"))

    class INRENTORY:

        ITEM: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME,
                      "Название инвентарного объекта"),
            FieldItem(FIELD_NAME_COLLECTION.INVENTORY_NUMBER,
                      "Инвентарный номер"),
            FieldItem(FIELD_NAME_COLLECTION.QUANTITY, "Количество"),
            FieldItem(FIELD_NAME_COLLECTION.NAME_COLUMN, None, False),
            FieldItem(FIELD_NAME_COLLECTION.INVENTORY_NUMBER_COLUMN, None, False),
            FieldItem(FIELD_NAME_COLLECTION.QUANTITY_COLUMN, None, False)
        )

    class AD:

        SEARCH_ATTRIBUTE: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.SEARCH_ATTRIBUTE_LOGIN, "Логин"),
            FieldItem(FIELD_NAME_COLLECTION.SEARCH_ATTRIBUTE_NAME, "Имя")
        )

        CONTAINER: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Название"),
            FieldItem(FIELD_NAME_COLLECTION.DESCRIPTION, "Описание")
        )

        TEMPLATED_USER: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.DESCRIPTION, "Описание"))

        USER: FieldItemList = FieldItemList(CONTAINER,
                                            FieldItem(
                                                FIELD_NAME_COLLECTION.LOGIN, "Логин"),
                                            FieldItem(
                                                FIELD_NAME_COLLECTION.TELEPHONE, "Телефон"),
                                            FieldItem(
                                                FIELD_NAME_COLLECTION.EMAIL, "Электронная почта"),
                                            FieldItem(
                                                FIELD_NAME_COLLECTION.DN, "Размещение"),
                                            FieldItem("userAccountControl", "Свойства аккаунта")).position(FIELD_NAME_COLLECTION.DESCRIPTION, 4)

        CONTAINER_TYPE: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.TEMPLATE_USER_CONTAINER,
                      "Шаблонный пользователь"),
            FieldItem(FIELD_NAME_COLLECTION.CONTAINER, "Контейнер"))

    class POLIBASE:

        PATIENT: FieldItemList = FieldItemList(FieldItem(FIELD_NAME_COLLECTION.FULL_NAME,
                                                         "ФИО пациента"),
                                               FieldItem(FIELD_NAME_COLLECTION.COMMENT,
                                                         "Комментарий пациента"))

    class POLICY:

        PASSWORD_TYPE: FieldItemList = FieldItemList(
            FieldItem("PC", "PC"),
            FieldItem("EMAIL", "Email"),
            FieldItem("SIMPLE", "Simple"),
            FieldItem("STRONG", "Strong"))

    class PRINTER:

        MAIN: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Name"),
            FieldItem("serverName", "Server name"),
            FieldItem("portName", "Host name"),
            FieldItem(FIELD_NAME_COLLECTION.DESCRIPTION, "Description"),
            FieldItem("adminDescription", "Admin description", False),
            FieldItem("driverName", "Driver name")
        )


class FIELD_COLLECTION_ALIAS(Enum):
    TIME_TRACKING: str = FIELD_COLLECTION.ORION.TIME_TRACKING
    PERSON: str = FIELD_COLLECTION.ORION.PERSON
    PATIENT: str = FIELD_COLLECTION.POLIBASE.PATIENT
    PERSON_DIVISION: str = FIELD_COLLECTION.ORION.PERSON_DIVISION
    PERSON_EXTENDED: str = FIELD_COLLECTION.ORION.PERSON_EXTENDED


LINK_EXT = "lnk"


class PrinterCommand(Enum):
    REPORT: str = "report"
    STATUS: str = "status"


class PASSWORD_GENERATION_ORDER:

    SPECIAL_CHARACTER: str = "s"
    LOWERCASE_ALPHABET: str = "a"
    UPPERCASE_ALPHABET: str = "A"
    DIGIT: str = "d"
    DEFAULT_ORDER_LIST: List[str] = [SPECIAL_CHARACTER,
                                     LOWERCASE_ALPHABET, UPPERCASE_ALPHABET, DIGIT]


class PASSWORD:

    class SETTINGS:

        SIMPLE: PasswordSettings = PasswordSettings(
            3, "", PASSWORD_GENERATION_ORDER.DEFAULT_ORDER_LIST, 0, 3, 0, 0, False)
        NORMAL: PasswordSettings = PasswordSettings(
            8, "!@#", PASSWORD_GENERATION_ORDER.DEFAULT_ORDER_LIST, 3, 3, 1, 1, False)
        STRONG: PasswordSettings = PasswordSettings(
            10, "#%+\-!=@()_",  PASSWORD_GENERATION_ORDER.DEFAULT_ORDER_LIST, 3, 3, 2, 2, True)
        DEFAULT: PasswordSettings = NORMAL
        PC: PasswordSettings = NORMAL
        EMAIL: PasswordSettings = NORMAL

    def get(name: str) -> SETTINGS:
        return PASSWORD.__getattribute__(PASSWORD.SETTINGS, name)


class LogTypes(Enum):
    MESSAGE: str = "message"
    COMMAND: str = "command"
    DEFAULT: str = MESSAGE

class LogChannels(Enum):
    BACKUP: int = auto()
    NOTIFICATION: int = auto()
    DEBUG_BOT: int = auto()
    DEBUG: int = auto()
    PRINTER: int = auto()
    PRINTER_BOT: int = auto()
    SYSTEM_BOT: int = auto()
    SYSTEM: int = auto()
    HR: int = auto()
    HR_BOT: int = auto()
    IT: int = auto()
    IT_BOT: int = auto()
    DEFAULT: int = NOTIFICATION

class LogLevels(Enum):
    NORMAL: int = 1
    ERROR: int = 2
    EVENT: int = 4
    DEBUG: str = 8
    TASK: int = 16
    NOTIFICATION: str = 32
    DEFAULT: str = NORMAL


class ServiceCommands(Enum):
    ping: int = auto()
    log: int = auto()
    command: int = auto()
    create_user_document: int = auto()
    create_time_tracking_report: int = auto()
    create_inventory_barcodes: int = auto()
    is_inventory_report: int = auto()
    get_inventory_report: int = auto()
    save_inventory_report_item: int = auto()
    close_inventory_report: int = auto()
    get_patient_by_pin: int = auto()

    user_is_exists_by_login: int = auto()
    get_user_by_full_name: int = auto()
    get_users_by_name: int = auto()
    get_active_users_by_name: int = auto()
    get_user_by_login: int = auto()
    get_template_list: int = auto()
    create_user_from_template: int = auto()
    create_user_in_container: int = auto()
    user_set_telephone: int = auto()
    authenticate: int = auto()
    user_set_password: int = auto()
    user_set_status: int = auto()
    get_containers: int = auto()
    printer_list: int = auto()
    get_users_by_job_position: int = auto()
    get_users_in_group: int = auto()
    user_remove: int = auto()

    printers_report: int = auto()
    printers_status: int = auto()

    get_free_marks: int = auto()
    get_person_divisions: int = auto()
    get_time_tracking: int = auto()
    is_mark_free: int = auto()
    get_mark_by_tab_number: int = auto()
    get_mark_by_person_name: int = auto()
    get_free_marks_group_statistics: int = auto()
    get_free_marks_by_group_id: int = auto()
    set_full_name_by_tab_number: int = auto()
    create_mark: int = auto()
    set_telephone_by_tab_number: int = auto()
    make_mark_as_free_by_tab_number: int = auto()
    remove_by_tab_number: int = auto()
    get_all_persons: int = auto()

    

class ServiceRoles(Enum):

    LOG: ServiceRoleValue = ServiceRoleValue("Log", "Log api service", CONST.HOST.LOG.NAME, CONST.RPC.PORT(1),
                                             commands=[ServiceCommands.log,
                                                       ServiceCommands.command],
                                             modules=["telegram-send"])

    DOCS: ServiceRoleValue = ServiceRoleValue("Docs", "Documents api service", 
                                                CONST.HOST.DOCS.NAME, 
                                                CONST.RPC.PORT(1),
                                              commands=[ServiceCommands.create_user_document,
                                                        ServiceCommands.create_time_tracking_report,
                                                        ServiceCommands.create_inventory_barcodes,
                                                        ServiceCommands.is_inventory_report,
                                                        ServiceCommands.get_inventory_report,
                                                        ServiceCommands.save_inventory_report_item,
                                                        ServiceCommands.close_inventory_report
                                                        ],
                                              modules=["xlsxwriter", "xlrd", "xlutils", "openpyxl", "python-barcode", "Pillow"])

    AD: ServiceRoleValue = ServiceRoleValue("ActiveDirectory", "Active directory api service", 
                                            CONST.HOST.AD.NAME, 
                                            CONST.RPC.PORT(), 
                                                commands=[ServiceCommands.user_is_exists_by_login,
                                                        ServiceCommands.get_user_by_full_name,
                                                        ServiceCommands.get_users_by_name,
                                                        ServiceCommands.get_active_users_by_name,
                                                        ServiceCommands.get_user_by_login,
                                                        ServiceCommands.get_template_list,
                                                        ServiceCommands.create_user_from_template,
                                                        ServiceCommands.create_user_in_container,
                                                        ServiceCommands.user_set_telephone,
                                                        ServiceCommands.authenticate,
                                                        ServiceCommands.user_set_password,
                                                        ServiceCommands.user_set_status,
                                                        ServiceCommands.get_containers,
                                                        ServiceCommands.printer_list,
                                                        ServiceCommands.get_users_by_job_position,
                                                        ServiceCommands.get_users_in_group,
                                                        ServiceCommands.user_remove
                                                        ], 
                                                    modules=["pyad", "pywin32"])
    
    PRINTER: ServiceRoleValue = ServiceRoleValue("Printer", "Printer api service", CONST.HOST.PRINTER.NAME, CONST.RPC.PORT(2),
                                                 commands=[ServiceCommands.printers_report,
                                                           ServiceCommands.printers_status,
                                                           ])

    ORION: ServiceRoleValue = ServiceRoleValue("Orion", 
                                                "Orion api service", 
                                                CONST.HOST.ORION.NAME, 
                                                CONST.RPC.PORT(),
                                                "\\orion\commands",
                                                 commands=[ServiceCommands.get_free_marks,
                                                            ServiceCommands.get_person_divisions,
                                                            ServiceCommands.get_time_tracking,
                                                            ServiceCommands.is_mark_free,
                                                            ServiceCommands.get_mark_by_tab_number,
                                                            ServiceCommands.get_mark_by_person_name,
                                                            ServiceCommands.get_free_marks_group_statistics,
                                                            ServiceCommands.get_free_marks_by_group_id,
                                                            ServiceCommands.set_full_name_by_tab_number,
                                                            ServiceCommands.create_mark,
                                                            ServiceCommands.set_telephone_by_tab_number,
                                                            ServiceCommands.make_mark_as_free_by_tab_number,
                                                            ServiceCommands.remove_by_tab_number,
                                                            ServiceCommands.get_all_persons],
                                               modules=["pymssql"])
                                
    POLIBASE: ServiceRoleValue = ServiceRoleValue(
        "POLIBASE", "Polibase api service", CONST.HOST.POLIBASE.NAME, CONST.RPC.PORT(), commands=[ServiceCommands.get_patient_by_pin], modules=["cx-Oracle"])

class LogCommands(Enum):

    DEBUG: LogCommand = LogCommand(
        "It is a debug command", LogChannels.NOTIFICATION, LogLevels.DEBUG.value)
    PRINTER_REPORT: LogCommand = LogCommand("Принтер {printer_name} ({location}):\n {printer_report}", LogChannels.PRINTER, LogLevels.NORMAL.value, (ParamItem(
        "printer_name", "Name of printer"), ParamItem("location", "Location"), ParamItem("printer_report", "Printer report"))),
    #
    LOG_IN: LogCommand = LogCommand(
        "Пользователь {full_name} ({login}) вошел с компьютера {computer_name}", LogChannels.SYSTEM, LogLevels.NORMAL.value, (ParamItem("full_name", "Name of user"), ParamItem("login", "Login of user"), ParamItem("computer_name", "Name of computer"))),

    START_SESSION: LogCommand = LogCommand(
        "Пользователь {full_name} ({login}) начал пользоваться программой {app_name}.\nВерсия: {version}.\nНазвание компьютера: {computer_name}", LogChannels.SYSTEM, LogLevels.NORMAL.value, (ParamItem("full_name", "Name of user"), ParamItem("login", "Login of user"), ParamItem("app_name", "Name of user"),  ParamItem("version", "Version"), ParamItem("computer_name", "Name of computer"))),

    SERVICE_STARTED: LogCommand = LogCommand(
        "Сервис {service_name} ({service_description}) запущен!\nИмя хоста: {host_name}\nПорт: {port}\nИдентификатор процесса: {pid}\n", LogChannels.SYSTEM, LogLevels.NORMAL.value, (ParamItem("service_name", "Name of service"), ParamItem("service_description", "Description of service"), ParamItem("host_name", "Name of host"), ParamItem("port", "Port"), ParamItem("pid", "PID"))),
    #
    POLIBASE_DB_BACKUP_START: str = LogCommand(
        "Start Polibase DataBase Dump backup",  LogChannels.BACKUP, LogLevels.NORMAL.value)
    POLIBASE_DB_BACKUP_COMPLETE: str = LogCommand(
        "Complete Polibase DataBase Dump backup",  LogChannels.BACKUP, LogLevels.NORMAL.value)
    #
    HR_NOTIFY_ABOUT_NEW_EMPLOYEE: str = LogCommand("День добрый, {hr_given_name}.\nДокументы для нового сотрудника: {employee_full_name} готовы!\nЕго корпоративная почта: {employee_email}.", LogChannels.HR, LogLevels.NOTIFICATION.value, (ParamItem(
        "hr_given_name", "Имя руководителя отдела HR"), ParamItem("employee_full_name", "ФИО нового сотрудника"), ParamItem("employee_email", "Корпаротивная почта нового сотрудника")))
    #
    IT_NOTIFY_ABOUT_NEW_USER: str = LogCommand("Добрый день, отдел Информационных технологий.\nДокументы для нового пользователя: {name} готовы!\nОписание: {description}\nЛогин: {login}\nПароль: {password}\nТелефон: {telephone}\nЭлектронная почта: {email}\nНомер карты доступа: {tab_number}", LogChannels.IT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("description", ""), ParamItem("login", ""), ParamItem("password", ""), ParamItem("telephone", ""),  ParamItem("email", ""),  ParamItem("tab_number", ""))),
    IT_TASK_AFTER_CREATE_NEW_USER: str = LogCommand("Добрый день, {it_user_name}.\nНеобходимо создать почту для пользователя: {name}\nАдресс электронной почты: {mail}\nПароль: {password}", LogChannels.IT, LogLevels.TASK.value, (ParamItem(
        "it_user_name", ""), ParamItem("name", ""), ParamItem("mail", ""), ParamItem("password", "")))