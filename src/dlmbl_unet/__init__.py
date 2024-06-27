"""A basic UNet backbone for DL@MBL exercises"""

from importlib.metadata import PackageNotFoundError, version

from .unet import ConvBlock, CropAndConcat, Downsample, OutputConv, UNet

try:
    __version__ = version("dlmbl-unet")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Morgan Schwartz"
__email__ = "msschwartz21@gmail.com"
__author__ = "Morgan Schwartz"
__email__ = "msschwartz21@gmail.com"
__all__ = ["ConvBlock", "CropAndConcat", "Downsample", "OutputConv", "UNet"]
