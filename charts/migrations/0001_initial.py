# Generated by Django 2.0.13 on 2019-07-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityAttendanceTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('check_in', models.TimeField(blank=True, null=True)),
                ('check_out', models.TimeField(blank=True, null=True)),
                ('tutor_time', models.CharField(max_length=15)),
                ('commitment', models.CharField(max_length=100)),
                ('p_a', models.CharField(max_length=15)),
                ('reason_for_absence', models.CharField(max_length=100)),
                ('slot', models.CharField(max_length=15)),
                ('student_name', models.CharField(max_length=20)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('com_status', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('center', models.IntegerField()),
                ('subtopic_name', models.CharField(max_length=100)),
                ('subtopic_progress', models.IntegerField(blank=True, null=True)),
                ('topic_name', models.CharField(max_length=100)),
                ('topic_progress', models.IntegerField(blank=True, null=True)),
                ('updated', models.IntegerField()),
                ('rem_topic_count', models.IntegerField()),
                ('rem_subtopic_count', models.IntegerField()),
            ],
            options={
                'db_table': 'eblity_attendance_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityCenter',
            fields=[
                ('center_code', models.IntegerField(primary_key=True, serialize=False)),
                ('center_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'eblity_center',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityCurrentTopic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_id', models.IntegerField()),
                ('topic_id', models.IntegerField()),
                ('topic_name', models.CharField(max_length=50)),
                ('subtopic_id', models.IntegerField()),
                ('subtopic_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'eblity_current_topic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityGrade',
            fields=[
                ('grade_code', models.IntegerField(primary_key=True, serialize=False)),
                ('grade_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'eblity_grade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityJourneyTemplate',
            fields=[
                ('subtopic_id', models.IntegerField()),
                ('journey_template_key', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=30)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('time_spent', models.TimeField(blank=True, null=True)),
                ('feedback', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'eblity_journey_template',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityLogTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('resource_type', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.CharField(max_length=15)),
                ('subtopic_id', models.IntegerField(blank=True, null=True)),
                ('topic_name', models.CharField(max_length=25)),
                ('subtopic_name', models.CharField(max_length=25)),
                ('tut_end_time', models.TimeField()),
                ('tut_start_time', models.TimeField()),
                ('tutor_time', models.FloatField()),
            ],
            options={
                'db_table': 'eblity_log_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityPlanTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=100)),
                ('weightage', models.CharField(max_length=15)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(max_length=15)),
                ('hours', models.IntegerField(blank=True, null=True)),
                ('subject', models.CharField(max_length=20)),
                ('topic_progress', models.IntegerField()),
                ('subject_progress', models.IntegerField()),
                ('subtopic_id', models.IntegerField(blank=True, null=True)),
                ('subtopic_name', models.CharField(max_length=100)),
                ('subtopic_progress', models.IntegerField()),
                ('subtopic_status', models.CharField(max_length=15)),
                ('topic_status', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'eblity_plan_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityResources',
            fields=[
                ('resource_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subtopic_id', models.IntegerField()),
                ('resource_type', models.CharField(max_length=30)),
                ('resource_link', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'eblity_resources',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblitySlot',
            fields=[
                ('slot_code', models.IntegerField(primary_key=True, serialize=False)),
                ('slot_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'eblity_slot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityStudentTable',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('grade', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('parent_email', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=15)),
                ('slot', models.IntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('center', models.IntegerField()),
            ],
            options={
                'db_table': 'eblity_student_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblitySubtopicTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('subtopic_id', models.IntegerField()),
                ('subtopic_name', models.CharField(max_length=25)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('max_minutes', models.FloatField(blank=True, null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('mean_minutes', models.FloatField(blank=True, null=True)),
                ('min_minutes', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'eblity_subtopic_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityTopicTable',
            fields=[
                ('topic_id', models.IntegerField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=100)),
                ('weightage', models.CharField(max_length=15)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('subject', models.CharField(max_length=100)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(max_length=15)),
                ('mean_minutes', models.FloatField(blank=True, null=True)),
                ('max_minutes', models.FloatField(blank=True, null=True)),
                ('pre_mid_term', models.CharField(max_length=15)),
                ('mid_term', models.CharField(max_length=15)),
                ('pre_final_term', models.CharField(max_length=15)),
                ('final_term', models.CharField(max_length=15)),
                ('min_minutes', models.FloatField(blank=True, null=True)),
                ('hours', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'eblity_topic_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EblityUserprofileinfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_type', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('first_name_p', models.CharField(max_length=50)),
                ('last_name_p', models.CharField(max_length=50)),
                ('center_type', models.IntegerField()),
                ('slot', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'eblity_userprofileinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LgData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('topic', models.TextField(blank=True, null=True)),
                ('subtopic', models.TextField(blank=True, null=True)),
                ('ld_type_id', models.TextField(blank=True, db_column='LD_type_ID', null=True)),
                ('lg_desc', models.TextField(blank=True, db_column='LG_desc', null=True)),
                ('lg_strength', models.FloatField(blank=True, db_column='LG_strength', null=True)),
                ('strong_or_weak', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lg_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerfTrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('subject_progress', models.IntegerField(blank=True, null=True)),
                ('topic', models.TextField(blank=True, null=True)),
                ('topic_progress', models.IntegerField(blank=True, null=True)),
                ('subtopic', models.TextField(blank=True, null=True)),
                ('subtopic_progress', models.IntegerField(blank=True, null=True)),
                ('sub_sub_topic', models.TextField(blank=True, null=True)),
                ('blto', models.TextField(blank=True, db_column='BLTO', null=True)),
                ('difficulty_level', models.TextField(blank=True, null=True)),
                ('timespent', models.IntegerField(blank=True, null=True)),
                ('attempts', models.IntegerField(blank=True, null=True)),
                ('errors', models.IntegerField(blank=True, null=True)),
                ('is_solved', models.NullBooleanField()),
                ('fundaas', models.IntegerField(blank=True, null=True)),
                ('bonus_fundaas', models.TextField(blank=True, null=True)),
                ('lg_type_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'perf_trail',
                'managed': False,
            },
        ),
    ]
