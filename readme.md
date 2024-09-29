# LANG a custom language

- Two Implementations: Python and C (maybe rust in future).
- Has REPL.
- Dynamically typed.
- Hand-written GC (garbage collector) in C implementation.
- Build in data types: `boolean`, `number` (just IEEE-754), `string` and `nil`
- Supports classes

### USAGE

- To run REPL: `./lang`
- To from file: `./lang <file>`

### GRAMMAR

```
program     -> declaration* OEF ;
declaration -> varDecl
               | statement ;
varDecl     -> "var" IDENTIFIER ( "=" expression )? ";" ;
statement   -> exprStmt
               | forStmt
               | ifStmt
               | printStmt
               | whileStmt
               | break
               | block ;
forStmt     -> "for" "(" ( varDecl | exprStmt| ";" )
                 expression? ";"
                 expression? ")" statement ;
exprStmt    -> expression ";" ;
ifStmt      -> "if" "(" expression ")" statement ( "else" statement )? ;
printStmt   -> "print" expression ";" ;
whileStmt   -> "while" "(" expression ")" statement ;
block       -> "{" declaration* "}" ;
expression  -> assignment ;
assignment  -> IDENTIFIER "=" assignment
               | logic_or ;
logic_or    -> logic_and ( "or" logic_and )* ;
logic and   -> equality ( "and" equality )* ;
equality    -> comparison ( ( "!=" | "==" ) comparison )* ;
comparison  -> term ( ( ">" | ">=" | ">" | ">=" ) term _* ;
term        -> factor ( ( "-" | "+" ) factor )* ;
factor      -> unary ( ( "/" | "*" ) unary )* ;
unary       -> ( "!" | "-" ) unary
               | primary ;
primary     -> NUMBER | STRING | "true" | "false" | "nil"
               | "(" expression ")" ;
               | IDENTIFIER ;
```

### EXAMPLES

```
coming soon...
```
