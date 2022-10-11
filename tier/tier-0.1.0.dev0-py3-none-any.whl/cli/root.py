# internal
from tier.cli.parser import parser
from tier.internal.logging import set_verbosity


def root():

    args = parser.parse_args()

    kwargs = vars(args)
    handler = kwargs.pop('handler')
    verbosity = kwargs.pop('verbose')

    if verbosity:
        set_verbosity(verbosity)

    handler(**kwargs)
