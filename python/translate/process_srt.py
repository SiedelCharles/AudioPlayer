import re
def process_srt(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        pattern = re.compile(r'^\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]\s*')
        with open(source_file, 'r', encoding='utf-8') as fin, \
             open(output_file, 'w', encoding='utf-8') as fout:
            for line in fin:
                processsed_line = pattern.sub("", line)
                fout.write(processsed_line)
        
if __name__ == "__main__":
    source_file = "prime_context.txt"
    output_file = "processed_context.txt"
    process_srt(source_file, output_file)
            
