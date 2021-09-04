import setuptools
from pathlib import Path

setuptools.setup(
    name='plotfa',
    author='Behnam Sajadifar',
    author_email='behnamsajadi@gmail.com',
    version="0.0.3",
    description='Create Persian plots using matplotlob/seaborn',
    long_description=Path("README.md").read_text(encoding="utf8"),
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib', 'seaborn', 'arabic-reshaper', 'python-bidi'
    ],
)