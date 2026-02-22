# Language Reference

A comprehensive guide to the TADS 3 programming language — its syntax, type system, object model, and runtime features.

## Core Language

- **[Introduction](intro.md)** — Overview of TADS 3 and what sets it apart
- **[Typographical Conventions](syntax.md)** — Notation used throughout the documentation
- **[Naming Conventions](naming.md)** — Standard naming practices for identifiers
- **[Hello, World!](hello.md)** — Your first TADS 3 program
- **[Source Code Structure](progstru.md)** — How source files and projects are organized
- **[Source File Character Sets](charmap.md)** — Character encoding for source files
- **[The Preprocessor](preproc.md)** — Macros, conditional compilation, and `#include`

## Types and Expressions

- **[Fundamental Datatypes](types.md)** — Integers, strings, objects, lists, and more
- **[String Literals](strlit.md)** — Single-quoted, double-quoted, and triple-quoted strings
- **[Enumerators](enum.md)** — Named constants and token enumerators
- **[Expressions and Operators](expr.md)** — Arithmetic, logical, comparison, and special operators

## Object Model

- **[The Object Inheritance Model](inherit.md)** — Single and multiple inheritance
- **[Object Definitions](objdef.md)** — Defining objects, classes, and templates
- **[Inline Objects](inlineobj.md)** — Creating objects inside expressions
- **[Operator Overloading](opoverload.md)** — Custom operator behavior for your classes
- **[Multi-Methods](multmeth.md)** — Methods dispatched on multiple argument types
- **[Dynamic Object Creation](dynobj.md)** — Creating objects at runtime
- **[Garbage Collection](gc.md)** — Automatic memory management and finalization

## Procedural Code

- **[Procedural Code](proccode.md)** — Statements, loops, and control flow
- **[Optional Parameters](optparams.md)** — Default values for function and method parameters
- **[Named Arguments](namedargs.md)** — Passing arguments by name
- **[Exceptions and Error Handling](except.md)** — `try`/`catch`/`finally` and throwing exceptions
- **[Anonymous Functions](anonfn.md)** — Closures and short-form anonymous functions

## Advanced Features

- **[Capturing Undefined Methods](undef.md)** — Intercepting calls to nonexistent properties
- **[Reflection](reflect.md)** — Inspecting objects and types at runtime
- **[Extending Intrinsic Classes](icext.md)** — Adding methods to built-in classes
- **[Exporting Symbols](export.md)** — Making symbols available across modules
- **[VM Error Codes](errmsg.md)** — Runtime error codes and their meanings

## System Library

- **[Program Initialization](init.md)** — Startup sequencing and `PreinitObject`/`InitObject`
- **[Main Program Entrypoint](startup.md)** — The `main()` function and game startup
- **[Basic Tokenizer](tok.md)** — The system tokenizer for parsing text
- **[Miscellaneous Library Definitions](libmisc.md)** — Utility functions and definitions
- **[Replacing the Standard Library](nodef.md)** — Building without the default system library

## User Interface

- **[The Output Formatter](fmt.md)** — Text formatting, HTML tags, and output streams
- **[The Default Display Function](dispfn.md)** — How `say()` and double-quoted strings work
- **[The Banner Window Display Model](banners.md)** — Multi-window text UI layout

## Web UI

- **[The Web UI](webui.md)** — Browser-based play with HTML and JavaScript
- **[Deploying Your Web UI Game](webdeploy.md)** — Publishing a web-playable game
- **[Setting Up a Custom TADS Web Server](webhost.md)** — Hosting your own game server

Start with the [Introduction](intro.md) for an overview of the language, or jump to [Hello, World!](hello.md) to see a minimal program.
