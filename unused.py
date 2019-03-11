# coding=utf-8
import glob
import os
import re
import locale
import string

locale.setlocale(locale.LC_ALL,'zh_CN.UTF-8')

# brew install the_silver_searcher

def get_all_image(path):
    all_image = []
    for index in range(0, 20):
        path_name = path + '*/' * index + '*.imageset'
        images = glob.glob(path_name)
        if len(images) == 0:
            continue
        all_image.extend(images)
    return all_image

def is_unused(path, image_name):
    command = 'ag --ignore-dir "Images.xcassets" "%s" %s' % (image_name, path)
    try:
        result = os.popen(command).read()
    except UnicodeDecodeError:
        print("except:" + image_name)
        return False

    return result == ''

def deal_image(path, project_name):
    images = get_all_image(path + project_name + "/")
    all_image_names = [os.path.basename(pic)[:-9] for pic in images]

    # 不确信是否使用
    not_sure_unused = []
    unused_images = []
    for index in range(0, len(images)):
        image_name = all_image_names[index]
        if is_ignore(image_name):
            continue

        # 移除末尾的数字
        new_image_name = image_name.rstrip(string.digits)
        if is_unused(path, new_image_name):
            # 末尾是数字 则不确信是否在使用中
            if image_name != new_image_name:
                not_sure_unused.append(image_name)
            else:
                image_path = images[index]
                os.system('rm -rf "%s"' % (image_path))
                unused_images.append(image_name)

    return (all_image_names, not_sure_unused, unused_images)


ignores = {r''}
def is_ignore(str):
    for ignore in ignores:
        if re.match(ignore, str):
            return True
    return False

if __name__ == '__main__':
    # path = "/Volumes/data/workspaces/公司/cargod/"
    # (all_images, not_sure_unused, unused_images) = deal_image(path, "CarGod")

    path = "/Volumes/data/workspaces/公司/iOS-省心宝汽车/ios/"
    (all_images, not_sure_unused, unused_images) = deal_image(path, "sxbCar")

    print("-------------所有-------------")
    print(len(all_images), all_images)
    print("-------------已删除-------------")
    print(unused_images)
    print("-------------可能在使用中-------------")
    print(not_sure_unused)

