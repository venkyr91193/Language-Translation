import sys, os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.dirname(__file__))))

from translator import Translator


def test_translate():
    obj = Translator()
    output_sentence = obj.translate("संयुक्त राष्ट्र के प्रमुख का कहना है कि सीरिया में कोई सैन्य समाधान नहीं है", "hindi", "french")
    assert output_sentence == "Le chef de l 'ONU affirme qu 'il n 'y a pas de solution militaire dans la Syrie."
    output_sentence = obj.translate("Hello, I am good", "english", "french")
    assert output_sentence == "Bonjour je vais bien"


if __name__ == "__main__":
    test_translate()
    print('All tests passed')
