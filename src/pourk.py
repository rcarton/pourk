#!/usr/bin/python

import sys, os, Image

# Default patchwork color
DEFAULT_COLOR = '#000000'
DEFAULT_SIZE = (1680, 1050)
DEFAULT_MODE = 'RGBA'
DEFAULT_COUTURIER = 'couturiers.default.LeColumnCouturier'

class Patchwork(object):
    
    def __init__(self, outfile, image_list=None, size=DEFAULT_SIZE, mode=DEFAULT_MODE, color=DEFAULT_COLOR):
        self.color = color
        self.size = size
        self.mode = mode
        self.outfile = outfile
        self.image_list = image_list or []
        self.image = self.create_image()
    
    def create_image(self):
        return Image.new(self.mode, self.size, self.color)
    
    def make_patchwork(self, couturier, options={}):
        couturier_class = couturier_import(couturier)
        couturier_instance = couturier_class(image_list=self.image_list)
        couturier_instance.sew(self.image)
        self.save() 
    
    def save(self):
        with open(self.outfile, 'wb') as f:
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

def usage():
    """Prints the usage."""
    
    print """
Usage:
    pourk.py "out file" "image1" "image2" ..
"""






def hoink(outfile, image_list=None, size=None, mode=None, color=None, couturier=None, options={}):
    """Makes the patchwork!"""
    
    size = size or DEFAULT_SIZE
    mode = mode or DEFAULT_MODE
    color = color or DEFAULT_COLOR
    couturier = couturier or DEFAULT_COUTURIER
    
    p = Patchwork(outfile, image_list=image_list, size=DEFAULT_SIZE)
    p.make_patchwork(couturier, options)
    
    


if __name__ == '__main__':
    # TODO: parse for real with optparse
    outfile = sys.argv[1]
    images = sys.argv[2:]
    
    if len(sys.argv) < 3:
        usage()
        exit(1)
    
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
    
    
    hoink(outfile, image_list=images, size=DEFAULT_SIZE)
    exit(0)
    
