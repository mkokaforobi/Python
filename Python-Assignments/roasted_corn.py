class roasted_corn:

    def string_length(text):
        count = 0
        for character in text:
            count += 1
        return count

    def add_ing(text):
        if self.string_length(text) < 3:
            return text
        if text.endswith("ing"):
            return text + "ly"
        return text + "ing"

    def remove_odd_index_characters(text):
        result = ""
        for index in range(self.string_length(text)):
            if index % 2 == 0:
                result += text[index]
        return result

    def repeat_string(text, times):
        if isinstance(times, float):
            return text
        return text * times

    def square_each(numbers):
        squares = []
        for number in numbers:
            squares.append(number * number)
        return squares

    def sum_of_squares(numbers):
        total = 0
        for number in numbers:
            total += number * number
        return total
