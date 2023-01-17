def count_words_in_file(in_file, out_file):
    counts = {}
    with open(in_file, 'r') as f:
        for l in f:
            # Split words on spaces.
            W = l.lower().split(' ')
            for w in W:
                if w != '':
                    if w in counts:
                        counts[w] += 1
                    else:
                        counts[w] = 0

    with open(out_file, 'w') as f:
        for k in counts.keys():
            f.write( k + ","+ str(counts[k]) + "\n")



if __name__ == "__main__":
   count_words_in_file(
        'module3_modularcode/data/input_file.txt', 
        'module3_modularcode/results/output_file.txt')