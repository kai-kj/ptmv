import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README-PIP.md").read_text()

setup(
    name="ptmv",
    version="1.0.1",
    description="An utf-8/truecolor image and video viewer for the terminal",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kal39/ptmv",
    author="kal39",
    author_email="kaikitagawajones@gmail.com",
    license="MIT",
    packages=["ptmv"],
    include_package_data=True,
    install_requires=["wheel", "opencv-python", "simpleaudio", "yt_dlp"],
    entry_points={
        "console_scripts": [
            "ptmv=ptmv.__main__:main",
        ]
    },
)
