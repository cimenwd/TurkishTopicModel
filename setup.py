import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Turkish Topic Model",
    version="0.0.1",
    author="Ali ÇİMEN, Sevinç GÜLSEÇEN",
    author_email="cimenwd@gmailcom, gulsecen@istanbul.edu.tr",
    description="Türkçe metin ön işleme ve konu analizi konusunda hazırlanmış fonksiyonlar kümesi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['pymysql >= 1.0.2',
'pandas >= 1.3.5',
'jpype1 >=1.3.0',
'requests >= 2.26.0',
'nltk >= 3.6.7',
'tomotopy >= 0.12.2']
)
