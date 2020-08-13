import os
from devtools.constants import file_fix_dict

templates_dir = '../templates/'
to_change_dict = file_fix_dict


def check_file(data):
    data: str
    q = 0
    for c in to_change_dict:
        q += data.count(c)

    return q


def fix_file(data):
    data: str
    for c in to_change_dict:
        data = data.replace(c, to_change_dict[c])
    return data


def check_files():
    templates = os.listdir(templates_dir)
    print('templates directory {t_dir}, templates list: \r\n {t_list}'
          .format(t_dir=templates_dir, t_list=templates))
    for template in templates:
        path = os.path.join(templates_dir, template)
        if not os.path.isfile(path):
            continue

        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
            q = check_file(data)
            print('file {file}, errors: {q}'
                  .format(file=template, q=q))


def fix_files():
    templates = os.listdir(templates_dir)

    for template in templates:
        path = os.path.join(templates_dir, template)
        if not os.path.isfile(path):
            continue

        f = open(path, 'r', encoding='utf-8')
        data = f.read()
        q = check_file(data)
        f.close()

        if q != 0:
            f = open(path, 'w', encoding='utf-8')
            f.write(fix_file(data))
            f.close()

    check_files()


if __name__ == '__main__':
    fix_files()
