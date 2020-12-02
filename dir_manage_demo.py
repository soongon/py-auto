# 매일 아침 images 디렉토리의 png 파일을 검색하여 날짜 디렉토리에 이동시킨다.
import glob
import os
import shutil


def main():
    os.chdir('/Users/soongonkim/PycharmProjects/py-auto/images')
    png_list = glob.glob('*.png')
    print(png_list)
    os.mkdir('./1202')
    print('./1202 디렉토리 생성 완료')

    for png in png_list:
        shutil.move(png, './1202')
        print(png + ' file moved ok..')

    print('job completed..')


if __name__ == '__main__':
    main()
