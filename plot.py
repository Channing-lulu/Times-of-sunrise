# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

"""
Read the SRS file in data/, draw sunrise & sunset for the month, save to out/.

    uv run plot.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt

FILE = "hko-sunrise-sunset-2024-09.json"    # same name as in fetch.py
PICTURE = "sunrise-sunset-2024-09.png"

HERE = Path(__file__).parent
DATA = HERE / "data" / FILE
OUT = HERE / "out"


def rows(path):
    """The SRS JSON as a list of rows, one per day."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    return raw["data"]


def to_hours(hhmm):
    """'06:05' -> 6.083, so it can go on a numeric axis."""
    hh, mm = hhmm.split(":")
    return int(hh) + int(mm) / 60


def main():
    table = rows(DATA)
    print(f"{DATA.name}: {len(table)} rows. The first one: {table[0]}")

    days, sunrises, sunsets = [], [], []
    for i, (year, month, day, sunrise, transit, sunset) in enumerate(table):
        days.append(i + 1)
        sunrises.append(to_hours(sunrise))
        sunsets.append(to_hours(sunset))

    print(f"{len(days)} days, "
          f"sunrise {min(sunrises):.2f}-{max(sunrises):.2f}, "
          f"sunset {min(sunsets):.2f}-{max(sunsets):.2f}")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(days, sunrises, color="#d6591d", linewidth=1.5, label="Sunrise")
    ax.plot(days, sunsets, color="#1d6fd6", linewidth=1.5, label="Sunset")
    ax.set_xlabel("day of September 2024")
    ax.set_ylabel("time of day (hours)")
    ax.set_title("Hong Kong Observatory — sunrise & sunset, September 2024")
    ax.legend()
    fig.tight_layout()

    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / PICTURE, dpi=150)
    print(f"saved out/{PICTURE}")
    plt.show()


if __name__ == "__main__":
    main()