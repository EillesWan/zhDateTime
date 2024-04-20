# -*- coding: utf-8 -*-

import setuptools

import zhDateTime

setuptools.setup(
    name="pyLunar",
    version=zhDateTime.__version__,
    author="Eilles Wan",
    author_email="EillesWan@outlook.com",
    description="一个简单的小巧的中式日期时间库，支持农历公历互相转换，支持时辰刻数的时间表达转换。",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitee.com/EillesWan/zhDateTime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
)
