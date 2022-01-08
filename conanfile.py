from platform import version
from conans import ConanFile
from conans import tools
from conan.tools.cmake import CMakeToolchain, CMake
from conan.tools.layout import cmake_layout
from conan.tools.files import apply_conandata_patches


class PesconvertConan(ConanFile):
    name = "pesconvert"
    license = "MIT"
    author = "tschabo"
    url = ""
    description = "Library for reading PES files"
    topics = ("PES", "embroidery")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports = {"CMakeLists.txt", "winlib.patch"}

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
    
    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        apply_conandata_patches(self)
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["pesconvert"]