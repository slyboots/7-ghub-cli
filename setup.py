from setuptools import setup, find_packages

setup(
    name='ghub',
    version='0.1',
    description='A simple cli for managing github repos',
    url='https://github.com/slyboots/7-ghub-cli',
    author='slyboots',
    author_email='admin@slyb--ts.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ghub = ghub.app:entry_func'
        ]
    }
)
