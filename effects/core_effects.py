import cv2
import numpy as np
from effect_engine import EffectConfig, AkumaEngine

@AkumaEngine.register_effect("akuma_zoom_in")
def zoom_in_effect(img: np.ndarray, progress: float, config: EffectConfig) -> np.ndarray:
    """Efecto de zoom progresivo centrado"""
    scale = 1 + progress * 0.2  # 1x a 2x
    h, w = img.shape[:2]
    
    new_width = int(w * scale)
    new_height = int(h * scale)
    resized = cv2.resize(img, (new_width, new_height), 
                       interpolation=config.interpolation)
    
    x = (new_width - w) // 2
    y = (new_height - h) // 2
    return resized[y:y+h, x:x+w]

@AkumaEngine.register_effect("akuma_zoom_out")
def zoom_out_effect(img: np.ndarray, progress: float, config: EffectConfig) -> np.ndarray:
    """Efecto de reducción progresiva con fondo personalizado"""
    scale = 1 - progress * 0.2  # 1x a 0.5x
    h, w = img.shape[:2]
    
    resized = cv2.resize(img, (int(w*scale), int(h*scale)), 
                       interpolation=config.interpolation)
    
    frame = np.full((h, w, 3), config.background_color, dtype=np.uint8)
    x = (w - resized.shape[1]) // 2
    y = (h - resized.shape[0]) // 2
    frame[y:y+resized.shape[0], x:x+resized.shape[1]] = resized
    return frame
