import argparse
import subprocess

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description='Preprocess a Processing source file.')
    parser.add_argument('source_dir', metavar='source_dir', type=str, help='the directory of the source files')
    args = parser.parse_args()

    subprocess.call(["processing-java", "--sketch=" + args.source_dir, "--run"])

if __name__ == '__main__':
    main()
