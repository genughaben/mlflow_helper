from setuptools import setup, find_packages

setup(
    name='mlflow_helpers',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'mlflow',
    ],
    author='genughaben',
    author_email='fwolf@posteo.de',
    description='Helper functions for standardized MLflow tracking',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/genughaben/mlflow_helpers',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
