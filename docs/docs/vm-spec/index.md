# T3 VM Specification

The technical specification for the T3 Virtual Machine — the runtime engine that executes TADS 3 programs. This is reference material for VM implementors and advanced developers.

## Overview

- **[Introduction](intro.md)** — What the T3 VM is and what this specification covers
- **[Design Philosophy](philosophy.md)** — Goals and trade-offs behind the VM's design
- **[Design Goals](goals.md)** — Specific requirements the VM was designed to meet
- **[Notation and Conventions](notation.md)** — Symbols and formatting used in this specification

## Architecture

- **[Machine Model](machine-model.md)** — Registers, stack, memory model, and execution basics
- **[The Metaclasses](metaclasses.md)** — The built-in object types the VM provides
- **[Byte-Code Instruction Set](bytecode.md)** — Complete listing of VM opcodes
- **[Image File Format](image-format.md)** — Structure of compiled `.t3` game files
- **[Portable Binary Encoding](binary-encoding.md)** — Cross-platform integer and data encoding

## Reference

- **[Character Mapping](character-mapping.md)** — How the VM handles character set conversions
- **[Debug Records](debug-records.md)** — Debug information embedded in image files
- **[t3vm Function Set](function-set.md)** — VM-level built-in functions
- **[Metaclass Identifier List](metaclass-ids.md)** — Canonical identifiers for all metaclasses
- **[Saving and Restoring State](save-restore.md)** — How game state is serialized and restored
- **[TADS Special Characters](special-characters.md)** — Character codes with special meaning to TADS
