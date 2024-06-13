from setuptools import setup, find_packages

setup(
    name="sms_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "twilio"
    ],
    entry_points={
        'console_scripts': [
            'sms_package=sms_app.main:app',
        ],
    },
)