<<<<<<< HEAD:5 LyThuyetThongTin/Baitaplon/Bai3/Bai3.1/vd.tab.h
/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
=======
/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
>>>>>>> 2390338784d48f8b5bc6acb46b5ec169fd1eeff1:5 LyThuyetThongTin/Baitaplon/Bai2/Câu 3/a/vd.tab.h
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
<<<<<<< HEAD:5 LyThuyetThongTin/Baitaplon/Bai3/Bai3.1/vd.tab.h
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */
=======
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */
>>>>>>> 2390338784d48f8b5bc6acb46b5ec169fd1eeff1:5 LyThuyetThongTin/Baitaplon/Bai2/Câu 3/a/vd.tab.h

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

<<<<<<< HEAD:5 LyThuyetThongTin/Baitaplon/Bai3/Bai3.1/vd.tab.h
/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */
=======
/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */
>>>>>>> 2390338784d48f8b5bc6acb46b5ec169fd1eeff1:5 LyThuyetThongTin/Baitaplon/Bai2/Câu 3/a/vd.tab.h

#ifndef YY_YY_VD_TAB_H_INCLUDED
# define YY_YY_VD_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

<<<<<<< HEAD:5 LyThuyetThongTin/Baitaplon/Bai3/Bai3.1/vd.tab.h
/* Token type.  */
=======
/* Token kinds.  */
>>>>>>> 2390338784d48f8b5bc6acb46b5ec169fd1eeff1:5 LyThuyetThongTin/Baitaplon/Bai2/Câu 3/a/vd.tab.h
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
<<<<<<< HEAD:5 LyThuyetThongTin/Baitaplon/Bai3/Bai3.1/vd.tab.h
    T_CONSTANT = 258,
    T_UMINUS = 259,
    T_ENDL = 260,
    UMINUS = 261
  };
=======
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    T_CONSTANT = 258,              /* T_CONSTANT  */
    T_UMINUS = 259,                /* T_UMINUS  */
    T_ENDL = 260                   /* T_ENDL  */
  };
  typedef enum yytokentype yytoken_kind_t;
>>>>>>> 2390338784d48f8b5bc6acb46b5ec169fd1eeff1:5 LyThuyetThongTin/Baitaplon/Bai2/Câu 3/a/vd.tab.h
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

<<<<<<< HEAD:5 LyThuyetThongTin/Baitaplon/Bai3/Bai3.1/vd.tab.h
int yyparse (void);

=======

int yyparse (void);


>>>>>>> 2390338784d48f8b5bc6acb46b5ec169fd1eeff1:5 LyThuyetThongTin/Baitaplon/Bai2/Câu 3/a/vd.tab.h
#endif /* !YY_YY_VD_TAB_H_INCLUDED  */
