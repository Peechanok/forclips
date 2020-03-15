from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    SINGLE = '01'
    MULTIPLE = '02'
    TYPES = (
        (SINGLE, 'Single answer'),
        (MULTIPLE, 'Multiple answer')
    )
    question_type = models.CharField(max_length=2, choices=TYPES, default='01')
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)

    def __str__(self):
        return '(%s) %s' % (self.poll.title, self.text)


class Choice(models.Model):
    text = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self):
        return '(%s) %s' % (self.question.text, self.text)


class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # กำหนด constraint unique_together ว่า user หนึ่งจะสามารถตอบคำถามข้อใดๆ ได้เพียง 1 ครั้ง
        unique_together = ['question', 'answer_by']