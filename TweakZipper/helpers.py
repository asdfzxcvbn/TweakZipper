import os
import sys
import platform
import subprocess
from glob import glob
from uuid import uuid4


# yep, this is stolen from cyan
def extract_deb(deb: str, tmpdir: str, files: dict[str, str]) -> None:
  t2 = f"{tmpdir}/{uuid4()}"
  os.mkdir(t2)

  if platform.system() == "Linux":
    tool = ["ar", "-x", deb, f"--output={t2}"]
  else:
    tool = ["tar", "-xf", deb, f"--directory={t2}"]

  try:
    subprocess.run(tool, check=True)
  except Exception:
    sys.exit(f"[!] couldn't extract {os.path.basename(deb)}")

  # it's not always "data.tar.gz"
  data_tar = glob(f"{t2}/data.*")[0]
  subprocess.run(["tar", "-xf", data_tar, f"--directory={t2}"])

  for hi in sum((
      glob(f"{t2}/**/*.dylib", recursive=True),
      glob(f"{t2}/**/*.bundle", recursive=True),
      glob(f"{t2}/**/*.framework", recursive=True)
  ), []):  # type: ignore
    if (
        os.path.islink(hi)  # symlinks are broken iirc
        or hi.count(".bundle") > 1  # prevent sub-bundle detection (rip)
        or hi.count(".framework") > 1
    ):
      continue

    files[os.path.basename(hi)] = hi

  print(f"[*] extracted {os.path.basename(deb)}")
  del files[os.path.basename(deb)]

