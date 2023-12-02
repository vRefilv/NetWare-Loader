import os, requests, zipfile, shutil
from pystyle import Colors, Colorate, Write
from refilmodules import center_text,slowType
color = Colors.purple_to_blue


def download_and_extract_latest_release(repo_url, destination_folder):
    # Gets link for latest release
    latest_release_url = f"{repo_url}/releases/latest"
    response = requests.get(latest_release_url)
    latest_release_tag = response.url.split("/")[-1]

    # Makes link to NetWare.zip download
    release_zip_url = f"{repo_url}/releases/download/{latest_release_tag}/NetWare.zip"

    slowType(center_text("Downloading: " + release_zip_url))

    # Download NetWare.zip
    zip_response = requests.get(release_zip_url)

    # Save NetWare.zip to destination_folder
    zip_path = os.path.join(destination_folder, "NetWare.zip")
    with open(zip_path, "wb") as zip_file:
        zip_file.write(zip_response.content)

    # Unpack NetWare.zip to destination folder
    temp_folder = os.path.join(destination_folder, "temp_extract")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_folder)

    # Move the contents of "NetWare" folder to the destination folder
    netware_source = os.path.join(temp_folder, "NetWare")
    for item in os.listdir(netware_source):
        s = os.path.join(netware_source, item)
        d = os.path.join(destination_folder, item)
        shutil.move(s, d)

    # Remove the temporary folder
    shutil.rmtree(temp_folder)

    # Deletes NetWare.zip file
    os.remove(zip_path)
    inject_cmd = os.path.join(destination_folder, "inject.cmd")
    os.remove(inject_cmd)

    # Save release version to version.txt file
    version_file_path = os.path.join(destination_folder, "version.txt")
    with open(version_file_path, "w") as version_file:
        version_file.write(latest_release_tag)


def get_current_version(destination_folder):
    version_file_path = os.path.join(destination_folder, "version.txt")
    try:
        with open(version_file_path, "r") as version_file:
            current_version = version_file.read().strip()
        return current_version
    except FileNotFoundError:
        return None

def check_for_update(repo_url, destination_folder):
    slowType(center_text("Checking for updates"))

    # Ensure the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        slowType(center_text(f"Created folder: {destination_folder}"))

    # Get the current installed version
    current_version = get_current_version(destination_folder)

    # Get the latest release version from GitHub
    latest_release_url = f"{repo_url}/releases/latest"
    response = requests.get(latest_release_url)
    latest_release_tag = response.url.split("/")[-1]

    if current_version is None:
        slowType(center_text(f"No version file found, Downloading the latest release."))
        # Perform the update
        download_and_extract_latest_release(repo_url, destination_folder)
    elif current_version is latest_release_tag > current_version:
        slowType(center_text(f"Updating from version {current_version} to version {latest_release_tag}"))
        # Perform the update
        download_and_extract_latest_release(repo_url, destination_folder)
    else:
        slowType(center_text("Already up to date."))
