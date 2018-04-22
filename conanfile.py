#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class Cli11Conan(ConanFile):
    name = "cli11"
    version = "1.5.3"
    description = "Command line parser for C++11"
    url = "https://github.com/bincrafters/conan-cli11"
    homepage = "https://github.com/CLIUtils/CLI11"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD 3-Clause"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        source_url = "https://github.com/CLIUtils/CLI11"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "CLI11-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_dir = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()
