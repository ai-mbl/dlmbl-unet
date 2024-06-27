"""A basic UNet backbone for DL@MBL exercises"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("dlmbl-unet")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Morgan Schwartz"
__email__ = "msschwartz21@gmail.com"
