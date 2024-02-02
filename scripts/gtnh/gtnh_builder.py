import distutils.dir_util
import zipfile
import urllib.request
import os
import wget
import shutil

client_download_url = "https://downloads.gtnewhorizons.com/ClientPacks/GT_New_Horizons_2.5.1_Client_Java_8.zip"
unzipped_modpack_folder = "out/gtnh/"
resources_folder = "resources/"


def gtnh_download_bar(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))


def prepare_gtnh():
    download_path = "tmp/gtnh.zip"
    if os.path.exists(unzipped_modpack_folder):
        print("GTNH already unzipped")
        return
    if os.path.exists("tmp"):
        shutil.rmtree("tmp")
    os.mkdir("tmp")
    if not os.path.exists(download_path):
        print("Start download %s" % client_download_url)
        wget.download(client_download_url, download_path, bar=gtnh_download_bar)
    print("Start unziping %s" % download_path)
    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall(unzipped_modpack_folder)
    shutil.rmtree("tmp")


def append_resources():
    distutils.dir_util.copy_tree(resources_folder, unzipped_modpack_folder)


def main():
    prepare_gtnh()
    append_resources()


if __name__ == '__main__':
    main()
