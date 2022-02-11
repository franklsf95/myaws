import setuptools

setuptools.setup(
    name="myaws",
    version="0.0.1",
    py_modules=[
        "myaws",
    ],
    install_requires=[
        "boto3",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "myaws = myaws:cli",
        ],
    },
)
