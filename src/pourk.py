#!/usr/bin/python

import os, Image

# Default patchwork color
DEFAULT_COLOR = '#000000'
DEFAULT_SIZE = (1680, 1050)
DEFAULT_MODE = 'RGBA'
#DEFAULT_COUTURIER = couturier

class Patchwork(object):
    
    def __init__(self, image_list=None, size=DEFAULT_SIZE, mode=DEFAULT_MODE, color=DEFAULT_COLOR):
        self.color = color
        self.size = size
        self.mode = mode
        self.image_list = image_list or []
        self.image = self.create_image()
    
    def create_image(self):
        return Image.new(self.mode, self.size, self.color)
    
    def make_pourk(self):
        couturier_class = couturier_import('couturiers.default.LeColumnCouturier')
        couturier = couturier_class(image_list=self.image_list)
        couturier.sew(self.image)
        self.save() 
    
    def save(self):
        test = '/home/remi/workspace/pourk/misc/out.jpg'
        with open(test, 'wb') as f:
            self.image.save(f, format='jpeg')


def couturier_import(name):
    """C/P from a Stack overflow answer.
    """
    
    components = name.split('.')
    couturiermod = '.'.join(components[:-1])
    
    mod = __import__(couturiermod)
    for m in components[1:]:
        mod = getattr(mod, m)
    return mod

if __name__ == '__main__':
    print 'HOINK HOINK'
    print """
                                         _
            _   _    __....._     _ '-)-'
           |_\_/ | .'        '.  '-)-'
          /      \/            \-'`
        _| 6 6    `             |
       /..\                     |
       \__/_,          |       /
         '--.___   \    \     \ 
             / /  /`----`;-.   >
            / /  /       / /  /
   jgs     /_/__/       /_/__/
"""
    
    path = '/home/remi/workspace/pourk/misc/images'
    
    
    p = Patchwork([os.path.join(path, i) for i in os.listdir(path)], size=DEFAULT_SIZE)
    p.make_pourk()
    
