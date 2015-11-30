from distutils.core import setup, Extension

setup(
    name         = "pytoxcore",
    version      = "0.0.14",
    description  = 'Python binding for ToxCore',
    author       = 'Anton Batenev',
    author_email = 'antonbatenev@yandex.ru',
    url          = 'http://github.com/abbat/pytoxcore',
    license      = 'GPL',
    ext_modules  = [
        Extension(
            "pytoxcore",
            sources            = ["pytox.c", "pytoxcore.c", "pytoxav.c"],
            define_macros      = [],
            include_dirs       = ["/usr/tox/include"],
            library_dirs       = ["/usr/tox/lib"],
            extra_compile_args = ["-Wall", "-Wno-declaration-after-statement"],
            libraries          = ["toxcore", "toxav", "sodium", "vpx", "opus", "rt"]
        )
    ]
)
