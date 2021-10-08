import setuptools

setuptools.setup(
    name="djangoshortcuts",
    version="0.0.1",
    author="Zhang",
    description="Shortcuts to create files easily when using django",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "dj=djangoshortcuts.command:main",
        ]
    },
    python_requires='>=3.5.2',
)
