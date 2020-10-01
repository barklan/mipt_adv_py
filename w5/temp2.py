# coding=UTF-8


class Publication:
    __title = ""
    __text = ""

    def __init__(self, title, text):
        self.__title = title
        self.__text = text

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def set_title(self, title):
        self.__title = title

    def set_text(self, text):
        self.__text = text

    def __str__(self):
        return self.get_str()


class News(Publication):
    __publication_date = ""
    __sources = []

    def __init__(self, title, text, publication_date, sources):
        super().__init__(title, text)
        self.__publication_date = publication_date

        self.set_sources(sources)

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_publication_date(self):
        return self.__publication_date

    def set_sources(self, sources):
        if not isinstance(sources, list):
            self.__sources = [sources]
        else:
            self.__sources = sources

    def get_sources(self):
        return self.__sources

    def get_str(self):
        return " ".join(["News:", self.get_title(), "\n",
                        "Text:", self.get_text(), "\n",
                        "Publication date:", self.get_publication_date(), "\n",
                        "Sources: ", " ".join(self.get_sources()), "\n",
                        "------------------------------------------------\n"])


class Announcement(Publication):
    __out_date = ""

    def __init__(self, title, text, out_date):
        super().__init__(title, text)
        self.__out_date = out_date

    def get_out_date(self):
        return self.__out_date

    def set_out_date(self, out_date):
        self.__out_date = out_date

    def get_str(self):
        return " ".join(["Announcement:", self.get_title(), "\n",
                        "Text:", self.get_text(), "\n",
                        "Out date:", self.get_out_date(), "\n",
                        "------------------------------------------------\n"])

class Article(Publication):
    __authors = []

    def __init__(self, title, text, authors):
        super().__init__(title, text)
        self.set_authors(authors)

    def set_authors(self, authors):
        if not isinstance(authors, list):
            self.__authors = [authors]
        else:
            self.__authors = authors

    def get_authors(self):
        return self.__authors

    def get_str(self):
        return " ".join(["Article:", self.get_title(), "\n",
                        "Text:", self.get_text(), "\n",
                        "Authors:", ", ".join(self.get_authors()), "\n",
                        "------------------------------------------------\n"])

if __name__ == "__main__":

    news = News("Braking news!", "That's a really exiting news!", "12 of November 2016", ["CNN", "BBC"])
    announce = Announcement("New announcement!", "I want to by an elephant!", "15 of December 2016")
    article = Article("We have new investigation", "Мы изобрели зелененький глазовыколупыватель", ["Профессор Бред",
                                                                                                   "Ассистент Капитан Очевидность"])
    
    strange_list = [news, announce, "Просто кусок непонятного бреда", article]

    for element in strange_list:
        if isinstance(element, Publication):
            print(element)
