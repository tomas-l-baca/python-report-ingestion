from ingestion.message_parser import identify_city


def main():
    subject = "UbiVu | City of Santa Fe New Mexico | Santa Fe Nodes"
    city = identify_city(subject)
    print(city)


if __name__ == "__main__":
    main()