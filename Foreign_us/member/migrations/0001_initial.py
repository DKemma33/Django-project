# Generated by Django 4.2.4 on 2023-08-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('member_email', models.CharField(max_length=200, unique=True)),
                ('member_nickname', models.CharField(max_length=200, unique=True)),
                ('member_intro', models.CharField(max_length=300)),
                ('member_intro_detail', models.TextField()),
                ('member_type', models.CharField(choices=[('Y', '일반 회원'), ('N', '탈퇴 회원'), ('A', '관리자')], default='Y', max_length=1)),
                ('member_address', models.CharField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'tbl_member',
            },
        ),
        migrations.CreateModel(
            name='MemberSNS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sns_type', models.CharField(max_length=200)),
                ('sns_url', models.CharField(max_length=500)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_member_sns',
            },
        ),
        migrations.CreateModel(
            name='MemberFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='member/%Y/%m/%d')),
                ('file_type', models.CharField(choices=[('P', '프로필 사진'), ('B', '배경 사진')], default='P', max_length=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
        ),
    ]
