import plistlib
from pathlib import Path

INPUT_FILE = "V50-BIGUPDATE.3105"
OUTPUT_FILE = "V50_AIM_FINAL.3105"

raw = Path(INPUT_FILE).read_bytes()
header = b"3105PATCH\x00"
if not raw.startswith(header):
    raise ValueError(f"Header không khớp: {raw[:16]}")

plist_data = plistlib.loads(raw[len(header):])
print("Các khóa trong file gốc:", list(plist_data.keys()))

plist_data["aimConfig"] = {
    "AimEnabled": True,
    "smoothness": 0.35,
    "fov_radius": 160,
    "draw_modes": {"DrawMode1": True, "DrawMode2": True, "DrawMode3": True},
    "targets": {"nearest": 1, "lowest_hp": 2}
}

out_bytes = header + plistlib.dumps(plist_data, fmt=plistlib.FMT_BINARY)
Path(OUTPUT_FILE).write_bytes(out_bytes)
print(f"Ghép thành công: {OUTPUT_FILE} ({len(out_bytes)} bytes)")
