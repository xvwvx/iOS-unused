# -*- coding:utf-8 -*-

import os
import locale

locale.setlocale(locale.LC_ALL,'zh_CN.UTF-8')

def find_all_paths(path, extension):
    command = 'find %s -name "*.%s"' % (path, extension)
    try:
        result = os.popen(command).read()
    except UnicodeDecodeError:
        return []

    return result.split('\n')

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'rt') as file:
        text = file.read()
        replace_text = text.replace(old_text, new_text)

    if text != replace_text:
        with open(file_path, 'w') as file:
            file.write(replace_text)


def replace_module_name(file_path, old_module, new_module, old_class_name, new_class_name = None):
    if new_class_name is None:
        new_class_name = old_class_name
    old_text = 'customClass="%s" customModule="%s" customModuleProvider="target"' % (old_class_name, old_module)
    new_text = 'customClass="%s" customModule="%s"' % (new_class_name, new_module)
    replace_text_in_file(file_path, old_text, new_text)

if __name__ == '__main__':
    is_sxbcar = True

    if is_sxbcar:
        path = "/Volumes/data/workspaces/公司/iOS-省心宝汽车/ios/sxbCar"
        old_module = 'sxbCar'
    else:
        path = "/Volumes/data/workspaces/公司/cargod"
        old_module = 'CarGod'

    new_module = 'XXFramework'

    xib_paths = find_all_paths(path, "xib")
    storyboard_paths = find_all_paths(path, "storyboard")

    all_paths = []
    all_paths.extend(xib_paths)
    all_paths.extend(storyboard_paths)

    for path in all_paths:
        if path != "":
            replace_module_name(path, old_module, new_module, 'XXTextView')
            replace_module_name(path, old_module, new_module, 'XXTextField')
            replace_module_name(path, old_module, new_module, 'XXLabel')
            replace_module_name(path, old_module, new_module, 'XXHairlineConstraint')

            replace_module_name(path, old_module, new_module, 'XXAlignLeftLayout')
            replace_module_name(path, old_module, new_module, 'XXAlignRightLayout')

            replace_module_name(path, old_module, new_module, 'XXExpandCollectionView')
            replace_module_name(path, old_module, new_module, 'XXScrollView')
            replace_module_name(path, old_module, new_module, 'XXAutolayoutView')

            # 替换老版本库
            replace_text_in_file(path, 'customClass="SxbLabel">', 'customClass="XXLabel" customModule="XXFramework">')
            replace_text_in_file(path, 'customClass="SxbTextField">', 'customClass="XXTextField" customModule="XXFramework">')
            replace_text_in_file(path, 'customClass="SxbTextView">', 'customClass="XXTextView" customModule="XXFramework">')
            replace_text_in_file(path, 'property="fd_collapsibleConstraints"', 'property="xx_collapsibleConstraints"')

            replace_text_in_file(path, 'keyPath="regexp_Empty"', 'keyPath="check_emptyMsg"')
            replace_text_in_file(path, 'keyPath="regexp_Rule"', 'keyPath="check_regRule"')
            replace_text_in_file(path, 'keyPath="regexp_Msg"', 'keyPath="check_regMsg"')
            replace_text_in_file(path, 'property="regexp_FrontViews"', 'property="check_frontViews"')