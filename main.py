# main.py
"""
Main script to generate a video with custom effects
using AkumaEngine.
"""

import cv2
from effect_engine import AkumaEngine, EffectConfig
import effects.core_effects  # Automatically imports and registers effects

def main():
    """Main function to generate a video with effects."""
    # Professional engine configuration
    config = EffectConfig(
        background_color=(255, 255, 255),  # White background
        interpolation=cv2.INTER_CUBIC  # High-quality interpolation
    )

    # Initialize the engine with the given configuration
    engine = AkumaEngine(config)

    # Video parameters
    image_src = "test.jpg"  # Path to the input image
    output_path = "presentation_intro.mp4"  # Path for the output video
    effect = "akuma_zoom_out"  # Effect to be applied
    duration = 5.0  # Duration of the video in seconds
    fps = 60  # Frames per second

    # Generate the video
    try:
        engine.generate_video(
            image_src=image_src,
            effect=effect,
            duration=duration,
            output_path=output_path,
            fps=fps
        )
        print(f"Video successfully generated: {output_path}")
    except Exception as e:
        print(f"Error generating video: {e}")

if __name__ == "__main__":
    main()
