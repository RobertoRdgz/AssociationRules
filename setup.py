from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='main',
    version='0.0.1',
    description='associationrules',
    long_description=readme(),
    classifiers=[
        'License :: OSI Approved :: MIT Licence',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],

    keywords='AssociationRules',
    url='',
    author='Aldair Serrano & Daniel Vera & Uzmar Gomez',
    author_email='uzmar.gomez@softtek.com',
    license='MIT',

    python_requires='>=3.7',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "flask",
        "numpy",
        "pandas",
    ],

    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': ['start-app=app:start_app']
    }
)