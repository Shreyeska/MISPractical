import requests
from bs4 import BeautifulSoup

cookies = {
    '_gid': 'GA1.3.1198343799.1734450784',
    'XSRF-TOKEN': 'eyJpdiI6IlQvOVZJamVkLzlHQ0ZkTFRKSFVTS3c9PSIsInZhbHVlIjoibGFQS0tYenNhcnczRVpFZTE2Sjc4eWE2QjhFekYzaUxnRzNPZWZLZUNBV00wZ2pHNlg5Smx6dEI2YVVBQnpxTytwUS8ySk5DVWc1eUZBRmpJN1psS29JZ3dadnFHcHVONXZxUjVGOVdhQ2Z3SnJIZFJvQXR2VHNTTHFhazM5TEsiLCJtYWMiOiI3MjRmN2QzNTM5ZDk4Mzc0OTVmN2YxZjlhMjJkMDMwNzY0OGQ4ZDM4ZjQwNjRjYWRkZDMzZmNlM2Y4NTM2ODcwIiwidGFnIjoiIn0%3D',
    'kalimati_fruits_and_vegetable_market_development_board_session': 'eyJpdiI6InVhaW5LK0MvcXZvdzhlOTR6N3NDK3c9PSIsInZhbHVlIjoibkp2RWpNa3VjUWNuUk9oMkxDV2pUU01yQ1pHdHF2WitYRzA3YW40ZGU5dUxvbWt2bURvSmVhTFNBWXpwdDFUQjkzc3lmTHlya1RGUVkzRHZMTHVhT0swSmk3dTVMdUhWOGlvb2pNb25rT0FyRlU4R0VuMWVrMTFZVU9jdEZMWHkiLCJtYWMiOiI0YTI5MmNlNDFkMTliMDM1OTQzMjcyNjA3OTVjZjk3ZTA3Y2FhODBhZWJhZmFkZDQ5YjIxNzM3MTg3NWJhNDJhIiwidGFnIjoiIn0%3D',
    '_ga_EMKDTWG87G': 'GS1.1.1734488409.2.1.1734490047.0.0.0',
    '_ga': 'GA1.3.1433230611.1734450784',
    'TawkConnectionTime': '0',
    'twk_uuid_62b413377b967b11799613cd': '%7B%22uuid%22%3A%221.gNHagPN1xcRjbln8PvFc6DgzCMzjwYPneN0XFsHPrra88inRRCOrborx4HKy7w8zOIKC7h24BxBICRpZ6yABCpdX7MrGfyjV0qMiE4MbW6C1KABuF5YpxjICeM1UIU5ut%22%2C%22version%22%3A3%2C%22domain%22%3A%22kalimatimarket.gov.np%22%2C%22ts%22%3A1734490047842%7D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    # 'cookie': '_gid=GA1.3.1198343799.1734450784; XSRF-TOKEN=eyJpdiI6IlQvOVZJamVkLzlHQ0ZkTFRKSFVTS3c9PSIsInZhbHVlIjoibGFQS0tYenNhcnczRVpFZTE2Sjc4eWE2QjhFekYzaUxnRzNPZWZLZUNBV00wZ2pHNlg5Smx6dEI2YVVBQnpxTytwUS8ySk5DVWc1eUZBRmpJN1psS29JZ3dadnFHcHVONXZxUjVGOVdhQ2Z3SnJIZFJvQXR2VHNTTHFhazM5TEsiLCJtYWMiOiI3MjRmN2QzNTM5ZDk4Mzc0OTVmN2YxZjlhMjJkMDMwNzY0OGQ4ZDM4ZjQwNjRjYWRkZDMzZmNlM2Y4NTM2ODcwIiwidGFnIjoiIn0%3D; kalimati_fruits_and_vegetable_market_development_board_session=eyJpdiI6InVhaW5LK0MvcXZvdzhlOTR6N3NDK3c9PSIsInZhbHVlIjoibkp2RWpNa3VjUWNuUk9oMkxDV2pUU01yQ1pHdHF2WitYRzA3YW40ZGU5dUxvbWt2bURvSmVhTFNBWXpwdDFUQjkzc3lmTHlya1RGUVkzRHZMTHVhT0swSmk3dTVMdUhWOGlvb2pNb25rT0FyRlU4R0VuMWVrMTFZVU9jdEZMWHkiLCJtYWMiOiI0YTI5MmNlNDFkMTliMDM1OTQzMjcyNjA3OTVjZjk3ZTA3Y2FhODBhZWJhZmFkZDQ5YjIxNzM3MTg3NWJhNDJhIiwidGFnIjoiIn0%3D; _ga_EMKDTWG87G=GS1.1.1734488409.2.1.1734490047.0.0.0; _ga=GA1.3.1433230611.1734450784; TawkConnectionTime=0; twk_uuid_62b413377b967b11799613cd=%7B%22uuid%22%3A%221.gNHagPN1xcRjbln8PvFc6DgzCMzjwYPneN0XFsHPrra88inRRCOrborx4HKy7w8zOIKC7h24BxBICRpZ6yABCpdX7MrGfyjV0qMiE4MbW6C1KABuF5YpxjICeM1UIU5ut%22%2C%22version%22%3A3%2C%22domain%22%3A%22kalimatimarket.gov.np%22%2C%22ts%22%3A1734490047842%7D',
    'priority': 'u=0, i',
    'referer': 'https://kalimatimarket.gov.np/comparative-prices',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = requests.get('https://kalimatimarket.gov.np/price', cookies=cookies, headers=headers)
# Parse HTML response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')

# Print the table in a readable format
if table:
    # Extract headers if present
    headers = table.find('thead')
    if headers:
        headers_row = headers.find('tr')
        header_columns = headers_row.find_all('th')
        print(' | '.join(col.get_text(strip=True) for col in header_columns))
        print('-' * (len(header_columns) * 20))  # Print a separator line

    # Extract rows
    tbody = table.find('tbody')
    if not tbody:  # Fallback to using all rows if tbody is not found
        tbody = table

    for row in tbody.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            print(' | '.join(col.get_text(strip=True) for col in columns))
else:
    print("No table found in the response.")
    