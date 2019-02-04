import sys, codecs

train_set = 0 
dev_set = 1

class Word:
    def __init__(self, string):
        self.string = self._normalize(string)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)
    
    def _normalize(self, string):
        return string.replace("</s>","SIL").replace("[silence]", "SIL").replace("<UNK>", "SIL")

    def to_string(self):
        start = self.phones[0].start
        end = self.phones[-1].end
        return "%.4f %.4f %s" % (start, end, self.string)

class Phone:
    def __init__(self, string):
        self.symbol, self.start, self.end = self.process_string(string)
        if self.start == 1: #beginning of the sentence
            self.start = 0.0
        #self.end = -1
    
    def set_end(self, value):
        self.end = value

    def process_string(self, string):
        line = string.split(" ")[1:]
        symbol = line[0].split(":")[0]
        if symbol == '1' or symbol == '70':
            symbol = "SIL"
        else:
            symbol = 'phn' + symbol
        return symbol, float(line[2]) * 0.01, float(sum([int(element) for element in line[2:]])) * 0.01
    
    def to_string(self):
        return "%.4f %.4f %s" % (self.start, self.end, self.symbol)

def match(files_id, index, f_id):
    for i in range(len(files_id)):
        if f_id == files_id[i][index]:
            return True, files_id[i][-1]
    return False, None

def process_lines(lines, files_id, index):
    Corpus = dict()
    i = 0
    valid = False
    while(i < len(lines)):
        line = lines[i]
        if "sid=" in line: #id case
            f_id = line.replace(".001","").split("=")[-1]
            valid, f_id = match(files_id, index, f_id)
            if valid:
                Corpus[f_id] = []
            i += 1
        elif "@ word=" in line and valid: #flag beginning of a word
            fragments = line.split("word=")[-1].split(" ")
            string = fragments[0]
            i += 1 #put the index on the first phone
            num_phones = int(fragments[1].replace("nbs=",""))
            word_element = Word(string)
            for _ in range(num_phones): #read phone
                p = Phone(lines[i])
                word_element.add_phone(p)
                i += 1
            Corpus[f_id].append(word_element)

        else: #trash
            i += 1
    return Corpus

def save_ids(dictionary, f_path):
    with open(f_path,"w") as output_file:
        for key in dictionary.keys():
            output_file.write(key + "\n")

def write_wrd(dct1, dct2):
    for dct in [dct1, dct2]:
        for key in dct.keys():
            with open("wrd/" + key + ".wrd", "w") as output_file:
                for word_element in dct[key]:
                    output_file.write(word_element.to_string() + "\n")

def write_phn(dct1, dct2):
    for dct in [dct1, dct2]:
        for key in dct.keys():
            with open("phn/" + key + ".phn", "w") as output_file:
                for word_element in dct[key]:
                    for phone in word_element.phones:
                        output_file.write(phone.to_string() + "\n")

def process():
    train_lines = [line.strip() for line in open(sys.argv[1],"r", errors="ignore")]
    dev_lines = [line.strip() for line in open(sys.argv[2],"r", errors="ignore")]
    files_id =[("_".join(line.strip().split("_")[1:]), line.strip()) for line in open(sys.argv[3],"r")]

    train_dict = process_lines(train_lines, files_id, train_set)
    dev_dict = process_lines(dev_lines, files_id, dev_set)

    #print(len(train_dict), len(dev_dict))

    save_ids(train_dict, "train.ids")
    save_ids(dev_dict, "dev.ids")

    #merge silence

    write_wrd(train_dict, dict())#, dev_dict)
    write_phn(train_dict, dict())#, dev_dict)


if __name__ == "__main__":
    process()