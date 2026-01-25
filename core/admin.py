from django.contrib import admin
from .models import BoardSettings, ParentMessage


@admin.register(BoardSettings)
class BoardSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "board_title",
        "cards_speed",
        "background_color",
        "neon_color",
        "updated_at",
    )

    list_editable = (
        "cards_speed",
        "background_color",
        "neon_color",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("معلومات اللوحة", {
            "fields": ("board_title",)
        }),
        ("إعدادات الحركة", {
            "fields": ("cards_speed",)
        }),
        ("ألوان التصميم", {
            "fields": (
                "background_color",
                "card_color",
                "card_text_color",
                "neon_color",
            )
        }),
        ("الشعارات", {
            "fields": ("ministry_logo", "school_logo")
        }),
        ("معلومات النظام", {
            "fields": ("created_at", "updated_at")
        }),
    )


@admin.register(ParentMessage)
class ParentMessageAdmin(admin.ModelAdmin):
    list_display = (
        "parent_name",
        "student_name",
        "is_active",
        "created_at",
    )

    list_filter = ("is_active",)
    search_fields = ("parent_name", "student_name", "message")
    readonly_fields = ("access_token", "created_at")
