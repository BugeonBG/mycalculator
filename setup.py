import setuptools

setuptools.setup (
    include_package_data=true,
  name='calculator',
  version='0.0.1',
  description='oss-dev my calculator',
  author='BugeonBG',
  author_email='jbg0118@naver.com',
  url = "https://github.com/BugeonBG/mycalculator",
  download_url = "https://github.com/BugeonBG/mycalculator/archive/refs/tags/v0.0.1.zip",
   install_requires=['pytest']
   long_description = 'oss-dev calculator python module',
    long_description_content_type = 'text/markdown',
    classifiers=[
        "programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
