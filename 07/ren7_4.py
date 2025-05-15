wikipedia_header = """
From Wikipedia, the free encyclopedia
This article is about the online encyclopedia. For Wikipedia's home page, see Main Page. For the primary English-language Wikipedia, see English Wikipedia. For other uses, see Wikipedia (disambiguation).
Wikipedia is a free content online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and the use of the wiki-based editing system MediaWiki. Wikipedia is the largest and most-read reference work in history. It is consistently ranked as one of the ten most popular websites in the world, and as of 2024 is ranked the fifth most visited website on the Internet by Semrush, and second by Ahrefs. Founded by Jimmy Wales and Larry Sanger on January 15, 2001, Wikipedia is hosted by the Wikimedia Foundation, an American nonprofit organization that employs a staff of over 700 people.
Initially only available in English, editions in other languages have been developed. Wikipedia's editions, when combined, comprise more than 62 million articles, attracting around 2 billion unique device visits per month and more than 14 million edits per month (about 5.2 edits per second on average) as of November 2023. Roughly 26% of Wikipedia's traffic is from the United States, followed by Japan at 5.9%, the United Kingdom at 5.4%, Germany at 5%, Russia at 4.8%, and the remaining 54% split among other countries, according to data provided by Similarweb.
Wikipedia has been praised for its enablement of the democratization of knowledge, extent of coverage, unique structure, and culture. It has been criticized for exhibiting systemic bias, particularly gender bias against women and geographical bias against the Global South (Eurocentrism). While the reliability of Wikipedia was frequently criticized in the 2000s, it has improved over time, receiving greater praise from the late 2010s onward while becoming an important fact-checking site.
Wikipedia has been censored by some national governments, ranging from specific pages to the entire site. Articles on breaking news are often accessed as sources for frequently updated information about those events.
"""

def main():
    word_count = {}
    for word in wikipedia_header.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print(sorted_word_count)

if __name__ == "__main__":
    main()
