# LanguageRef

Inspired by the first Apprenticeship Pattern from the book with the same name
(Apprenticeship Patterns) I decided to create this Language reference which
will be a runnable cheatsheet for every language that I'm working with.

# How it works

I'm going to create a file with the pattern
`<language_name>.<language_extension>` for each programming language that I
need, in it, I will create a bunch of assertions that will be something like:

    assert [1, 2, 3] == [i for i in range(1, 4)]

As you can see, the format is `<expected value> == <expression>`, this will
make me see at a glance what does what, and with the example above in mind,
I will be able to remember that range is inclusive in the first argument but
not inclusive for the second one.

Should the language not have an assertion function builtin, I shall make my
own.
