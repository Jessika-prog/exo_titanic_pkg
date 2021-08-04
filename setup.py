from setuptools import setup, find_packages

setup(
    name='titanic_ML',
    version='0.0.1',
    packages=find_packages(),
    scripts=['scripts/titanic_script'],
    requirements=['numpy', 'pandas', 'matplotlib', 'seaborn', 'scikit-learn', 'fastapi', 'pytest', 'uvicorn']
    )
