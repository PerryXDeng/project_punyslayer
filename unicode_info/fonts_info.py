"""
file: fonts_info.py
language:python 3

extracts meta information from .ttf font files
"""
import numpy as np
import glob
from fontTools.ttLib import TTFont
import unicode_info.database as db


_FONT_DIR = "/home/pxd256/Workspace/project_punyslayer/fonts/"


def implemented_characters_indices(fontpath:str) -> np.array:
  """
  gets the indices of implemented characters in a font
  :param fontpath: file path to font
  :return: array of indices
  """
  ttf = TTFont(fontpath)
  cmap = ttf["cmap"].tables[0].cmap
  indices = list(cmap.keys())
  if len(indices) > 0:
    return np.asarray(indices)
  return np.asarray([32])


def count_implemented_characters(fontdir:str) -> (int, int):
  """
  gets the coverage of characters by font files in a directory
  :param fontdir: directory of fonts
  :return: number of covered characters and number of total characters
  """
  ttf_filepaths = glob.glob(fontdir, recursive=True)
  _, indices, n = db.map_blocks()
  covered = np.full(len(indices), False)
  for filepath in ttf_filepaths:
      covered[implemented_characters_indices(filepath)] = True
  coverage = np.sum(covered)
  return coverage, n


def main():
  print(count_implemented_characters(_FONT_DIR + "os_fonts/*/*.ttf"))


if __name__ == "__main__":
  main()
