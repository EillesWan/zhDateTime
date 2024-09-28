# -*- coding: utf-8 -*-

import setuptools

import zhDateTime

setuptools.setup(
    name="zhDateTime",
    version=zhDateTime.__version__,
    author="Eilles Wan",
    author_email="EillesWan@outlook.com",
    description="一个简单的小巧的中式日期时间库，附带数字汉字化操作。",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitee.com/EillesWan/zhDateTime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
