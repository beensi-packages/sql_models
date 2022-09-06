from setuptools import setup, find_packages

setup(
    name='sql_models',
    version='0.01',
    license='BEENSI',
    author='beensi.com dev group',
    # author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/beensi-packages/sql_models.git',
    # keywords='',
    install_requires=[],
)
