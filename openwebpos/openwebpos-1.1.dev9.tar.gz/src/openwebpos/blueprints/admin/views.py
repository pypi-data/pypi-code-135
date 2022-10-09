from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required

from openwebpos.blueprints.user.decorators import manager_required, \
    admin_required
from openwebpos.blueprints.pos.models.menu import Menu, Ingredient, Recipe
from openwebpos.blueprints.pos.models.order import OrderPager, OrderType, \
    TransactionType, Order
from .models import Company, CompanyLocation, CompanyPrinter
from .forms import PagerForm, IngredientForm, \
    CompanyForm, CompanyLocationForm, CompanyPrinterForm

from .nested_views import nested_views

bp = Blueprint('admin', __name__, template_folder='templates',
               url_prefix='/admin')

for nested_view in nested_views:
    bp.register_blueprint(nested_view)


@bp.before_request
@login_required
@manager_required
def before_request():
    """
    Protects all the admin endpoints.
    """
    pass


@bp.get('/')
def index():
    """
    Render the admin index page.
    """
    return render_template('admin/index.html', title='Admin')


@bp.get('/settings')
def settings():
    """
    Renders the admin settings page.
    """
    return render_template('admin/settings.html', title='Admin - Settings')


@bp.get('/config')
def config():
    """
    Renders the admin config page.
    """
    return render_template('admin/config.html', title='Admin - Config')


@bp.get('/company')
def company():
    """
    Renders the admin company page.
    """
    _company = Company.query.first()
    company_form = CompanyForm(obj=_company)
    return render_template('admin/company.html', title='Admin - Company',
                           company_form=company_form, company=_company)


@bp.post('/company')
def company_post():
    """
    Handles the admin company page form submission.
    """
    _company = Company.query.first()
    company_form = CompanyForm()

    if company_form.validate_on_submit():
        if _company is None:
            _company = Company(name=company_form.name.data)
            _company.save()
        else:
            _company.name = company_form.name.data
            _company.update()
        return redirect(url_for('admin.company'))

    return redirect(url_for('admin.company'))


@bp.get('/company/locations')
def company_locations():
    """
    Renders the admin company locations page.
    """
    _locations = CompanyLocation.query.all()
    location_form = CompanyLocationForm()
    return render_template('admin/company_locations.html',
                           title='Admin - Company Locations',
                           location_form=location_form,
                           locations=_locations)


@bp.post('/company/location')
def company_location_post():
    """
    Handles the admin company location form submission.
    """
    location_form = CompanyLocationForm()
    print(location_form.name.data)

    if location_form.validate_on_submit():
        _location = CompanyLocation(name=location_form.name.data,
                                    address=location_form.address.data,
                                    city=location_form.city.data,
                                    state=location_form.state.data,
                                    zipcode=location_form.zipcode.data,
                                    phone=location_form.phone.data,
                                    fax=location_form.fax.data,
                                    email=location_form.email.data,
                                    company_id=Company.query.first().id)
        _location.save()
        print(_location.name)
        return redirect(url_for('admin.company'))
    return redirect(url_for('admin.company'))


@bp.get('/company/printers')
def company_printers():
    """
    Renders the admin company printers page.
    """
    _printers = CompanyPrinter.query.all()
    _locations = CompanyLocation.query.all()
    printer_form = CompanyPrinterForm()
    return render_template('admin/company_printers.html',
                           title='Admin - Company Printers',
                           printer_form=printer_form,
                           printers=_printers, locations=_locations)


@bp.get('/company/printer/delete/<int:printer_id>')
def company_printer_delete(printer_id):
    """
    Handles the admin company printer delete request.
    """
    _printer = CompanyPrinter.query.get_or_404(printer_id)
    _printer.delete()
    return redirect(url_for('admin.company_printers'))


@bp.post('/company/printer')
def company_printer_post():
    """
    Handles the admin company printer form submission.
    """
    printer_form = CompanyPrinterForm()

    if printer_form.validate_on_submit():
        location = request.form['companyLocation']
        cp = CompanyPrinter(name=printer_form.name.data,
                            ip=printer_form.ip.data,
                            port=printer_form.port.data,
                            type=printer_form.type.data,
                            company_location_id=location)
        cp.save()
        return redirect(url_for('admin.company_printers'))
    return redirect(url_for('admin.company_printers'))


@bp.get('/pagers')
def pagers():
    """
    Renders the admin pagers page.
    """
    _pagers = OrderPager.query.filter_by(hidden=False).all()
    form = PagerForm()
    return render_template('admin/pagers.html', title='Admin - Pagers',
                           pagers=_pagers, form=form)


