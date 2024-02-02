import distutils.dir_util
import zipfile
import urllib.request
import os
import shutil

# https://downloads.gtnewhorizons.com/ClientPacks/GT_New_Horizons_2.5.1_Client_Java_8.zip
client_download_url = "https://transfer.sh/nNDgzlNrdK/GT_New_Horizons_2.5.1_Client_Java_8.zip"
unzipped_modpack_folder = "out/gtnh/"
resources_folder = "resources/"


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
        urllib.request.urlretrieve(client_download_url, download_path)
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
