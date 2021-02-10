from setuptools import setup

setup(
	name='dock-python-cli',
	version='0.1.2',
	author='https://github.com/Pebaz',
	py_modules=['dock_cli'],
	entry_points={
		'console_scripts' : [
			'dock=dock_cli:main'
		]
	}
)
