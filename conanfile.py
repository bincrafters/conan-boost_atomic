#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostAtomicConan(base.BoostBaseConan):
    name = "boost_atomic"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_atomic"
    lib_short_names = ["atomic"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_type_traits"
    ]
