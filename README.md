# Аналіз Відношень

## :busts_in_silhouette: Розподілення розробки функцій:
* _Тетяна Присяжник та Ліля Кушта_ - читання відношення з файлу, запис відношення 
в файл. Пошук симетричного та рефлексивного замикання відношень.
* _Остап Дутка_ - пошук транзитивного замикання відношень з використанням алгоритму Уоршела.
Перевірка чи відношення є транзитивним.
* _Устим Ганик_ - розбиття відношення еквівалентності на класи еквівалентності.
* _Богдан Магомета_ - підрахунок кількості усіх транзитивних відношень на множині з n елементів.

## :bookmark_tabs: Описи функцій:

### Знаходження класів еквівалентності

##### :question: Що таке класи еквівалентності?
Нехай R – відношення еквівалентності на множині А. Множину всіх елементів, які
еквівалентні до елемента a ∈ A, називають класом еквівалентності (елемента а) за
відношенням R.
***
**Для знаходження класів еквівалентності** у відношенні еквівалентності варто скористатися 
функцією **find_equiv_classes(relations)**. У аргументах вона приймає список кортежів 
пар елементів, та повертає список списків класів еквівалентності.

```
   >>> find_equiv_classes([(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)])
   [[0, 1], [2, 3]]
```
***
### Читання відношень з матриці
Функція **matrix_to_relations(matrix)** приймає матрицю у вигляді списку списків,
та повертає список кортежів пар елементів. _Індексація починається з 0._
```
>>> matrix_to_relations([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)]
```

###  Пошук транзитивного замикання відношення:

**warshall_alg(rel)** - функція, що приймає матрицю у форматі списку списків і за допомогою 
**алгоритму Уоршела** знаходить транзитивне замикання заданого матрицею відношення. Повертає матрицю 
у вигляді списку списків.
Алгоритм Уоршела використовується для знаходження транзитивного замикання, працює з булевою матрицею.

***
_Псевдокод алгоритму Уоршела:_
```
rel (<- matrix)
for j to n:
    for i to n:
        if rel[i][j] == 1:
            rel[i] = rel[i] ∨ rel[j]
    next i
next j
```

Ітеруємо по колонках, якщо у колонці є 1, то порівнюємо ряди матриці за
індексом ```i``` та ```j``` за допомогою диз'юнкції.  Порівняння реалізоване 
у функції **compare(lst1, lst2)**, яка приймає два ряди (списки) матриці і 
порівнює їхні елементи між собою, формується новий список після порівняння, 
на який буде замінено ```rel[i]```, тобто рядок, де була знайдена 1.

Приклад роботи **compare(lst1, lst2)**:
```
>>> compare([0, 0, 1], [0, 1, 1])
[0, 1, 1]
```
***
**check_transition(rel)** - функція, що приймає матрицю у форматі списку списків і за допомогою функції **warshall_alg(rel)** перевіряє чи задане відношння є транзитивне, тобто чи знайдене за допомогою алгоритму Уоршела транзитивне замикання є таким самим як задане користувачем. Повертає ```True``` або ```False```.

Приклад роботи **check_transition(rel)**:
```
>>> check_transition([[0, 0], [0, 0]])
True
```
***
## :smiley: Враження від виконання проєкту:
> Кажуть, що пояснюючи комусь матеріал, ви самі глибше опановуєте тему, знаходите
> прогалини у своїх знаннях. Пояснити пайтону дискретну математику досить важко, однак
> виконання цього непростого завдання безперечно зробило мої знання більш ґрунтовними - **Устим Ганик**
***
## :speech_balloon: Зворотний зв'язок викладачам та асистентам:
> Завдання були простими на перший погляд, але при розробці заставили досить так довго
> думати над пошуком найефективнішого розв'язання проблем. Також цінним був досвід
> використання github'у для співпраці у команді- **Устим Ганик**
