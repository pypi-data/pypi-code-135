from setuptools import Extension, setup


setup(
    ext_modules = [
        Extension(
            name="unicode_age",
            sources=[
                "src/unicode_age.pyx",
            ],
        ),
    ]
)
