from conans import ConanFile, CMake, tools
from os.path import splitext, join


class RangesNextConan(ConanFile):
    name = "rangesnext"
    version = "0.1"
    license = "LLVM"
    author = "Richard Vock <vock@cs.uni-bonn.de>"
    url = "https://github.com/richard-vock/conan-rangesnext"
    description = "Implements a set of views intended to be proposed to a future C++ standard."
    topics = ("stl", "ranges")
    settings = "os"

    def source(self):
        self.run("git clone https://github.com/cor3ntin/rangesnext")
        src_folder = join(self.source_folder, "rangesnext/include/cor3ntin")
        src_files = [join(src_folder,f) for f in tools.relative_dirs(src_folder) if splitext(f)[1] == '.hpp']
        for f in src_files:
            tools.replace_in_file(f, "cor3ntin::", "", strict=False)
            tools.replace_in_file(f, "cor3ntin/", "", strict=False)


    def package(self):
        self.copy("*.hpp", dst="include", src="rangesnext/include/cor3ntin", keep_path=True)

    def package_id(self):
        self.info.header_only()

