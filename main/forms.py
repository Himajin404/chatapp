from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # AuthenticationForm を追加
from .models import Talk, User
from django.core.exceptions import ValidationError

TABOO_WORDS = [
    "ばか",
    "バカ",
    "あほ",
    "アホ",
    "Fuck",
    "Shit",
    "Wanker",
    "Cunt",
    "fuck",
    "shit",
    "wanker",
    "cunt",
    "ファック",
    "ファッキュー",
    "しね",
    "死ね",
    "シネ",
    "ｼﾈ",
    "くたばれ",
    "bitch",
    "ビッチ",
    "あま",
    "クソアマ",
    "アマ",
    "くそあま",
    "Whore",
    "Hoe",
    "Nigger",
    "whore",
    "hoe",
    "nigger",
    "ﾀﾋﾈ",
    "ぼけ",
    "ドアホ",
    "キモ",
    "きも",
    "⑨",
    "ブス",
    "ドブス",
    "sine"
    "雑魚"
    "ざこ"
    "ざっこ"
    "mf",
    "fck",
    "fk",
    "fUck",
    "fuCk",
    "fucK",
    "FUck",
    "FuCk",
    "FucK",
    "FUCk"
    "FUCK"
    "fUCk"
    "fUCK"
    "noob"
    "Noob"
    "L"
    "ass",
    "Ass"
    "Pussy",
    "pussy",
    "今どんな気持ち？"
]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

class LoginForm(AuthenticationForm):
    pass

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)

    def clean_message(self):
        message = self.cleaned_data["message"]
        matched = [w for w in TABOO_WORDS if w in message]
        if matched:
            raise ValidationError(f"禁止ワード {', '.join(matched)} が含まれています")
        return message

# 以下を追加
class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "新しいユーザー名"}
        help_texts = {"username": ""}

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {"email",}
        labels = {"email": "新しいメールアドレス"}
        help_texts = {"email": ""}

