from setuptools import setup, find_packages

setup(
    name="todo-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "todo=todo_cli.main:main",
        ],
    },
    python_requires=">=3.6",
    description="A simple command-line TODO list application",
    author="EliteGoodDev",
) 