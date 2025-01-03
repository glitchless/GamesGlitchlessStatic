import distutils.dir_util
import zipfile
import urllib.request
import os
import shutil

client_download_url = "https://f003.backblazeb2.com/file/lionzxy-static-files/nomi-1.7.3.zip"
unzipped_modpack_folder = "out/nomi/"
resources_folder = "resources/"

def prepare_nomi():
    download_path = "tmp/nomi.zip"
    if os.path.exists(unzipped_modpack_folder):
        print("NOMI already unzipped")
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


def remove_unsupported():
    os.remove(unzipped_modpack_folder + "mods/Avaritia-1.12.2-3.3.0.37-universal.jar")
    # os.remove(unzipped_modpack_folder + "mods/notenoughIDs-1.5.3.jar")
    # os.remove(unzipped_modpack_folder + "mods/hydroenergy-1.1.1.jar")


def main():
    prepare_nomi()
    remove_unsupported()
    append_resources()


if __name__ == '__main__':
    main()
