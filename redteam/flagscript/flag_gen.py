from flag_conf import dirs, fnames, alpha, alpha_num, all_chrs, fake_flags, fake_prefixes
import random as r
import os


debug = False


def main():
    print('For generating directories, use:\n1: dirs\n2: random')
    dir_choice = input('> ')
    if dir_choice == '2':
        max_depth = int(input('Max depth: '))
    print('For generating filenames, use:\n1: fnames\n2: alpha\n3: alpha_num\n4: random')
    fname_choice = input('> ')
    if fname_choice != '1':
        fname_len = int(input('Filename length: '))
    num = int(input('Number to generate: '))
    i = 0
    while i < num:
        # get the path
        try:
            if dir_choice == '1':
                path = r.choice(dirs)
            elif dir_choice == '2':
                path = '/'
                for _ in range(max_depth):
                    folders = [os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
                    if len(folders) > 0:
                        path = r.choice(folders)
                    else:
                        break
        except Exception as e:
            if debug:
                print(f'ERROR generating path "{path}" failed ({e})')
            continue
        # get the fname
        if fname_choice == '1':
            fname = r.choice(fnames)
        else:
            charset = {'2': alpha, '3': alpha_num, '4': all_chrs}[fname_choice]
            fname = ''.join([r.choice(charset) for _ in range(fname_len)])
        # get the flag content and write
        try:
            with open(os.path.join(path, fname), 'w') as f:
                flag = r.choice(fake_prefixes) + '{' + r.choice(fake_flags) + '}'
                if debug:
                    print(f'Writing "{flag}" to {os.path.join(path, fname)}')
                f.write(flag)
                i += 1
        except Exception as e:
            if debug:
                print(f'ERROR writing "{flag}" to {os.path.join(path, fname)} failed with error {e}')

if __name__ == '__main__':
    main()

