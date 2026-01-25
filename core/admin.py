from django.contrib import admin
from .models import BoardSettings, ParentMessage


# ======================================================
# ⚙️ إعدادات لوحة الشركاء
# ======================================================

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
        "logo_preview",
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
            "fields": (
                "ministry_logo",
                "school_logo",
                "logo_preview",
            )
        }),
        ("معلومات النظام", {
            "fields": ("created_at", "updated_at")
        }),
    )

    def logo_preview(self, obj):
        if obj.ministry_logo:
            return f'<img src="{obj.ministry_logo.url}" style="height:80px;margin-left:10px;" />'
        return "لا يوجد شعار مرفوع"

    logo_preview.short_description = "معاينة الشعار"
    logo_preview.allow_tags = True


# ======================================================
# 📩 رسائل أولياء الأمور
# ======================================================

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

    actions = ["activate_messages", "deactivate_messages"]

    @admin.action(description="تفعيل الرسائل المختارة")
    def activate_messages(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="إلغاء تفعيل الرسائل المختارة")
    def deactivate_messages(self, request, queryset):
        queryset.update(is_active=False)
