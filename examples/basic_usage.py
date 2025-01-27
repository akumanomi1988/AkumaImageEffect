from akuma import AkumaEngine, EffectConfig

# Configuración profesional
config = EffectConfig(
    background_color=(255, 255, 255),  # Fondo blanco
    interpolation=cv2.INTER_CUBIC
)

# Procesamiento de video
engine = AkumaEngine(config)
engine.generate_video(
    image_src="input.jpg",
    effect="akuma_zoom_in",
    duration=4.0,
    output_path="presentation_intro.mp4",
    fps=60
)

print("Video generado exitosamente")