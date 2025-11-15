# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a Python Back-end Bootcamp repository from DIO (Digital Innovation One) in partnership with Luizalabs. It contains educational materials and exercises covering Python fundamentals, organized in sequential lessons (Aula 2 through Aula 10).

## Project Structure

The repository is organized as a learning progression:

- **Aula 2**: First Python program (Hello World)
- **Aula 3**: Variables, data types, type conversion, input/output
- **Aula 4**: Operators (arithmetic, comparison, logical, assignment, identity, membership)
- **Aula 5**: Control structures (conditionals, loops, indentation)
- **Aula 6**: Strings and string methods
- **Aula 7**: Lists with comprehensive examples of list methods
- **Aula 8**: Tuples
- **Aula 9**: Dictionaries with extensive method examples
- **Aula 10**: (Content pending)

Each lesson contains standalone Python files demonstrating specific concepts. Advanced lessons (7-9) have organized subdirectories with numbered examples for each method or concept.

## Development Commands

### Running Python Files
```bash
python3 "path/to/file.py"
```

### Running Files with Spaces in Path/Name
```bash
python3 "Aula X/filename.py"
```

### Running Specific Examples
```bash
# Lists examples
python3 "Aula 7/01 - Listas/00_declarando_listas.py"

# Dictionary examples  
python3 "Aula 9/04 - Dicionários/00_declarando_dicionarios.py"
```

## Code Architecture

### Learning Structure
- **Sequential Learning**: Each lesson builds upon previous concepts
- **Method-Focused Examples**: Advanced topics (lists, dicts) have individual files for each method
- **Standalone Files**: Each Python file is self-contained and can be run independently

### Code Style Patterns
- Portuguese comments and variable names (educational content in Brazilian Portuguese)
- Simple, educational examples focusing on one concept per file
- Print statements to demonstrate results
- Commented-out code sections showing alternative approaches
- Use of descriptive variable names (e.g., `produto_1`, `produto_2`)

### File Naming Convention
- Numbered files for sequential examples: `00_declarando_listas.py`, `01_acesso_direto.py`
- Descriptive names for concept files: `operadores_aritmeticos.py`, `estruturas_condicionais.py`

## Working with This Codebase

### Testing Individual Concepts
Run any Python file directly to see the concept demonstration:
```bash
python3 "Aula 4/operadores_aritmeticos.py"
```

### Exploring Data Structure Methods
Navigate to specific subdirectories for comprehensive method examples:
- Lists: `Aula 7/01 - Listas/`
- Dictionaries: `Aula 9/04 - Dicionários/`

### Understanding Code Progression
Follow lessons sequentially (Aula 2 → Aula 10) as each builds on previous concepts. When modifying or adding examples, maintain the educational progression and simple, demonstrative style.

### Language Context
This is Brazilian Portuguese educational content. Comments, variable names, and output messages are in Portuguese. When adding new content, maintain consistency with the existing language and educational approach.