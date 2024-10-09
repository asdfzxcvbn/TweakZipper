import os
import sys
import argparse
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile

from TweakZipper import helpers

def main():
  parser = argparse.ArgumentParser(
    description="deb/dylib -> trollfools zip converter"
  )

  parser.add_argument(
    "-o", metavar="output", required=True,
    help="zipfile to create"
  )

  parser.add_argument(
    "-f", metavar="file", required=True, nargs="+",
    help="the files to add to the zip"
  )

  args = parser.parse_args()

  # output exist + overwrite check
  output = os.path.normpath(args.o)
  if os.path.isfile(output):
    overwrite = input(f"[<] '{output}' already exists. overwrite? [Y/n] ")
    if overwrite.strip().lower() not in ("y", "yes", ""):
      sys.exit("[>] quitting.")

  # file dedupe + validation
  files = {os.path.basename(f): os.path.realpath(f) for f in args.f}
  for f in files.values():
    if not (f.endswith(".dylib") or f.endswith(".deb")):
      sys.exit(f"[!] '{f}' is not a deb or dylib")

    if not os.path.isfile(f):
      sys.exit(f"[!] '{f}' does not exist or is not a file")

  print("[*] generating..")
  with TemporaryDirectory() as tmpdir:
    for deb in list(files.values()):
      if not deb.endswith(".deb"):
        continue

      helpers.extract_deb(deb, tmpdir, files)

    with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=4) as zf:
      for name, path in files.items():
        if os.path.isfile(path):
          zf.write(path, name)
        else:
          if path.endswith("/"):
            path = path[:-1]  # yes this is needed to prevent a bug 😭

          for dp, _, files in os.walk(path):
            for f2 in files:
              thing = f"{dp}/{f2}"
              zf.write(
                thing,
                os.path.relpath(thing, os.path.dirname(path))
              )  # no, i don't know what this is doing.


if __name__ == "__main__":
  main()

