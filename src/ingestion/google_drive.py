from googleapiclient.discovery import build

from ingestion.google_auth import authenticate


def create_drive_service():
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)
    return service

def find_root_folder(service):
    query = (
        "name = 'Ubivu Ubicquia' "
        "and mimeType = 'application/vnd.google-apps.folder' "
        "and trashed = false"
    )

    results = service.files().list(
        q=query,
        spaces="drive",
        fields="files(id, name)",
    ).execute()

    folders = results.get("files", [])

    if not folders:
        print("Error: Root folder 'Ubivu Ubicquia' not found in My Drive.")
        return None

    return folders[0]

def find_city_folder(service, root_folder_id, city_name):
    query = (
        f"name = '{city_name}' "
        "and mimeType = 'application/vnd.google-apps.folder' "
        f"and '{root_folder_id}' in parents "
        "and trashed = false"
    )

    results = service.files().list(
        q=query,
        spaces="drive",
        fields="files(id, name)",
    ).execute()

    folders = results.get("files", [])

    if not folders:
        print(f"Warning: Subfolder '{city_name}' not found under Ubivu Ubicquia.")
        return None

    return folders[0]