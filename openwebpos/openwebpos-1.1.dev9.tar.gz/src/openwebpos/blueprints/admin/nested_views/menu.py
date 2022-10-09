from flask import Blueprint, render_template, redirect, url_for

from openwebpos.blueprints.pos.models.menu import Menu, Item, Ingredient, Recipe

from ..forms import MenuForm, MenuItemForm

bp = Blueprint('menu', __name__, url_prefix='/menu',
               template_folder='templates')


@bp.route('/')
def index():
    return render_template('admin/menu/index.html')


@bp.get('/list')
def list_all():
    """
    Renders the admin menus page.
    """
    _menus = Menu.query.all()
    form = MenuForm()
    return render_template('admin/menu/list.html', title='Admin - Menus',
                           menus=_menus, form=form)


@bp.post('/list')
def post_menu():
    """
    Adds a menu to the database.
    """
    form = MenuForm()
    if form.validate_on_submit():
        m = Menu(name=form.name.data)
        m.save()
        return redirect(
            url_for('.menu_items', menu_name=m.name))
    return redirect(url_for('.list_all'))


@bp.post('/<int:menu_id>/update')
def update_menu(menu_id):
    """
    Updates a menu in the database.
    """
    form = MenuForm()
    if form.validate_on_submit():
        m = Menu.query.get(menu_id)
        m.name = form.name.data
        m.save()
        return redirect(url_for('.list_all'))
    return redirect(url_for('.list_all'))


@bp.get('/<int:menu_id>/delete')
def delete_menu(menu_id):
    """
    Deletes a menu from the database.
    """
    m = Menu.query.get_or_404(menu_id)
    if m.not_empty():
        return redirect(url_for('.list_all'))
    m.delete()
    return redirect(url_for('.list_all'))


@bp.get('/<string:menu_name>/items')
def menu_items(menu_name):
    """
    Renders the admin menu items page.
    """
    _menu = Menu.query.filter_by(name=menu_name).first_or_404()
    _menu_items = Item.query.filter_by(menu_id=_menu.id).all()
    _menu_ingredients = Recipe.query.filter_by(menu_id=_menu.id).all()
    # _ingredients = Ingredient.query.filter_by(active=True).all()
    _ingredients = Ingredient.list_ingredients_not_in_menu(_menu.id)
    form = MenuItemForm()
    _title = f'Admin - {_menu.name} Menu Items'
    return render_template('admin/menu/items.html', title=_title,
                           menu_items=_menu_items, menu=_menu, form=form,
                           menu_ingredients=_menu_ingredients,
                           ingredients=_ingredients)


@bp.post('/<string:menu_name>/items')
def add_menu_items(menu_name):
    """
    Adds a menu item to the database.
    """
    form = MenuItemForm()
    if form.validate_on_submit():
        m = Menu.query.filter_by(name=menu_name).first_or_404()
        mi = Item(name=form.name.data, price=form.price.data, menu_id=m.id)
        mi.save()
        return redirect(
            url_for('.menu_items', menu_name=menu_name))
    return redirect(url_for('admin.admin_menu.menu_items', menu_name=menu_name))


@bp.route('/<string:menu_name>/<string:menu_item_name>/edit',
          methods=['GET', 'POST'])
def edit_menu_item(menu_name, menu_item_name):
    """
    Updates a menu item in the database.
    """
    form = MenuItemForm(
        obj=Item.query.filter_by(name=menu_item_name).first_or_404())
    _item_id = Item.query.filter_by(
        name=menu_item_name).first_or_404().id
    _ingredients = Ingredient.query.filter_by(active=True).all()
    if form.validate_on_submit():
        mi = Item.query.filter_by(name=menu_item_name).first_or_404()
        mi.name = form.name.data
        mi.price = form.price.data
        mi.save()
        return redirect(url_for('.menu_items', menu_name=menu_name))
    return render_template('admin/edit_menu_item.html', form=form,
                           ingredients=_ingredients,
                           item_id=_item_id)


@bp.get('/<string:menu_name>/<string:menu_item_name>/delete')
def delete_menu_item(menu_name, menu_item_name):
    """
    Deletes a menu item from the database.
    """
    m = Menu.query.filter_by(name=menu_name).first_or_404()
    mi = Item.query.filter_by(name=menu_item_name,
                              menu_id=m.id).first_or_404()
    mi.delete()
    return redirect(url_for('.menu_items', menu_name=menu_name))


@bp.get('/<string:menu_name>/<string:menu_item_name>/active-toggle')
def toggle_menu_item_active(menu_name, menu_item_name):
    """
    Toggles the active state of a menu item.
    """
    m = Menu.query.filter_by(name=menu_name).first_or_404()
    mi = Item.query.filter_by(name=menu_item_name,
                              menu_id=m.id).first_or_404()
    mi.active = not mi.active
    mi.save()
    return redirect(url_for('.menu_items', menu_name=menu_name))
