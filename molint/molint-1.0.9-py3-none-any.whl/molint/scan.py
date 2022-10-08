import os
import shutil
import argparse

create_init_path = []


def set_init(code_path):
    """
        创建init文件
    """

    for file in os.listdir(code_path):
        if not file.startswith('.'):
            file_path = os.path.join(code_path, file)
            if os.path.isdir(file_path):
                init = os.path.join(file_path, "__init__.py")
                if not os.path.exists(init):
                    create_init_path.append(init)
                    with open(init, "a") as file:
                        file.write("")
                set_init(file_path)
    root_init = os.path.join(code_path, "__init__.py")
    if not os.path.exists(root_init):
        create_init_path.append(root_init)
        with open(root_init, "a") as file:
            file.write("")


def create_rcfile(code_path, config_name):
    lint_path = os.path.join(code_path, config_name)
    if not os.path.exists(lint_path):
        shutil.copy(os.path.join(os.path.dirname(__file__), config_name), lint_path)
        create_init_path.append(lint_path)


def delete_init():
    """
        删除创建的init文件
    """
    while True:
        if len(create_init_path) == 0:
            break
        work_path = create_init_path.pop()
        if os.path.exists(work_path):
            os.remove(work_path)


def lint_scan(root_path, lang):
    """
        :param root_path: 扫描路径
        :param lang: py or js
    """
    if root_path in ['./', '.', '/']:
        root_path = os.getcwd()
    lang_map = {
        "py": ".pylintrc",
        "js": ".eslintrc.js"
    }
    create_rcfile(root_path, lang_map[lang])
    if lang == 'py':
        set_init(root_path)
        rc_ptah = os.path.join(root_path, lang_map[lang])
        cmd = f"pylint {root_path} --rcfile={rc_ptah}"
    if lang == 'js':
        print('注意：使用js扫描前，先确认是否已经安装配置过eslint的环境')
        print('安装方式:')
        print("\t 1. npm install eslint eslint-plugin-vue@latest --registry=https://registry.npm.taobao.org")
        print("\t 2. npm install")
        os.chdir(root_path)
        cmd = f'eslint ./ --ext .js,.wxml,.json,.wxss,.vue --ignore-pattern .eslintrc.js'  # js
    os.system(cmd)
    delete_init()


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('rp', nargs='?', default='./', help='代码路径')
        args = parser.parse_args()
        lang = "py" if bool(list(filter(lambda i: '.py' in i, os.listdir(args.rp)))) else "js"
        lint_scan(args.rp, lang)
    except KeyboardInterrupt:
        delete_init()


if __name__ == '__main__':
    main()
