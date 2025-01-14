import os
import re
import argparse
from slugify import slugify
import yaml

def split_markdown(file_path, output_dir=None, toc_file=None, main_toc_title="Exercises"):
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    if output_dir is None:
        output_dir = os.path.dirname(file_path)
    else:
        os.makedirs(output_dir, exist_ok=True)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all headers (###, ##, #)
    pattern = re.compile(r'^(#{1,3})\s+(.*)', re.MULTILINE)
    matches = list(pattern.finditer(content))

    if not matches:
        print("No headers found in the file.")
        return

    sections = []
    chapter_files = {}
    current_section_title = None

    for i, match in enumerate(matches):
        header_level, header_title = match.groups()
        start_index = match.end()
        end_index = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section_content = content[start_index:end_index].strip()

        if header_level == '##':
            current_section_title = header_title
            slug = slugify(header_title)
            filename = f"{slug}.md"
            placeholder_path = os.path.join(output_dir, filename)
            if not os.path.exists(placeholder_path):
                with open(placeholder_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {header_title}\n\n*This section serves as a placeholder for related content.*\n")
                print(f"Created placeholder: {placeholder_path}")
            chapter_files[current_section_title] = os.path.splitext(os.path.relpath(placeholder_path, start=os.getcwd()).replace('\\', '/'))[0]

        elif header_level == '###':
            slug = slugify(header_title)
            filename = f"{slug}.md"
            counter = 1
            while os.path.exists(os.path.join(output_dir, filename)):
                filename = f"{slug}-{counter}.md"
                counter += 1

            section_full_content = f"# {header_title}\n\n{section_content}\n"
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as out_f:
                out_f.write(section_full_content)

            print(f"Created: {output_path}")
            sections.append({
                'file': os.path.splitext(os.path.relpath(output_path, start=os.getcwd()).replace('\\', '/'))[0],
                'title': header_title,
                'section': current_section_title or main_toc_title
            })

    if toc_file:
        if not os.path.isfile(toc_file):
            print(f"Error: The ToC file '{toc_file}' does not exist.")
            return

        with open(toc_file, 'r', encoding='utf-8') as f:
            toc_content = f.read()
        toc = yaml.safe_load(toc_content) if toc_content.strip() else {}

        if toc is None:
            toc = {}

        if 'chapters' not in toc or toc['chapters'] is None:
            toc['chapters'] = []

        section_map = {}
        for section in sections:
            section_map.setdefault(section['section'], []).append({
                'file': section['file'],
                'title': section['title']
            })

        for sec_title, sec_files in section_map.items():
            chapter = next((c for c in toc['chapters'] if c.get('title') == sec_title), None)
            if not chapter:
                chapter = {
                    'file': chapter_files.get(sec_title, ''),
                    'title': sec_title,
                    'sections': []
                }
                toc['chapters'].append(chapter)
            chapter['sections'].extend(sec_files)

        with open(toc_file, 'w', encoding='utf-8') as f:
            yaml.dump(toc, f, sort_keys=False)
        print(f"Updated ToC: {toc_file}")

def main():
    parser = argparse.ArgumentParser(description="Split a Markdown file by ### headers.")
    parser.add_argument('file', help="Path to the input Markdown file.")
    parser.add_argument('-o', '--output-dir', help="Directory to save the split files.", default=None)
    parser.add_argument('-t', '--toc', help="Path to the _toc.yml file to update.", default=None)
    parser.add_argument('--toc-title', help="Title for the ToC.", default="Exercises")

    args = parser.parse_args()
    split_markdown(args.file, args.output_dir, args.toc, args.toc_title)

if __name__ == "__main__":
    main()
