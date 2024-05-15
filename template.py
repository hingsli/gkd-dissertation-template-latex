import os

def create_directory(path):
    """ Helper function to create a directory if it doesn't exist. """
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"Directory {path} already exists.")

def create_file(path, content=""):
    """ Helper function to create a file with optional initial content. """
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    project_root = "my-dissertation"
    
    # Create the root directory
    create_directory(project_root)
    
    # Create main.tex and other root-level tex files
    create_file(os.path.join(project_root, "main.tex"), "% Main document\n")
    create_file(os.path.join(project_root, "preamble.tex"), "% Preamble settings\n")
    create_file(os.path.join(project_root, "abstract.tex"), "% Abstract\n")
    create_file(os.path.join(project_root, "acknowledgments.tex"), "% Acknowledgments\n")
    
    # Create directories for chapters, figures, tables, and appendices
    chapters_dir = os.path.join(project_root, "chapters")
    figures_dir = os.path.join(project_root, "figures")
    tables_dir = os.path.join(project_root, "tables")
    appendices_dir = os.path.join(project_root, "appendices")
    
    create_directory(chapters_dir)
    create_directory(figures_dir)
    create_directory(tables_dir)
    create_directory(appendices_dir)
    
    # Create placeholder chapters and appendices
    for i in range(1, 4):  # Example for 3 chapters
        create_file(os.path.join(chapters_dir, f"chapter{i}.tex"), f"% Chapter {i}\n")
    
    for i in range(1, 3):  # Example for 2 appendices
        create_file(os.path.join(appendices_dir, f"appendix{i}.tex"), f"% Appendix {i}\n")
    
    # Create bibliography file
    create_file(os.path.join(project_root, "bibliography.bib"), "% Bibliography\n")

if __name__ == "__main__":
    main()
