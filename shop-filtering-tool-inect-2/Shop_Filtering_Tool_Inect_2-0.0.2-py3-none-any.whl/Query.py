try:
    from Filter import Filter
except ModuleNotFoundError:
    from shop.Filter import Filter

try:
    from Shop import Shop
except ModuleNotFoundError:
    from shop.Shop import Shop

try:
    from BinaryTree import BinaryTreeNode, BinaryTree
except ModuleNotFoundError:
    from shop.BinaryTree import BinaryTree, BinaryTreeNode

try:
    from Infix_to_Polish import infix_to_polish, evaluate_polish
except ModuleNotFoundError:
    from shop.Infix_to_Polish import infix_to_polish, evaluate_polish


# values of node are supposed to be filters
class Query(BinaryTree):
    def fix(self):
        def fix_node(root):
            if not isinstance(root.value, Filter):
                root.value = None
            if root.left() is not None:
                root.left().key = 2 * root.key
                fix_node(root.left())
            if root.right() is not None:
                root.right().key = 2 * root.key + 1
                fix_node(root.right())
        self.root.key = 1
        fix_node(self.root)

    def __init__(self, root=BinaryTreeNode(1, '')):
        super().__init__(root)
        self.fix()

    def is_good(self, item: dict):
        current_node = self.root
        while True:
            good = current_node.value.is_good(item)
            if good:
                if current_node.left() is None:
                    return True
                current_node = current_node.left()
            else:
                if current_node.right() is None:
                    return False
                current_node = current_node.right()

    def apply(self, shop: Shop) -> Shop:
        shop.unify()
        result = []
        for item in shop:
            if self.is_good(item):
                result.append(item)
        return Shop.from_list(result)

    @staticmethod
    def from_string(__input):
        special_chars = '()+-'

        def filter_from_seed(seed):
            # proxy function
            # seed format: colname,*args (separted by ,)
            formatted_seed = seed.replace(';', '')
            if formatted_seed[-1] != ',':
                formatted_seed = formatted_seed + ','
            col_name = None
            args = []
            while formatted_seed:
                if col_name is None:
                    col_name = formatted_seed[:formatted_seed.find(',')]
                else:
                    args.append(formatted_seed[:formatted_seed.find(',')])
                formatted_seed = formatted_seed[formatted_seed.find(',') + 1:]

            return Filter(col_name, args, empty=False)

        def next_filter_seed(string):
            for i, j in enumerate(string):
                if j in special_chars:
                    if j == ';':
                        return i + 1, string[:i]
                    return i, string[:i]
            return len(string), string

        def parse(string):
            temp_lst = []
            proxy = string.replace(' ', '')
            while proxy:
                if proxy[0] in special_chars:
                    temp_lst.append(proxy[0])
                    proxy = proxy[1:]
                else:
                    reminder, seed = next_filter_seed(proxy)
                    #  temp_lst.append(filter_from_seed(seed))
                    temp_lst.append(seed)  # for development purposes
                    proxy = proxy[reminder:]
            return temp_lst

        parsed_input = parse(__input)
        parsed_input = infix_to_polish(parsed_input)

        def right(old: BinaryTree, new: BinaryTree):
            old.append_side(new, 'right')
            return old

        def left(old: BinaryTree, new: BinaryTree):
            old.append_side(new, 'left')
            return old

        def translate(seed):
            return Query(BinaryTreeNode(1, filter_from_seed(seed)))

        operators = {'translate': translate, '+': left, '-': right}
        return evaluate_polish(parsed_input, operators)


def test():
    root = BinaryTreeNode(1, Filter('', [], empty=True))
    a = Query(root)
    a[2] = Filter(1, ['b'])
    a[5] = Filter(1, ['ab'])
    a[11] = Filter(2, ['dd'])
    a[23] = Filter(1, ['a'])
    item = {'title': 'Regał do'}
    item2 = {'title': 'noś'}
    print(a.is_good(item), a.apply(Shop.from_list([item, item2])))


def test2():
    query = Query.from_string(input('Podaj kod\n'))
    item1 = {'title': 'Regał do'}
    item2 = {'title': 'noś'}
    print(query)
    print(query.is_good(item1), query.is_good(item2))


if __name__ == '__main__':
    test2()
