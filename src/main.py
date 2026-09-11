from ingestion.file_naming import build_report_filename
from ingestion.message_parser import identify_city, extract_download_url
from ingestion.google_drive import (
    create_drive_service,
    find_root_folder,
    find_city_folder,
)

def main():
    subject = "UbiVu | City of Santa Fe New Mexico | Santa Fe Nodes"
    body = '<a href="https://reports.example.com/sample-report.csv">Download</a>'

    city = identify_city(subject)
    download_url = extract_download_url(body)

    if download_url and city != "":
        report_filename = build_report_filename(city)

        service = create_drive_service()
        root_folder = find_root_folder(service)

        if root_folder is None:
            return

        city_folder = find_city_folder(
            service,
            root_folder["id"],
            city,
        )

        if city_folder is None:
            return

        print(city)
        print(download_url)
        print(report_filename)

if __name__ == "__main__":
    main()
