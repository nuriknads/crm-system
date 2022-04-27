from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32, blank=True)
    company = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.email})'


class Deal(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        IN_PROGRESS = 'in_progress', 'В работе'
        WON = 'won', 'Успех'
        LOST = 'lost', 'Провал'

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='deals')
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    close_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} — {self.amount} ({self.get_status_display()})'


class Task(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1, 'Низкий'
        MEDIUM = 2, 'Средний'
        HIGH = 3, 'Высокий'

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['done', '-priority', 'due_date']

    def __str__(self):
        return self.title
# Commit 4 — 2021-02-10
# Commit 8 — 2021-02-22
# Commit 22 — 2021-04-05
# Commit 34 — 2021-05-11
# Commit 36 — 2021-05-17
# Commit 37 — 2021-05-20
# Commit 42 — 2021-06-04
# Commit 50 — 2021-06-28
# Commit 52 — 2021-07-04
# Commit 59 — 2021-07-25
# Commit 66 — 2021-08-15
# Commit 3 — 2021-02-07
# Commit 4 — 2021-02-10
# Commit 7 — 2021-02-19
# Commit 18 — 2021-03-24
# Commit 19 — 2021-03-27
# Commit 23 — 2021-04-08
# Commit 25 — 2021-04-14
# Commit 30 — 2021-04-29
# Commit 37 — 2021-05-20
# Commit 50 — 2021-06-28
# Commit 62 — 2021-08-03
# Commit 65 — 2021-08-12
# Commit 67 — 2021-08-18
# Commit 76 — 2021-09-14
# Commit 90 — 2021-10-26
# Commit 109 — 2021-12-22
# Commit 114 — 2022-01-06
# Commit 115 — 2022-01-09
# Commit 121 — 2022-01-27
# Commit 124 — 2022-02-05
# Commit 129 — 2022-02-20
# Commit 131 — 2022-02-26
# Commit 132 — 2022-03-01
# Commit 134 — 2022-03-07
# Commit 135 — 2022-03-10
# Commit 140 — 2022-03-25
# Commit 142 — 2022-03-31
# Commit 144 — 2022-04-06
# Commit 148 — 2022-04-18
# Commit 151 — 2022-04-27
