def main():
    # Register the program's command line arguments
    parser = ArgumentParser(description='Markdown contents list generator.')
    parser.add_argument("-i", "--input", dest="input", help="Specify the markdown file to generate the content list from.", type=str, required=True)
    arguments = parser.parse_args()

## App entry
if __name__ == '__main__':
    main()
