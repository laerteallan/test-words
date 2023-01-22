from src.exceptions import ErrorNotListValid


class ControllerWords:

    @staticmethod
    def wowels_count(list_words):
        vowels = ["a", "e", "i", "o", "u"]
        if not isinstance(list_words, list):
            raise ErrorNotListValid("List invalid!")

        response = {}
        for word in list_words:
            count = 0
            for item in word:
                if str(item).lower() in vowels:
                    count += 1
            response.update({word: count})
        return response

    @staticmethod
    def sort_list(list_words, order):

        if order == 'asc':
            list_words.sort()
            return list_words

        list_words.sort(reverse=True)
        return list_words
