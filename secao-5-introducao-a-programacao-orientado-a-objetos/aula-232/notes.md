# Teoria: polimorfismo, assinatura de métodos e Liskov Substitution Principle

O polimorfismo é o princípio que permite que classes derivadas de uma super classe tenham métodos com a mesma assinatura, porém com comportamentos diferentes.

A fim de evitar a alta complexidade na herança entre classe, existem alguns padrões de projetos para tal fim, e um deles é o **SOLID**. Dentre os princípios 5 princípios do SOLID, iremos abordar o Liskov Substitution Principle (ou Princípio da substituição de Liskov).

Esse princípio foi desenvolvida pela matemática Barbara Liskov o qual diz que os objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.