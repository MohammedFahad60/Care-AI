import base64
import io
from PIL import Image

class MedicalImageEncoder:
    """
    Preprocessing pipeline for Medical Imaging (X-Ray / Dermatology).
    Prepares images for Gemini 1.5 Vision or ResNet-50.
    """

    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size

    def process_base64(self, base64_string):
        """Decodes and resizes image for tensor input"""
        try:
            if "," in base64_string:
                base64_string = base64_string.split(",")[1]
            
            image_data = base64.b64decode(base64_string)
            image = Image.open(io.BytesIO(image_data))
            
            # Resize for Neural Network standard input
            image = image.resize(self.target_size)
            
            if image.mode != 'RGB':
                image = image.convert('RGB')
                
            return image
        except Exception as e:
            print(f"❌ Image Encoding Error: {e}")
            return None

    def get_image_embeddings(self, image):
        """
        Placeholder for Vector Embeddings generation.
        """
        return "tensor<1x1024 float32>"