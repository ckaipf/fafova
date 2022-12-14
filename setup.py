from setuptools import setup, find_packages

setup(
    name                           = 'fafova',
    packages                       = find_packages(),
    include_package_data           = True,
    entry_points={
        "console_scripts": [
            "fafova=fafova.__main__:app",
        ]
    },
    install_requires=[
        'typer',
        'biopython'
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov',
        ],
    },
)