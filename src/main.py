# Resolve the problem!!

import re

def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        for i in f:          
            mensaje = re.findall('[a-z]', i)
            mensaje = ''.join(mensaje)
        
        print(mensaje)


if __name__ == '__main__':
    run()
