import os
import sys
import shutil
import argparse
import tempfile

from PIL import Image


name_size = {  # width, hight
    'icon_512x512@2x.png': (1024, 1024),
    'icon_512x512.png': (512, 512),
    'icon_256x256@2x.png': (512, 512),
    'icon_256x256.png': (256, 256),
    'icon_128x128@2x.png': (256, 256),
    'icon_128x128.png': (128, 128),
    'icon_32x32@2x.png': (64, 64),
    'icon_32x32.png': (32, 32),
    'icon_16x16@2x.png': (32, 32),
    'icon_16x16.png': (16, 16),
}


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('src')
    parser.add_argument('--no-clean', default=False, action='store_true')
    args = parser.parse_args(argv)

    tmpdir = tempfile.mkdtemp(dir='./')
    icons_dir = os.path.join(tmpdir, '{}.iconset'.format(args.name))
    icon_file_name = '{}.icns'.format(args.name)
    os.makedirs(icons_dir, exist_ok=True)

    img = Image.open(args.src)
    for name, size in name_size.items():
        resized_img = img.resize(size, Image.ANTIALIAS)
        img_path = os.path.join(icons_dir, name)
        resized_img.save(img_path)
    os.system('iconutil -c icns {}'.format(icons_dir))
    os.rename(os.path.join(tmpdir, icon_file_name), icon_file_name)

    if not args.no_clean:
        shutil.rmtree(tmpdir)

if __name__ == '__main__':
    sys.exit(main())
