# -*- coding: utf-8 -*-

import setuptools

import zhLunarDate

setuptools.setup(
    name="pyLunar",
    version=zhLunarDate.__version__,
    author="Eilles Wan",
    author_email="EillesWan@outlook.com",
    description="简易Python农历日期库，利用本地数据进行公历、农历互相转换",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitee.com/EillesWan/pyLunar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
)
