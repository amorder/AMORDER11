#!/usr/bin/env python3
"""Lightweight, platform-safe animated motion-graphics overlays for AMORDER edits."""

from __future__ import annotations

from typing import Final

ACCENT: Final[str] = "0x42C4D8@0.60"
SOFT: Final[str] = "0x42C4D8@0.30"
AMBER: Final[str] = "0xF3A45A@0.62"


def build_motion_graphics_filter(width: int, height: int, duration: float, visual: str) -> str:
    """Build animated vector accents evaluated by FFmpeg at delivery frame rate.

    The Blender render remains the PBR 3D hero image. These deliberately restrained
    overlays provide continuously animated motion-design detail without rendering
    thousands of expensive full-resolution Blender frames.
    """
    w = max(1, int(width))
    h = max(1, int(height))
    key = str(visual).strip().lower()
    filters = [
        # A narrow light sweep and a small moving tracking node, kept away from text.
        f"drawbox=x='mod(t*{max(65, w * 0.09):.3f}\\,W+80)-80':y='{h * .16:.3f}':w=2:h='{h * .22:.3f}':color={SOFT}:t=fill",
        f"drawbox=x='W*0.885+sin(t*1.7)*W*0.018':y='H*0.31+cos(t*1.7)*H*0.055':w=8:h=8:color={ACCENT}:t=fill",
        f"drawbox=x='W*0.10':y='{h * .14:.3f}':w='W*0.80':h=2:color=0xB9D8E3@0.18:t=fill",
    ]

    if key == "timestamp":
        # A moving time marker and a shorter secondary tick.
        filters.extend([
            f"drawbox=x='W*0.13+mod(t*{w * .055:.3f}\\,W*0.72)':y='H*0.25':w=3:h='H*0.18':color={ACCENT}:t=fill",
            f"drawbox=x='W*0.13+mod(t*{w * .055:.3f}\\,W*0.72)-9':y='H*0.25':w=21:h=3:color={AMBER}:t=fill",
        ])
    elif key == "idea":
        # A restrained orbiting focus point around the evidence object.
        filters.append(
            f"drawbox=x='W*0.15+cos(t*1.25)*W*0.045':y='H*0.44+sin(t*1.25)*H*0.035':w=8:h=8:color={ACCENT}:t=fill"
        )
    elif key == "source":
        # Three separate signal nodes travel along a shared connector.
        for offset, y_ratio in ((0.0, .34), (1.25, .40), (2.5, .46)):
            filters.append(
                f"drawbox=x='W*0.12+mod((t+{offset})*{w * .07:.3f}\\,W*0.70)':y='H*{y_ratio:.3f}':w=7:h=7:color={ACCENT}:t=fill"
            )
    elif key == "gaps":
        # Small signal bars pulse independently; the scene's missing block remains the hero.
        for index, x_ratio in enumerate((.13, .16, .19, .22, .25)):
            phase = index * .7
            filters.append(
                f"drawbox=x='W*{x_ratio:.3f}':y='H*0.63-(7+7*(1+sin(t*2.2+{phase:.2f})))':w=4:h='7+7*(1+sin(t*2.2+{phase:.2f}))':color={SOFT}:t=fill"
            )
        filters.append(
            f"drawbox=x='W*0.76':y='H*0.63':w=3:h='H*0.10':color={AMBER}:t=fill"
        )
    elif key == "stand_down":
        # A breathing pair of bracket marks that suggests a controlled pause.
        filters.extend([
            f"drawbox=x='W*0.13':y='H*0.33':w=3:h='H*(0.16+0.015*sin(t*2))':color={ACCENT}:t=fill",
            f"drawbox=x='W*0.13':y='H*0.33':w='W*(0.055+0.006*sin(t*2))':h=3:color={ACCENT}:t=fill",
            f"drawbox=x='W*0.81':y='H*0.33':w=3:h='H*(0.16+0.015*sin(t*2))':color={ACCENT}:t=fill",
            f"drawbox=x='W*0.76':y='H*0.33':w='W*(0.055+0.006*sin(t*2))':h=3:color={ACCENT}:t=fill",
        ])
    elif key == "brand":
        # A subtle orbital point and a counter-moving detail.
        filters.extend([
            f"drawbox=x='W*0.50+cos(t*1.05)*W*0.18':y='H*0.37+sin(t*1.05)*H*0.07':w=9:h=9:color={ACCENT}:t=fill",
            f"drawbox=x='W*0.50+cos(t*1.05+3.14159)*W*0.18':y='H*0.37+sin(t*1.05+3.14159)*H*0.07':w=5:h=5:color={AMBER}:t=fill",
        ])
    else:
        # Generic editorial sweep for any new storyboard visual key.
        filters.append(
            f"drawbox=x='W*0.12+mod(t*{w * .045:.3f}\\,W*0.72)':y='H*0.55':w=9:h=3:color={ACCENT}:t=fill"
        )

    return ",".join(filters)
