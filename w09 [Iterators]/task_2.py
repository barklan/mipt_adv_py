import requests
import zipfile
import os
from pathlib import Path
import re
import shutil


class TextLoader():

    def __init__(self, url):

        # download and write in binary mode to temp.zip
        r = requests.get(url, allow_redirects=True)
        open('temp.zip', 'wb').write(r.content)

        # unzip temp.zip to temp folder in our current directory
        with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
            zip_ref.extractall('./temp')
            
        # delete archive
        os.remove('temp.zip')

        # make a master path
        self.master_path = Path('temp')
        
        # make a list of pathlib.Path's of all found files in master path
        self.files_list = [x for x in list(self.master_path.glob('**/*'))
                           if x.is_file()]
        
        # make an iterable from it to use it in __next__()
        self.iterable = iter(self.files_list)

    def __len__(self):
        # allows us to call len(object)
        return len(self.files_list)

    def normalize(self, string):
        s = re.sub(r'[^\w\s]', '', string)
        s = re.sub(r'[\n]', ' ', s)
        s = re.sub(r'  ', ' ', s)
        s = s.strip(' ').lower()
        return s

    def __iter__(self):
        return self
    
    def __next__(self):

        filepath = next(self.iterable)

        # read
        with filepath.open('r', encoding='utf-8') as f:
            string_read = f.read()
        
        # normalize and rewrite
        with filepath.open('w', encoding='utf-8') as f:
            string_normalized = self.normalize(string_read)
            f.write(string_normalized)

        # open in read mode and return file object
        f = filepath.open('r', encoding='utf-8')
        return f

    def __del__(self):
        shutil.rmtree(self.master_path)


if __name__ == '__main__':

    href = 'http://cs.mipt.ru/advanced_python/extra/lab9/sample.zip'
    a = TextLoader(href)


    print(f'Files found: {len(a)}\n----------\n')


    for i in range(102):  
        # We expect it to raise StopIteration around 100th
        try:
            one = next(a)
            if ((i < 3) | (i > 96)):
                print(one.read()[:50])
                print('---')
        except StopIteration:
            print('There you go')