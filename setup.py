# -*- coding: utf-8 -*-

import setuptools

import zhDateTime

setuptools.setup(
    name="zhDateTime",
    version=zhDateTime.__version__,
    author="Eilles Wan",
    author_email="EillesWan@outlook.com",
    description="中式日期时间库，附带数字汉字化功能。",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="""版权所有 © 2025 金羿ELS
Copyright (C) 2025 Eilles(EillesWan@outlook.com)

zhDateTime is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.""",
    url="https://gitee.com/EillesWan/zhDateTime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mulan Permissive Software License v2 (MulanPSL-2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
