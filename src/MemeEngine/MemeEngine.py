from PIL import Image, ImageDraw, ImageFont
import random
import os

class MemeEngine:
    def __init__(self, output_dir:str='./tmp') -> None:
        self.outdir = output_dir        
    
    def make_meme(self, img_path, text, author, width=500) -> str:
        """Insert quotes into the image, resize & return the output image path."""
        
        # Sep 1: Load the input image from disk
        with Image.open(img_path) as img:
            # Step 2: Transform image by resizing to a maximum width of 500px 
            # while maintaining the input aspect ratio (float)
            ratio = img.width / img.height      # float
            height =  int(width / ratio)        # int
            img = img.resize((width, height))
            
            # Step 3: Draw a quote into the resized image
            
            # Step 3.1: Get font
            fnt = ImageFont.truetype('MemeEngine/fonts/LilitaOne-Regular.ttf', size=20)
            
            # Step 3.1: Get a drawing context
            draw = ImageDraw.Draw(img)
            
            # Step 3.2: Draw quote
            x_text = random.randint(5, width // 2)
            y_text = random.randint(5, height - height // 10)
            
            # Draw meme text
            draw.text((x_text, y_text), text, fill='black', 
                        font=fnt, align='left')
            
            # Draw author text
            draw.text((x_text + 20, y_text + 30), f'- {author}', fill='white', 
                        font=fnt, align='center')            

            # Step 4: Saving the meme
            new_img_name = f'meme_{os.path.basename(img_path)}'
            new_path = MemeEngine.build_img_path(self.outdir, 
                                                 new_img_name)
            img.save(new_path)
            return new_path
    
    @staticmethod
    def build_img_path(dir:str, img_name:str) -> str:
        """Create directory & return image path."""
        if not os.path.isdir(dir):
            os.mkdir(dir)           
        return os.path.join(dir, img_name)
