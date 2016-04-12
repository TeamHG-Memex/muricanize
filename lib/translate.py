# import sys
# import os.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', os.path.pardir)))


import os
import json
import subprocess
from muricanize.lib.buckwalter import uni2buck, buck2uni
from multiprocessing import Process, JoinableQueue, Queue
from threading import Thread
from timeit import timeit

class TranslationWorker(Thread):
    def __init__(self, q_in, q_out):
        Thread.__init__(self, target=self.run)
        self.q_in = q_in
        self.q_out = q_out
        self.dict_json = os.path.join(os.path.dirname(__file__), os.path.pardir, 'data/ar_dict.json')

        with open(self.dict_json, 'r') as f:
            self.ar_dict = json.loads(f.read())

        self.uni2buck = uni2buck
        self.buck2uni = buck2uni
        self.moses = os.path.join(os.path.dirname(__file__), 'moses')

    def run(self):
        while not self.q_in.empty():
            text = self.q_in.get()
            self.q_out.put((text, self.e2e_translate(text)))
            self.q_in.task_done()

    @staticmethod
    def clean_romanized(text):
        return text.replace('>', '&gt;').replace('<', '&lt;').replace('|', '&#124;')

    def romanize(self, text):
        # Transform the text to romanized for translation.
        ar_romanized = self.convert_ar_script(text)

        # Map known words to glue word phrases
        to_translate = self.match_phrases(ar_romanized)

        return self.clean_romanized(to_translate)

    def translate_processed(self, text):
        # Run the translation process on the text
        translated = ''
        text = subprocess.Popen(['echo', text.encode('ascii', 'backslashreplace')], stdout=subprocess.PIPE)
        moses = subprocess.Popen(['./moses', '-f', './moses-zone-interplm.ini', '-threads', '8'], stdin=text.stdout, stdout=subprocess.PIPE)

        while True:
            line = moses.stdout.readline().decode('utf-8')
            if line != '':
                translated += line
                continue
            else:
                break

        return translated

    def e2e_translate(self, text):
        romanized = self.romanize(text)
        translated = self.translate_processed(romanized)
        return translated

    def match_word(self, word):
        if word == '\n':
            return word

        try:
            if self.ar_dict[word[:2]][word]:
                return self.ar_dict[word[:2]][word]
        except:
            pass
        if '<' in word or '>' in word and 'Y' in word:
            try:
                if self.ar_dict['A-and-Y'][word]:
                    return self.ar_dict['A-and-Y'][word]
            except:
                pass
        if '<' in word or '>' in word:
            try:
                if self.ar_dict['A'][word]:
                    return self.ar_dict['A'][word]
            except:
                pass
        if 'Y' in word:
            try:
                if self.ar_dict['Y'][word]:
                    return self.ar_dict['Y'][word]
            except:
                pass
        try:
            if self.ar_dict['other'][word]:
                return self.ar_dict['other'][word]
        except:
            pass

    def convert_ar_script(self, data):
        ret = ''
        for i in range(len(data)):
            try:
                ret += self.uni2buck[data[i].encode('unicode-escape').lower()]
                continue
            except:
                if data[i] != ' ' and data[i] != '\n':
                    is_space = ' '

                    if i == 0:
                        is_space = ''

                    ret += is_space + data[i] + ' '
                    continue
                ret += data[i]
        return ret

    def match_phrases(self, data):
        lines = data.split('\n')

        output = ''
        for line in lines:
            words = line.split(' ')
            for word in words:
                next_word = self.match_word(word)

                if next_word:
                    output += next_word + ' '
                    continue

                output += word + ' '

            output += '\n'
        return output[:len(output) - 1]

class Translator():
    @staticmethod
    def get_sentences(text):
        text_arr = text.split('.')
        text_set = set()

        for sentence in text_arr:
            text_set.add(sentence)

        return text_arr

    def translate(self, orig_text):
        q_in = JoinableQueue()
        q_out = Queue()

        q_in.put(orig_text)

        # Worker was a remnant from a previous experimental input, not sure if it's still needed here.
        worker = TranslationWorker(q_in, q_out)
        worker.start()
        q_in.join()

        # This is wonky for now, because I'm going to rework how the translator works for longer
        # entries.  It will need to translate each sentence only once and then replace each sentence
        # from the original entry.
        full_translate = orig_text

        q_out.put(('', ''))
        orig, tr_text = q_out.get()

        while tr_text != '':
            full_translate = full_translate.replace(orig, tr_text)
            orig, tr_text = q_out.get()


        # Maybe this should just return the text that was translated, instead of a JSON object, not sure yet.
        return {"orig_text": orig_text, "translated_text": full_translate}
