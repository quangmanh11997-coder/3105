import plistlib
from pathlib import Path

INPUT_FILE = "V50-BIGUPDATE.3105"
OUTPUT_FILE = "V50_AIM_FINAL.3105"

raw = Path(INPUT_FILE).read_bytes()
print("Kích thước gốc:", len(raw), "bytes | Header:", raw[:16])

header = b"3105PATCH " if raw.startswith(b"3105PATCH ") else b""
payload = raw[len(header):]

try:
    plist_data = plistlib.loads(payload)
    plist_data["aimConfig"] = {
        "AimEnabled": True,
        "smoothness": 0.35,
        "fov_radius": 160,
        "draw_modes": {"DrawMode1": True, "DrawMode2": True, "DrawMode3": True},
        "targets": {"nearest": 1, "lowest_hp": 2}
    }
    out_bytes = header + plistlib.dumps(plist_data, fmt=plistlib.FMT_BINARY)
    Path(OUTPUT_FILE).write_bytes(out_bytes)
    print(f"Ghép thành công (bplist): {OUTPUT_FILE} ({len(out_bytes)} bytes)")
except Exception as e:
    print("Cấu trúc file gốc không phải bplist thuần:", e)
    raise
