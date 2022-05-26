from PIL import Image, ImageFont, ImageDraw

class MemeEngine():
    def __init__(self, out_path: str):
        self.out_path = out_path
    
    def make_meme(self, img_path: str, body: str, author: str, width=500) -> str:
        """Make a meme from the image path and the quote components given

        Arguments:
            img_path {str} -- the file location for the input image.
            body {str} -- the body or text of the quote.
            author {str} -- the author of the quote.
            width {int} -- the width of the image, capped at 500px.
        Returns:
        str -- the file path to the output image.
        """
        width = min(width, 500)
        im = Image.open(img_path)
        im = im.resize((int(width), int(width * (im.height / im.width))), Image.NEAREST)
        font = ImageFont.truetype("./fonts/LilitaOne-Regular.ttf", 100)

        init_length = font.getsize(f'"{body}" - {author}')[0]
        print(font.size)
        new_font_size = int(font.size / (init_length/(im.width * .8)))
        draw = ImageDraw.Draw(im)
        draw.text((int(im.width * 0.1),10), f'"{body}" - {author}', font=ImageFont.truetype("./fonts/LilitaOne-Regular.ttf", new_font_size))
        im.save(f'{self.out_path}/{body.strip(".")}.jpg')
            
        return f'{self.out_path}/{body.strip(".")}.jpg'