# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

"""
Read the SRS file in data/, draw hours of daylight across the month,
and mark the autumn equinox. Save the picture to out/.

    uv run plot.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt

FILE = "hko-sunrise-sunset-2024-09.json"      # same name as in fetch.py
PICTURE = "daylight-2024-09.png"

HERE = Path(__file__).parent
DATA = HERE / "data" / FILE
OUT = HERE / "out"

EQUINOX = 22          # 2024 autumn equinox falls on 22 September


def rows(path):
    """The SRS JSON as a list of rows, one per day."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    return raw["data"]


def to_hours(hhmm):
    """'06:06' -> 6.1, so it can go on a numeric axis."""
    hh, mm = hhmm.split(":")
    return int(hh) + int(mm) / 60


def main():
    table = rows(DATA)
    print(f"{DATA.name}: {len(table)} rows. The first one: {table[0]}")

    days, sunrises, sunsets, daylight = [], [], [], []
    for i, (date, sunrise, transit, sunset) in enumerate(table):
        r = to_hours(sunrise)
        s = to_hours(sunset)
        days.append(i + 1)
        sunrises.append(r)
        sunsets.append(s)
        daylight.append(s - r)                # the number this plot is about

    print(f"{len(days)} days, daylight "
          f"{min(daylight):.2f}-{max(daylight):.2f} hours")
    print(f"on the equinox (day {EQUINOX}): {daylight[EQUINOX - 1]:.2f} hours")

    fig, ax = plt.subplots(figsize=(10, 4))

    # the curve: hours of daylight across the month
    ax.plot(days, daylight, color="#d6591d", linewidth=2, marker="o",
            markersize=3, label="Hours of daylight")

    # the equinox: the moment day and night are equal
    ax.axhline(12, color="grey", linestyle="--", linewidth=1)
    ax.axvline(EQUINOX, color="grey", linestyle=":", linewidth=1)
    ax.annotate("autumn equinox\n22 Sep",
                xy=(EQUINOX, 12), xytext=(EQUINOX + 2, 12.15),
                fontsize=9, color="grey")

    ax.set_xlabel("day of September 2024")
    ax.set_ylabel("hours of daylight")
    ax.set_title("Hong Kong Observatory — daylight shrinking after the equinox")
    ax.legend(loc="lower left")
    fig.tight_layout()

    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / PICTURE, dpi=150)
    print(f"saved out/{PICTURE}")
    plt.show()


if __name__ == "__main__":
    main()