"""Build the standalone skill ZIP from this repository using Python stdlib."""

from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/icon.svg",
    "references/cas-editoriaux.md",
    "CITATION.cff",
    "LICENSE",
)


def build():
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    archive = output / f"humanizer-linkedin-v{VERSION}.zip"
    for relative in FILES:
        if not (ROOT / relative).is_file():
            raise FileNotFoundError(relative)
    with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as bundle:
        for relative in FILES:
            info = ZipInfo(f"humanizer-linkedin/{relative}", (2026, 10, 31, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, (ROOT / relative).read_bytes(), compresslevel=9)
    digest = sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(".zip.sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"Built {archive.name} ({archive.stat().st_size} bytes)")
    print(f"SHA-256: {digest}")
    return archive


if __name__ == "__main__":
    build()
