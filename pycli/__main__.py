from . import cli

prog = cli.Cli()

@prog.register([
    cli.argument('--test', '-t', action='store')
])
def command(args):
    print(args)

if __name__ == '__main__':
    prog()
