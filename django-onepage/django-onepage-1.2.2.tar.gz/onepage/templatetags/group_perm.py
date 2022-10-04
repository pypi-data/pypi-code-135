from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='has_perm')
def has_perm(user, perm_name):
    all_perms = user.get_all_permissions()
    # print('Template Level has perms : ', has_perm)
    # print('Template Level ALL perms : ', all_perms)
    if perm_name in all_perms:
        return True
    else:
        return False


@register.filter(name='joinby')
def joinby(value, arg):
    list =[]
    if value:
        list = value.split(",")
    return list
