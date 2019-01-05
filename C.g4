/*
 [The "BSD licence"]
 Copyright (c) 2013 Sam Harwell
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/** C 2011 grammar built from the C11 Spec */
grammar C;

compilationUnit :   (functionDefinition  |   declaration)* EOF;

functionDefinition:   typeSpecifier declarator compoundStatement ;

typeSpecifier
    :  CONST? ('int' | 'void' | 'char') POINTER?
    ;

declarator
    :   Identifier      # pureIdentifier
    |   Identifier '[' assignmentExpression? ']'       # arrayIdentifier
    |   Identifier '(' parameterTypeList? ')' /* function definition or function declaration */    # functionDefinitionOrDeclaration
    ;

statement
    :   compoundStatement
    |   expression ';'
    |   'if' '(' expression ')' statement ('else' statement)?
    |   'while' '(' expression ')' statement
    |   'for' '(' forDeclaration? ';' forExpression? ';' forExpression? ')' statement
    |   'continue' ';'
    |   'break' ';'
    |   'return' expression? ';'
    ;

forDeclaration :   typeSpecifier initDeclaratorList;

/* forExpression is the same as expression, but just for simplicity we rename it forExpression.
(so that every statement has at most 1 expression) */
forExpression :   assignmentExpression (',' assignmentExpression)*;

compoundStatement
    :   '{' blockItem* '}'
    ;

blockItem
    :   statement
    |   declaration
    ;

declaration
    :   typeSpecifier initDeclaratorList ';'
    ;

initDeclaratorList
    :   initDeclarator (',' initDeclarator)*
    ;

initDeclarator
    :   declarator
    |   declarator '=' initializer
    ;

primaryExpression
    :   Identifier
    |   Constant
    |   StringLiteral
    ;

postfixExpression
    :   primaryExpression
    |   postfixExpression '[' expression ']'
    |   postfixExpression '(' expression? ')'
    ;

castExpression
    :   unaryExpression
    |   DigitSequence // for
    |   castExpression ('*' | '/') castExpression
    |   castExpression ('-' | '+') castExpression
    ;

unaryExpression
    :   postfixExpression
    |   '++' postfixExpression
    |   '--' postfixExpression
    ;

relationalExpression
    :   castExpression
    |   castExpression '<' castExpression
    |   castExpression '<=' castExpression
    |   castExpression '>' castExpression
    |   castExpression '>=' castExpression
    ;

equalityExpression
    :   relationalExpression
    |   equalityExpression '==' relationalExpression
    |   equalityExpression '!=' relationalExpression
    ;

logicalAndExpression
    :   equalityExpression
    |   logicalAndExpression '&&' equalityExpression
    ;

logicalOrExpression
    :   equalityExpression
    |   logicalOrExpression '||' equalityExpression
    ;

assignmentExpression
    :   logicalAndExpression
    |   logicalOrExpression
    |   unaryExpression '=' assignmentExpression
    ;

expression :   assignmentExpression (',' assignmentExpression)* ;

parameterTypeList :   parameterList (',' '...')? ;

parameterList :   parameterDeclaration (',' parameterDeclaration)* ;

parameterDeclaration :   typeSpecifier declarator ;

initializer
    :   assignmentExpression
    |   '{' initializerList? ','? '}'
    ;

initializerList
    :   initializer (',' initializer)*
    ;


CONST : 'const';
POINTER : '*';

Identifier:   [a-zA-Z_]  (   [a-zA-Z_]  |   [0-9])* ;

Constant:   [1-9] [0-9]*;

DigitSequence:   [0-9]+;

StringLiteral:   '"' SCharSequence? '"' | '\'' SChar '\'';

fragment
SCharSequence:   SChar+;

fragment
SChar
    :   ~["\\\r\n]
    |   '\\' ['"?abfnrtv0\\]
    |   '\\\n'   // Added line
    |   '\\\r\n' // Added line
    ;

Whitespace  :   [ \t]+  -> skip;

Newline  :   (   '\r' '\n'?   |   '\n')  -> skip;

BlockComment    :   '/*' .*? '*/'   -> skip;

LineComment   :   '//' ~[\r\n]*   -> skip;
