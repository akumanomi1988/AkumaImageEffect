# Akuma Image Effect 🖼️➡🎥

**Professional framework for transforming images into videos with dynamic effects**

---

## Features ✨

- 🎨 **Dynamic Effects**: Apply zoom, fade, and custom transformations to images.
- 🌐 **Multi-Source Support**: Load images from local files or remote URLs.
- 🛠️ **Extensible System**: Easily register custom effects.
- 🎥 **Video Generation**: Create MP4 videos with configurable duration and FPS.
- 🧩 **Professional Configuration**: Fine-tune quality, interpolation, and background colors.

---

## Installation 📦

```bash
pip install akumaimageeffect
```

---

## Quick Start 🚀

```python
from akuma import AkumaEngine

# Initialize the engine
engine = AkumaEngine()

# Generate a video with zoom-in effect
engine.generate_video(
    image_src="input.jpg",
    effect="akuma_zoom_in",
    duration=3.0,
    output_path="output.mp4"
)
```

---

## Available Effects 🎨

| Effect Name       | Description                          | Key Parameters           |
|-------------------|--------------------------------------|--------------------------|
| `akuma_zoom_in`   | Smooth centered zoom effect          | `interpolation`          |
| `akuma_zoom_out`  | Progressive reduction with background | `background_color`       |

---

## Register Custom Effects 🛠️

```python
from akuma import AkumaEngine, EffectConfig

@AkumaEngine.register_effect("custom_effect")
def custom_effect(image: np.ndarray, progress: float, config: EffectConfig) -> np.ndarray:
    """
    Custom effect logic
    
    Args:
        image: Input image (numpy array)
        progress: Animation progress (0.0 to 1.0)
        config: Effect configuration
        
    Returns:
        Transformed image
    """
    # Your transformation logic here
    return transformed_image
```

---

## Advanced Configuration ⚙️

```python
from akuma import EffectConfig

# Custom configuration
config = EffectConfig(
    output_quality=18,            # Video quality (0-51, lower is better)
    interpolation=cv2.INTER_CUBIC,  # Interpolation method
    background_color=(255, 255, 255)  # Background color (BGR format)
)

# Initialize engine with custom config
engine = AkumaEngine(config)
```

---

## System Requirements 💻

- **Python**: 3.10+
- **FFmpeg**: Required for video processing
- **Dependencies**:
  - OpenCV (`opencv-python`)
  - NumPy (`numpy`)
  - Requests (`requests`)

---

## Contributing 🤝

1. Fork the repository.
2. Add new effects in the `akuma/effects/` directory.
3. Submit a pull request with a clear description of your changes.

---

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Example Use Cases 🌟

- **Social Media Content**: Create engaging intros/outros for videos.
- **Presentations**: Add dynamic effects to slides.
- **E-Learning**: Enhance educational materials with animated visuals.

---

## Support 🆘

For issues or feature requests, please open an issue on the [GitHub repository](https://github.com/akumanomi1988/AkumaImageEffect).

---

**Akuma Image Effect**: Where images come to life! 🎬✨