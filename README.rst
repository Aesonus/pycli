**PyCLI**
=================
This package is to provide functionality for subcommands, and also scripts
as well.

Vision
-----------------
The idea of this project is to allow a developer of python applications to
easily provide argument parsing using subcommands with arguments to the
package's __main__.py file and/or provide argument parsing to endpoint
scripts defined in the package manager's configuration file that are using
individual subcommands as self contained scripts. This is all achieved by
using a callable class that has a decorator to define subcommands, such that
only one class is needed.

Usage
-----
1. Import the module and create a Cli instance:

    .. code-block:: python

        """__main__.py"""

        import pycli.cli as pycli
        prog = pycli.Cli(description="A sample program")

2. Decorate your subcommand

    .. code-block:: python

        """__main__.py (cont.)"""

        @prog.register(
            [pycli.argument('--argument', '-a', action='store_true')]
        )
        def my_command(args):
            print(args)

3. Call the Cli instance in this module to run using subcommands

    .. code-block:: python

        """__main__.py (cont.)"""

        if __name__ == '__main__':
            prog()

4. Use subcommand as a script installed at package install time:

    .. code-block:: toml

        # Using Poetry in pyproject.toml
        [tool.poetry.scripts]
            command = "example.__main__:my_command"



