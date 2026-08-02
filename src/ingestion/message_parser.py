import re
def extract_download_url(body):
    match = re.search(
        r'href="(https://reports\.example\.com[^"]+)"',
        body,
    )

    if match:
        return match.group(1)

    return None
def identify_city(subject):
    if subject == "UbiVu | City of Rio Rancho NM | Rio Rancho Nightly":
        return "Rio Rancho"
    elif subject == "UbiVu | City of Santa Fe New Mexico | Santa Fe Nodes":
        return "Santa Fe"
    elif subject == "UbiVu | City of Belen, NM | Belen Nightly":
        return "Belen"

    return ""