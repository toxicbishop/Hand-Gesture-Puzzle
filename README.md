# Hand Gesture Puzzle

[![CodeQL](https://github.com/toxicbishop/hand-gesture-puzzle/actions/workflows/codeql.yml/badge.svg)](https://github.com/toxicbishop/hand-gesture-puzzle/actions/workflows/codeql.yml)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

A real-time computer vision puzzle game where you build and solve a sliding image puzzle using **hand gestures instead of a mouse or touchscreen**.

Built with **OpenCV** and **MediaPipe**, it tracks your hands live through a webcam and drives the entire game loop — frame selection, capture, tile dragging, and reset — off gesture input alone.

## Features

- Real-time hand tracking (MediaPipe, lite model for low-latency inference)
- Two-hand frame selection — mark opposite corners with both index fingers to choose your puzzle area
- Pinch gesture to capture the selected region
- Three difficulty levels — 3x3, 4x4, 5x5 (switch anytime with the `1` / `2` / `3` keys)
- Drag-and-drop tile solving via pinch-and-hold gestures
- Smoothed pointer tracking (exponential moving average) so dragging doesn't feel jittery
- Shuffle animation before each puzzle starts
- Live timer with persistent best-time tracking per difficulty (saved to `scores.json`)
- Open-palm hold gesture to reset back to camera/frame-selection mode
- Fully playable without touching the keyboard or mouse once running

---

## Tech Stack

- **Python**
- **OpenCV** – video capture, rendering, and image processing
- **MediaPipe** – hand landmark detection and gesture tracking

---

## How to Run

```bash
git clone https://github.com/toxicbishop/hand-gesture-puzzle.git
cd hand-gesture-puzzle
pip install -r requirements.txt
python main.py
```

**Controls**

| Action | Gesture / Key |
|---|---|
| Select puzzle area | Hold up both hands, mark corners with index fingers |
| Capture image | Pinch (thumb + index finger) |
| Drag a tile | Pinch on a tile, move, release over another tile |
| Change difficulty | `1` (3x3) / `2` (4x4) / `3` (5x5), while in camera mode |
| Reset to camera mode | Hold an open palm for ~1.5s |
| Quit | `Q` or `Esc` |

---

## How It Works

1. OpenCV captures live video from your webcam.
2. MediaPipe detects hand landmarks every frame (throttled to every other frame to keep the render loop responsive).
3. In camera mode, both index fingers define a selection box; a pinch captures that region.
4. The captured image is sliced into an N×N grid and shuffled.
5. In puzzle mode, pinch-drag gestures swap tiles until the grid matches the solved order.
6. Solve time is tracked live and compared against your saved best for that difficulty.

---

## Troubleshooting: laggy video on a USB webcam

If the feed feels delayed relative to your actual hand movement, check the console output on startup — it prints the resolution, FPS, and codec your camera actually granted:

```
Camera granted: 1280x720 @ 30fps, fourcc=YUY2
```

If `fourcc` isn't `MJPG`, your camera is falling back to uncompressed video. Uncompressed 1280x720@30fps is roughly 440 Mbps, which exceeds USB 2.0's real-world throughput (~280–320 Mbps) — the resulting frame drops happen at the driver level, before Python ever sees them, and no amount of code-side optimization fixes it. `main.py` detects this automatically and falls back to 640x480, which fits comfortably within USB 2.0 bandwidth. The window auto-sizes to match whatever resolution the camera ends up at, so there's no stretching either way.

---

## Future Improvements

- Web-based version (no local install required)
- Multiplayer / competition mode
- On-screen gesture legend for first-time users

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
