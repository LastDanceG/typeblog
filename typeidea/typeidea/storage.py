# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import StringIO

from PIL import Image, ImageDraw, ImageFont


class MyStorage(FileSystemStorage):

    def save(self, name, content, max_length=None):

        # 给图片加水印
        if 'image' in content.content_type:
            image = self.watermark_with_text(content, 'xxx', 'red')
            content = self.convert_image_to_file(image, name)
        return super(MyStorage, self).save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = StringIO()
        image.save(temp, format='PNG')
        return InMemoryUploadedFile(temp, None, name, 'image/png', temp.len, None)

    def watermark_with_text(self, file_obj, text, color, font_family=None):
        image = Image.open(file_obj).convert('RGBA')
        image_water_mark = Image.new('RGBA', image.size, (255,255,255,0))

        draw = ImageDraw.Draw(image_water_mark)
        width, height = image.size
        margin = 10

        if font_family:
            font = ImageFont.truetype(font_family, int(height / 20))
        else:
            font = None
        text_width, text_height = draw.textsize(text, font)
        x = (width - text_width - margin) / 2
        y = height - text_height - margin

        draw.text((x, y), text, color, font)

        return Image.alpha_composite(image, image_water_mark)

