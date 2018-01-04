#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
from conans.model.version import Version
import os

class LibnameConan(ConanFile):
    name = "cli11"
    version = "1.3.0"
    description = "Command line parser for C++11"
    url = "https://github.com/bincrafters/conan-cli11"
    license = "BSD 3-Clause"
    exports = ["LICENSE.md"]
    settings = "compiler"

    def source(self):
        source_url = "https://github.com/CLIUtils/CLI11"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "CLI11-" + self.version
        os.rename(extracted_dir, "sources")
    
    def package(self):
        self.copy(pattern="LICENSE", src="sources")
        self.copy(pattern="*", dst="include", src="sources/include")

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        v = Version(str(self.settings.compiler.version))
        if self.settings.compiler == "gcc":
            if v >= "5":
                self.cpp_info.defines = [ '_GLIBCXX_USE_CXX11_ABI=1' ]
            else:
                self.cpp_info.defines = [ '_GLIBCXX_USE_CXX11_ABI=0' ]

        if str(self.settings.compiler) in [ "gcc", "apple-clang", "clang" ]:
            self.cpp_info.cppflags = [ "-std=c++11" ]

