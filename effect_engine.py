import cv2
import numpy as np
import requests
from dataclasses import dataclass
from urllib.parse import urlparse
from pathlib import Path
from typing import Callable, Dict

@dataclass
class EffectConfig:
    """Configuración para procesamiento de efectos"""
    output_quality: int = 23  # 0-51 (lower = mejor calidad)
    interpolation: int = cv2.INTER_LINEAR
    background_color: tuple = (0, 0, 0)  # Formato BGR

class AkumaEngine:
    _effects_registry: Dict[str, Callable] = {}
    
    def __init__(self, config: EffectConfig = EffectConfig()):
        self.config = config

    @classmethod
    def register_effect(cls, effect_name: str) -> Callable:
        """Registra un nuevo efecto en el sistema"""
        def decorator(func: Callable):
            cls._effects_registry[effect_name] = func
            return func
        return decorator

    def generate_video(self, image_src: str, effect: str, 
                      duration: float, output_path: str = "output.mp4", 
                      fps: int = 30) -> None:
        """
        Genera un video aplicando el efecto especificado
        
        Args:
            image_src: URL/Ruta local de la imagen
            effect: Nombre del efecto registrado
            duration: Duración en segundos
            output_path: Ruta de salida
            fps: Cuadros por segundo
        """
        image = self._load_image(image_src)
        effect_func = self._get_effect(effect)
        
        height, width = image.shape[:2]
        total_frames = int(duration * fps)
        
        writer = cv2.VideoWriter(
            output_path,
            cv2.VideoWriter_fourcc(*'mp4v'),
            fps,
            (width, height)
        )
        
        for frame in range(total_frames):
            progress = frame / total_frames
            processed_frame = effect_func(image, progress, self.config)
            writer.write(processed_frame)
            
        writer.release()

    def _load_image(self, source: str) -> np.ndarray:
        """Carga imágenes desde múltiples fuentes"""
        parsed = urlparse(source)
        if parsed.scheme in ('http', 'https'):
            response = requests.get(source)
            image = cv2.imdecode(np.frombuffer(response.content, np.uint8), 
                               cv2.IMREAD_COLOR)
        else:
            if not Path(source).exists():
                raise FileNotFoundError(f"Archivo no encontrado: {source}")
            image = cv2.imread(source)
            
        if image is None:
            raise ValueError("Formato de imagen no soportado")
        return image

    def _get_effect(self, name: str) -> Callable:
        """Recupera un efecto del registro"""
        effect = self._effects_registry.get(name)
        if not effect:
            raise ValueError(f"Efecto '{name}' no registrado")
        return effect