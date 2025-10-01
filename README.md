# LegacyExtract

Entity extraction tool for Legacy New Homes contracts. Automates the tedious stuff - pulls data from PDFs, sets up Windows folders in the right spots, fills out document templates, and automates data entry.

## What it does

Processes real estate contracts from Legacy New Homes, extracting ~40 data fields and automatically creating the folder structure needed for closings. Built this to handle repetitive document workflows at my job - turns a 20-minute manual process into a 2-second automated one.

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Drag in a PDF, verify the data looks right, hit process. Done.

## Core Features

**PDF Processing** - Uses pdfminer to extract text from contracts, then regex patterns to pull out buyer names, addresses, sale prices, closing dates, agent info, etc.

**Folder Creation** - Generates client folders with proper naming convention (`LastName 25-`) and standard subdirectories

**Document Generation** - Templates out file labels and setup docs using the extracted data. Tracks label numbers (1-20) across sessions.

**Data Export** - Outputs to `.pxt` format for integration with other systems

## Tech Stack

- PyQt6 for the GUI (dark theme because obviously)
- pdfminer.six for PDF text extraction  
- python-docx/docxtpl for Word doc generation
- regex parsing for entity extraction

## File Structure

```
main.py                 # Entry point
processing_logic.py     # The actual extraction engine
gui/
  ├── main_window.py    # Main app window
  ├── tabs/             # Processing & data viewer tabs
  └── widgets.py        # Custom drag-drop PDF widget
templates/              # Word templates for doc generation
```

## Output

Creates this folder structure automatically:
```
ClientName 25-/
├── overlay.pxt         # All extracted data
├── [contract].pdf      # Copy of original
├── Setup/
│   ├── Label.docx     
│   └── setupdocs.docx
├── TitleSearch/
└── Emails/
```

## Notes

Built specifically for Legacy New Homes contracts - the regex patterns are tuned for their specific format. Could be adapted for other contract types by modifying the parsing logic in `processing_logic.py`.

Currently defaults to `T:\Closings\Legacy SELLER` for output - change in the GUI or modify the default in `gui/tabs/processing_tab.py`.
