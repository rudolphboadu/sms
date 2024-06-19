from setuptools import setup, find_packages

setup(
    name="PyCommsPay SMS",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "twilio"
    ],
    entry_points={
        'console_scripts': [
            'sms_package= app.main:app',
        ],
    },
)