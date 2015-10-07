import click

@click.group()
def cli():
	pass


@click.command()
def tests():
	click.echo("Running all autodiscovered testes...")
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity = 2).run(tests)

cli.add_command(tests)

if __name__ == "__main__":
	cli()