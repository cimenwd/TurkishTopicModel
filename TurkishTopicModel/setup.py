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
)
