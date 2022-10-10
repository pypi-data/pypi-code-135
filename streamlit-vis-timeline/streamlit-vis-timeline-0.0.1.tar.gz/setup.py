import setuptools

setuptools.setup(
    name="streamlit-vis-timeline",
    version="0.0.1",
    author="Qiusheng Wu",
    author_email="giswqs@gmail.com",
    description="Streamlit component for rendering vis.js timeline",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/giswqs/streamlit-timeline",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
