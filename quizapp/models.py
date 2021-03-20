from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils import timezone

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(_('username'),unique=False, max_length=235)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = "Users"
        

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name



class Questions(models.Model):
    question =  models.CharField(max_length=500,null=True,blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"  
        db_table = "quesions"

class QuestionChoices(models.Model):
    question = models.ForeignKey('Questions', models.DO_NOTHING, null=True, blank=True)
    is_right_choice = models.BooleanField(default=False)
    choice = models.CharField(max_length=500,null=True,blank=True)

    class Meta:
        verbose_name = "question_choice"
        verbose_name_plural = "question_choices"  
        db_table = "question_choices"



class UserQuestionAnswers(models.Model):
    user =  models.ForeignKey('User', models.DO_NOTHING, null=True, blank=True)
    choice = models.ForeignKey('QuestionChoices', models.DO_NOTHING, null=True, blank=True)
    question =   models.ForeignKey('Questions', models.DO_NOTHING, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    answer_time =  models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "question_answer"
        verbose_name_plural = "question_answers"  
        db_table = "question_answers"



