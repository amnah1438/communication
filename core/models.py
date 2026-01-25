from django.db import models
import uuid


class BoardSettings(models.Model):
    board_title = models.CharField(
        max_length=200,
        verbose_name="اسم اللوحة",
        default="معًا نصنع التعليم… شركاء في بناء المستقبل"
    )

    # سرعة حركة البطاقات (بالثواني)
    cards_speed = models.PositiveIntegerField(
        default=40,
        verbose_name="سرعة حركة البطاقات (بالثواني)",
        help_text="كلما زاد الرقم أصبحت الحركة أبطأ"
    )

    # ألوان اللوحة
    background_color = models.CharField(
        max_length=7,
        default="#0FA968",
        verbose_name="لون الخلفية الرئيسي"
    )

    card_color = models.CharField(
        max_length=7,
        default="#FFFFFF",
        verbose_name="لون البطاقة"
    )

    card_text_color = models.CharField(
        max_length=7,
        default="#1B4F72",
        verbose_name="لون نص البطاقة"
    )

    neon_color = models.CharField(
        max_length=7,
        default="#2EC4B6",
        verbose_name="لون النيون حول البطاقة"
    )

    # الشعارات
    ministry_logo = models.ImageField(
        upload_to="logos/",
        blank=True,
        null=True,
        verbose_name="شعار وزارة التعليم"
    )

    school_logo = models.ImageField(
        upload_to="logos/",
        blank=True,
        null=True,
        verbose_name="شعار المدرسة"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخر تحديث"
    )

    class Meta:
        verbose_name = "إعدادات اللوحة"
        verbose_name_plural = "إعدادات اللوحة"

    def __str__(self):
        return "إعدادات لوحة شركاء التعليم"


# ======================================================
# 📩 رسائل أولياء الأمور
# ======================================================

class ParentMessage(models.Model):
    parent_name = models.CharField(
        max_length=100,
        verbose_name="اسم ولي الأمر"
    )

    student_name = models.CharField(
        max_length=100,
        verbose_name="اسم الطالبة"
    )

    message = models.TextField(
        verbose_name="نص الرسالة"
    )

    # رمز خاص لولي الأمر (للتعديل والحذف لاحقًا)
    access_token = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="رمز التعديل والحذف"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="مفعّلة للعرض"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "رسالة ولي أمر"
        verbose_name_plural = "رسائل أولياء الأمور"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.parent_name} – {self.student_name}"
