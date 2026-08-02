from ingestion.message_parser import identify_city, extract_download_url


def main():
    subject = "UbiVu | City of Santa Fe New Mexico | Santa Fe Nodes"
    body = '<a href="https://reports.example.com/sample-report.csv">Download</a>'

    city = identify_city(subject)
    download_url = extract_download_url(body)

    print(city)
    print(download_url)


if __name__ == "__main__":
    main()