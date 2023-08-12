def get_people(rank):
    people = [
        {
            "headline": "headline here",
            "Rank": 10,
            "Link": "https://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)",
            "CosineSimilarity": "0.9519",
            "Article": "የኢትዮጵያ ብሔራዊ ቡድን(ዋልያዎቹ) ከኮትዲቯር ብሔራዊ ቡድን(ዝሆኖቹ) ጋር ለ2021 የካሜሩ"
        },
        {
            "headline": "headline here",
            "Rank": 12,
            "Link": "https://www.fifa.com/fifaplus/en",
            "CosineSimilarity": "0.9519",
            "Article": "የኢትዮጵያ ወጣቶች ስፖርት አካዳሚ በአዋጅ ከተሰጡት ኃላፊነቶች መካከል አንዱ ለባለሙያዎች የአጭርና ረጅም ጊዜ የአቅም ግንባታ ስልጠናዎችን"
        },
        {
            "headline": "headline here",
            "Rank": 10,
            "Link": "https://example.com",
            "CosineSimilarity": "0.9519",
            "Article": "Another person with rank 10"
        }
    ]

    matching_people = []  # List to store all matching results

    for person in people:
        if person["Rank"] == rank:
            matching_people.append(person)

    return matching_people

results = get_people(10)
for result in results:
    print(result)