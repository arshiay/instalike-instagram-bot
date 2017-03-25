

class ContentManager:
    __media_list = []
    __media_algorithm = None

    def get_media_generator(self):
        if not self.__media_list:
            self.download_media()

        yield self.__media_list.pop()

    def download_media(self):
        pass
