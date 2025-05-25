# `select_related` and `prefetch_related` in Django
When we access related objects (like `foreign keys`), Django may run extra queries, which can slow down our app. To solve this, Django gives us:
- select_related() — for `ForeignKey` and `OneToOneField`
- prefetch_related() — for `ManyToManyField` and `reverse ForeignKey`

# `select_related()` – Joins with SQL (Good for ForeignKey)
## Use cases
- Accessing a related object from a `ForeignKey`
- We want fewer database hits

## Model
Suppose we have models `Author` and `Book`.
```py
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```
## Without `select_related()`
```py
books = Book.objects.all()
for book in books:
    print(book.title, book.author.name)  # One query for books, one per author = N+1 queries
```

## With `select_related()`
```py
books = Book.objects.select_related('author')
for book in books:
    print(book.title, book.author.name)  # Only 1 query (JOIN)
```

### What happens
```sql
SELECT * FROM book
JOIN author ON book.author_id = author.id;
```

# prefetch_related() – Separate Query + Python Join (Good for ManyToMany and reverse FK)
## Use cases
- Accessing `reverse relationships` or `ManyToMany`
- We want Django to batch fetch related objects

## Without `prefetch_related`
```py
authors = Author.objects.all()
for author in authors:
    print(author.name, [book.title for book in author.books.all()])  # N+1 queries
```
### What Django does
First query to get all authors:
```sql
SELECT * FROM author;
```
Then for each author, a separate query to get their books:
```sql
SELECT * FROM book WHERE author_id = 1;
SELECT * FROM book WHERE author_id = 2;
SELECT * FROM book WHERE author_id = 3;
```
### Result
Total queries: 1 (authors) + N (books) = N+1 queries. This is called the N+1 query problem.

## With `prefetch_related`
```py
authors = Author.objects.prefetch_related('books')
for author in authors:
    print(author.name, [book.title for book in author.books.all()])  # Only 2 queries
```

### What Django does
```sql
SELECT * FROM author;
SELECT * FROM book WHERE author_id IN (1, 2, 3, ...);
```

### Note
Here, Django already preloaded all books with a single extra query. So even though `author.books.all()` is still called, Django uses the cached, pre-fetched data in memory, not the database. So, total queries: only 2
- 1 for all authors
- 1 for all related books


# `Prefetch_related()` in `ManyToMany` relationship

## Model
```py
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')
```

## Without `prefetch_related`
```py
students = Student.objects.all()
for student in students:
    print(student.name, [course.title for course in student.courses.all()])
```

### What Django does (N+1 queries)
Query all students:
```sql
SELECT * FROM student;
```
For each student, Django will run
```sql
SELECT course.*
FROM course
JOIN course_students
  ON course.id = course_students.course_id
WHERE course_students.student_id = <student_id>;
```
For 10 students, that’s 1 (student) + 10 (courses) = 11 queries.


## With `prefetch_related`
```py
students = Student.objects.prefetch_related('courses')
for student in students:
    print(student.name, [course.title for course in student.courses.all()])
```

### What Django does (only 2 queries)
Query all students:

```sql
SELECT * FROM student;
```
Query all courses related to those students:
```sql
SELECT course.*, course_students.student_id
FROM course
INNER JOIN course_students
ON course.id = course_students.course_id
WHERE course_students.student_id IN (1, 2, 3, ...);
```
Django then builds an in-memory mapping of student → courses and avoids querying inside the loop.