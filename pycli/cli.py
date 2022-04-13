
import argparse
import functools

def argument(*name_or_flags, **kwargs):
    """
    Convenience function to properly format arguments to pass to the
    register decorator.
    """
    return (list(name_or_flags), kwargs)

class Cli(object):
    def __init__(self, **kwargs) -> None:
        self.parser = argparse.ArgumentParser(**kwargs)
        self.sub_commands: list[tuple] = []

    def register(self, arguments):
        """
        Registers functions to be used as subcommands or as endpoint scripts.
        Call the class to use subcommands or call the function this is used on
        to just parse its own args without using subcommands
        """
        def outer(func):
            @functools.wraps(func)
            def decorator():
                parser = argparse.ArgumentParser(description=func.__doc__)
                for name_or_flags, kwargs in arguments:
                    parser.add_argument(*name_or_flags, **kwargs)
                return func(parser.parse_args())
            self.sub_commands.append(
                (func, arguments)
            )
            return decorator
        return outer

    def __call__(self):
        subparsers = self.parser.add_subparsers(dest='subcommand')
        for func, arguments in self.sub_commands:
            parser = subparsers.add_parser(func.__name__,
                                           description=func.__doc__)
            for name_or_flags, kwargs in arguments:
                parser.add_argument(*name_or_flags, **kwargs)
            parser.set_defaults(func=func)
        args = self.parser.parse_args()
        if args.subcommand is None:
            self.parser.print_help()
        else:
            args.func(args)