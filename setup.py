from setuptools import setup

setup(
	name='EventSystem.py',
	version='0.0.0',
	description='An event bus adapter for RabbitMQ.',
	url='https://gitlab.com/ProjektQ/EventSystem.py',
	author='Jan-Luca Klees',
	author_email='email@janlucaklees.de',
	license='MIT',
	packages=['event_system'],
	install_requires=[
		'pika == 0.13.0',
		'eventlet == 0.24.1',
		'schema == 0.6.8'
	],
	test_suite='nose2.collector.collector',
	tests_require=['nose2'],
	zip_safe=False
)