@bp.post('/pagers')
def add_pagers():
    """
    Adds a pager to the database.
    """
    form = PagerForm()
    if form.validate_on_submit():
        p = OrderPager(name=form.name.data)
        p.save()
        return redirect(url_for('admin.pagers'))
    return redirect(url_for('admin.pagers'))


@bp.get('/pagers/<int:pager_id>/active-toggle')
def toggle_pager_active(pager_id):
    """
    Toggles the active state of a pager.
    """
    p = OrderPager.query.get_or_404(pager_id)
    p.active = not p.active
    p.save()
    return redirect(url_for('admin.pagers'))


@bp.get('/pagers/<int:pager_id>/delete')
def delete_pager(pager_id):
    """
    Deletes a pager from the database.
    """
    p = OrderPager.query.get_or_404(pager_id)
    p.delete()
    return redirect(url_for('admin.pagers'))


@bp.get('/order-types')
def order_types():
    """
    Renders the admin order types page.
    """
    _order_types = OrderType.query.all()
    return render_template('admin/order_types.html',
                           title='Admin - Order Types',
                           order_types=_order_types)


@bp.get('/order-types/<int:order_type_id>/active-toggle')
def toggle_order_type_active(order_type_id):
    """
    Toggles the active state of an order type.
    """
    ot = OrderType.query.get_or_404(order_type_id)
    ot.active = not ot.active
    ot.save()
    return redirect(url_for('admin.order_types'))


@bp.get('/transaction-types')
def transaction_types():
    """
    Renders the admin transaction types page.
    """
    _transaction_types = TransactionType.query.all()
    return render_template('admin/transaction_types.html',
                           title='Admin - Transaction Types',
                           transaction_types=_transaction_types)


@bp.get('/transaction-types/<int:transaction_type_id>/active-toggle')
def toggle_transaction_type_active(transaction_type_id):
    """
    Toggles the active state of a transaction type.
    """
    tt = TransactionType.query.get_or_404(transaction_type_id)
    tt.active = not tt.active
    tt.save()
    return redirect(url_for('admin.transaction_types'))


@bp.get('/ingredients')
def ingredients():
    """
    Renders the admin ingredients page.
    """
    _ingredients = Ingredient.query.all()
    form = IngredientForm(price=0.00)
    return render_template('admin/ingredients.html',
                           title='Admin - Ingredients',
                           ingredients=_ingredients, form=form)


@bp.post('/ingredients')
def add_ingredient():
    """
    Adds an ingredient to the database.
    """
    form = IngredientForm()
    if form.validate_on_submit():
        i = Ingredient(name=form.name.data, price=form.price.data)
        i.save()
        return redirect(url_for('admin.ingredients'))
    return redirect(url_for('admin.ingredients'))


@bp.get('/ingredients/<int:ingredient_id>/active-toggle')
def toggle_ingredient_active(ingredient_id):
    """
    Toggles the active state of an ingredient.
    """
    i = Ingredient.query.get_or_404(ingredient_id)
    i.active = not i.active
    i.save()
    return redirect(url_for('admin.ingredients'))


@bp.get('/ingredients/<int:ingredient_id>/addon-toggle')
def toggle_ingredient_addon(ingredient_id):
    """
    Toggles the addon state of an ingredient.
    """
    i = Ingredient.query.get_or_404(ingredient_id)
    i.addon = not i.addon
    i.save()
    return redirect(url_for('admin.ingredients'))


@bp.get('/ingredients/<int:ingredient_id>/delete')
def delete_ingredient(ingredient_id):
    """
    Deletes an ingredient from the database.
    """
    i = Ingredient.query.get_or_404(ingredient_id)
    i.delete()
    return redirect(url_for('admin.ingredients'))


@bp.get('/recipe/<int:menu_id>/<int:ingredient_id>/add')
def add_recipe(menu_id, ingredient_id):
    """
    Renders the admin add recipe page.
    """
    _menu = Menu.query.get_or_404(menu_id)
    _ingredient = Ingredient.query.get_or_404(ingredient_id)
    _recipe = Recipe(menu_id=_menu.id, ingredient_id=_ingredient.id)
    _recipe.save()
    return redirect(
        url_for('admin.admin_menu.menu_items', menu_name=_menu.name))


@bp.get('/sales')
def sales():
    """
    Renders the admin orders page.
    """
    _orders = Order.query.all()
    return render_template('admin/sales.html', title='Admin - Sales',
                           orders=_orders)


@bp.get('/sales/<int:order_id>/delete')
def delete_order(order_id):
    """
    Deletes an order from the database.
    """
    Order.delete_order(order_id)
    return redirect(url_for('admin.sales'))
