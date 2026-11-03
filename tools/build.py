"""data/죄명표.txt 를 tools/template.html 에 넣어 index.html 을 만든다.

사용법:  python3 tools/build.py
"""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
data = (root / "data" / "죄명표.txt").read_text(encoding="utf-8").strip()
assert "`" not in data and "${" not in data
tpl = (root / "tools" / "template.html").read_text(encoding="utf-8")
out = tpl.replace("/*DATA*/", data)
(root / "index.html").write_text(out, encoding="utf-8")
print(f"index.html {len(out.encode()):,} bytes")
